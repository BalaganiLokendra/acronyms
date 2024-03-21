s=input()
l=s.split()
l_1=[]
for element in l:
    l_1+= element[0]
    l_1+=["."]
a=len(l_1)
b=a-1
string=""
for i in range(0,b):
    string +=l_1[i]
print(string)