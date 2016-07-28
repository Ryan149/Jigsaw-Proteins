def intersect(a,b):
 return list(set(a) & set(b))

f=open('/tmp/assemble','r')
l=f.readlines()

a=l[0]
a1=0
a2=3
b=l[1]
b1=0
b2=3
i=0
x=a[a1:a2]
y=b[b1:b2]

for i in range(len(a)):
 if (x==y):
  b1=b1+1
  b2=b2+1
 if (x!=y):
   
