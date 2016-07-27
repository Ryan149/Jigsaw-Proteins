f=open('/tmp/assemble','r')
l=f.readlines()
for i in range(len(l)):
 print l[i]
 g=l[i]
 for z in range(len(g)):
  print g[z]
