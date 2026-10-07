
import csv
import json

def convert_csv_to_json(csv_filename):
      try:
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csvfile:
            data = list(csv.DictReader(csvfile))
        with open("data.json", mode="w", newline="",encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
      except:
        return False
