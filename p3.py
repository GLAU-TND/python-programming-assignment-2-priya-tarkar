t=int(input())
q=bin(t)
print(q)
q=q[2:]
print(max(map(len,q.split('0'))))
