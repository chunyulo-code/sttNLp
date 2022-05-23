import json
f=open(r"D:\sttNlp\output.txt","r")
data_dict = json.load(f)
dir = data_dict['dir'].lower()
bui = data_dict['bui'].lower()
func = data_dict['func'] .lower()

print(dir, bui, func)