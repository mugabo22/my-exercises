import csv
import pandas as pd
import json
with open('data.csv', 'r') as file:
    bag = csv.reader(file)
    for row in bag:
        print(row)
        
data = pd.read_csv('data.csv')
print(data)

data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
with open('data.csv', 'w', newline='') as file:
    write= csv.writer(file)
    write.writerows(data)
    

data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
data.to_csv('data.csv', index=False)

#Encoding and Decoding in json
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print(json_str)

json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)
print(data)