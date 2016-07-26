f=open('/tmp/assemble','r')
l=f.readlines()

#this prints *third* line with newline at the end
print l[2]

#stripping newline
s=l[2].rstrip()
print s
