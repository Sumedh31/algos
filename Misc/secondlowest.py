students=[]
for i in range(int(input())):
    student_list=[]
    name = input()
    student_list.append(name)
    score = float(input())
    student_list.append(score)          
    students.append(student_list)
    m1=m2=float('-inf')      
for Index in range(len(students)):
    if float(students[Index][1])>float(m1):
        m2=m1
        m1=students[Index][1]        
    elif float(students[Index][1])>float(m2) and float(students[Index][1])!=float(m1):
            m2=students[Index][1]
print(m2)
runnerup=[]
for Index in range(len(students)):
    if students[Index][1]==m2:
        runnerup.append(students[Index][0])
    print(*sorted(runnerup), sep='\n')
            
 
        

