N = int(input())
txt = input()
D = {}
for t in txt:
    D[t] = D.get(t, 0) + 1

mv, mk = 0, ''

for k, v in D.items():
    if mv < v:
        mv = v
        mk = k

print(mk, mv) 