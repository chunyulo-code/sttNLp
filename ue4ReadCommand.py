import json

with open("D:\sttNlp\output.txt") as f:
    data = f.read()

js = json.loads(data)
print(js['dir', 'bui'])