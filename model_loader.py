import json

filename = 'wavenet/Models/WaveNet3-ds1.json'

# https://medium.com/@vaibhaw.vipul/building-a-dilated-convnet-in-pytorch-f7c1496d9bf5

with open(filename, 'r') as f:
    data = json.loads(f.read())
    keys = list(data.keys())
    print(keys)
    
    k = keys[-2] 
    print(k)
    a = data[k]
    print("="*80)

    print(type(a))
    if type(a) == list:
        print(len(a))
        print("*"*80)
        for x in a:
            print(x)
            # print(f"name: {x['name']} layer_idx: {x['layer_idx']} len_data: {len(x['data'])}")
    else:
        print(a)
