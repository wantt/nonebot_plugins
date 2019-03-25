with open('./adgroup.txt','r') as f:
    for id in f.read().split('\n')[:-1]:
        print(id)

with open('./adgroup.txt','a+') as f:
    f.write('1\n')
