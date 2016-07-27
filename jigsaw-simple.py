import re
seq="sqtap","tapal","apalt"
a=seq[0]
b=seq[1]
c=seq[2]
print a
print b
print c
i=0
g=5
status="No_Match"
while (status=="No_Match"):
 if (a[i]==b[g-2]) and (a[i+1]==b[g-1]) and (a[i+2]==b[g]):
  print "Success"
  status="Match"
 else:
  i=i+1
  print "Fail"
