import json
f=open(r"D:\sttNlp\output.txt","r")
data_dict = json.load(f)
dir = data_dict['dir']
bui = data_dict['bui']
func = data_dict['func'] 

print(dir, bui, func)