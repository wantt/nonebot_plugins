import json

with open('my_export.json','r') as f:
    load_dict = json.load(f)
    
for k in load_dict.keys():
    print(type(load_dict[k]))
    print(load_dict[k])
    del load_dict[k][0]
    print(load_dict[k])
