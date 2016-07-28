f=open('/tmp/assemble','r')
l=f.readlines()
x=0
y=1
count1=0
count2=0
while y in range(0,185):
 s1=l[x]
 s2=l[y]
 a=s1[count1],s1[count1+1],s1[count1+2],s1[count1+3]
 b=s2[count2],s2[count2+1],s2[count2+2],s2[count2+3]
 if (a==b):
  
 elif (a!=b):
  solution=a
  count2=count2+1
