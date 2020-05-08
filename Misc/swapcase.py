
def swap_case(s):        
    list2=[]     
    for i,char in enumerate(range(len(s))):
        
        if(97<=ord(s[i])<=122):
            list2.append(str(s[i]).upper())
        elif(65<=ord(s[i])<=90):
            list2.append(str(s[i]).lower())
        else:
            list2.append(str(s[i]))
    return "".join(list2)   

if __name__ == '__main__':
    s = "test"
    list1=[]
    for c in s:
        if c.islower():
            list1.append(c.upper())
        else:
            list1.append(c.lower())
    result = swap_case(s)
    print("".join(list1))