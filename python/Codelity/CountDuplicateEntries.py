'''
Created on 10-Oct-2020

@author: Sumedh
name     price weight
box       2      3
gloves    1      1
shirts    3      4
shirts    2      4
gloves    1      1

gloves is dupplicate hence return 1
'''

def count_duplicates(name, price, weight):
    # Write your code here
    items={}
    ans=0
    for index in range(len(name)):
        currentKey=name[index]+str(price[index])
        if (currentKey in items.keys()):
            
            if(weight[index] in items[currentKey]):
                ans+=1
            else:
                items[currentKey].append(weight[index])
        else:
            key=name[index]+str(price[index])
            items[key]=[weight[index]]
    return ans 

if __name__ == '__main__':
    name = ["box","box","box","box"]
    price = [2,2,2,2]   
    weight = [2,2,2,2]
    result = count_duplicates(name, price, weight)