import json

ticker = "msft"
ammount = {'total' : 5, 'price' : 201.01}
json_dict = {}
json_dict[ticker] = ammount
print(json_dict)

test = ['123123','123123']

with open('test.txt', 'w') as outfile:
    json.dump(json_dict, outfile)
outfile.close()

with open('test.txt', 'r') as f:
        datastore = json.load(f)
f.close()

print(datastore['msft']['total'])
