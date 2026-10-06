#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file


data ={
    "name": "Sultan",
    "age": 0,
    "city": "Jazan"
}


serialize_and_save_to_file(data, "filename.json")

print("Sultan")


deserialized_data = load_and_deserialize('filename.json')

print("Jafari")
print(deserialized_data)
