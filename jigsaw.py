f=open('/tmp/assemble','r')
l=f.readlines()
for z in range(0,185):
 for i in range(0,z):
  g=l[z]
  h=l[i]
  if g[i] in h[i]:
   print "I win" 
