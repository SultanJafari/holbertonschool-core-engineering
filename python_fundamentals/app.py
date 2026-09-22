from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# 1. تخزين مؤقت لفاتورة التقسيم الحالية
current_bill = {
    "total": 0,
    "count": 0,
    "per_person": 0,
    "statuses": []
}

# 2. قاعدة بيانات تجريبية للزبائن والديون (للبقالات والبطاقات الذكية)
customers_db = {
    "CARD123": {"name": "أحمد العتيبي", "balance": -150.0},
    "CARD456": {"name": "سعد القحطاني", "balance": -45.0},
    "CARD789": {"name": "خالد الشمري", "balance": 0.0}
}

# تخزين سجل العمليات (الإيصالات)
transactions_log = []

@app.route('/')
def index():
    return render_template('index.html')

# --- مسارات نظام تقسيم الفواتير ---
@app.route('/api/bill/set', methods=['POST'])
def set_bill():
    data = request.json
    total = float(data.get('total', 0))
    count = int(data.get('count', 1))

    current_bill['total'] = total
    current_bill['count'] = count
    current_bill['per_person'] = round(total / count, 2)
    current_bill['statuses'] = [False] * count

    return jsonify(current_bill)

@app.route('/api/bill/pay/<int:index>', methods=['POST'])
def pay_person(index):
    if 0 <= index < len(current_bill['statuses']):
        current_bill['statuses'][index] = True
    return jsonify(current_bill)

@app.route('/api/bill/status', methods=['GET'])
def get_bill_status():
    return jsonify(current_bill)

# --- مسارات نظام البطاقة الذكية والديون (البقالة) ---
@app.route('/api/store/scan', methods=['POST'])
def scan_card():
    data = request.json
    card_id = data.get('card_id')

    if card_id in customers_db:
        return jsonify({"success": True, "customer": customers_db[card_id]})
    return jsonify({"success": False, "message": "البطاقة غير مسجلة"})

@app.route('/api/store/transaction', methods=['POST'])
def store_transaction():
    data = request.json
    card_id = data.get('card_id')
    amount = float(data.get('amount', 0))
    action_type = data.get('type') # 'debt' (دين جديد) أو 'pay' (سداد)
    store_name = data.get('store_name', "بقالة الحي الذكية")

    if card_id not in customers_db:
        return jsonify({"success": False, "message": "خطأ في بيانات العميل"})

    customer = customers_db[card_id]
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    if action_type == 'debt':
        customer['balance'] -= amount  # زيادة الدين (السالب)
        msg = f"تم تسجيل مبلغ {amount} ريال كدين على الحساب بكل سرية."
    else:
        customer['balance'] += amount  # سداد جزء أو كل الدين
        msg = f"تم تسديد مبلغ {amount} ريال بنجاح."

    # حفظ تفاصيل العملية في السجل
    tx_record = {
        "store": store_name,
        "name": customer['name'],
        "card_id": card_id,
        "amount": amount,
        "type": action_type,
        "new_balance": customer['balance'],
        "time": timestamp
    }
    transactions_log.append(tx_record)

    return jsonify({
        "success": True,
        "message": msg,
        "new_balance": customer['balance'],
        "receipt": tx_record
    })

@app.route('/api/store/admin/reports', methods=['GET'])
def get_admin_reports():
    return jsonify({
        "customers": customers_db,
        "transactions": transactions_log[::-1]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
