import json
from ast import literal_eval

dict_data = {"key1": "['data1', 'data2'], "key2" : "['data3']"}
actual_data = json.loads(dict_data)
for key, value in actual_data.items():
    actual_data[key] = literal_eval(value)   
with open('temp_data.json', 'w') as file:
    json.dump(actual_data, file)
