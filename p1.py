l=[i for i in input().split()]
p=[]
for i in l:
	if(len(i)==1):
		p.append(i)
i=0
while(i<len(l)):
	if l[i] in p:
		l.remove(l[i])
		continue
	else:
		i+=1
p.sort(reverse=True)
l.sort(reverse=True)
print(p)
m=0
while(m<len(l)):
	if l[m][0] in p:
		if(l[m][l]<l[m][0]):
			p.insert(p.index(l[m][0])+1,l[m])
			print(p)
		else:
			p.inser(p.index(l[m][0]),l[m])
	else:
		p.append(l[m])
	m=m+1
print(''.join(p))
