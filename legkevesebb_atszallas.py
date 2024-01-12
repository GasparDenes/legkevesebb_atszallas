elso_sor=input('N, M')
N_str, M_str = elso_sor.split(' ')
N=int(N_str)
M=int(M_str)

jo_vonatok=[]
K=-1
start=[]
veg=[]
pos=1

for i in range(N):
    vonat=input()
    A_str, B_str = vonat.split(' ')
    A=int(A_str)
    B=int(B_str)
    start.append(A)
    veg.append(B)

print('Beolvasas vege')

def utazas():
    max = pos
    for i in range(N):
        if start[i]<=pos and veg[i]>pos and veg[i] > max:
            index = i
            max = veg[i]
    if max <=pos:
        index=-1
    return index, max


while pos!=M:
    index, max = utazas()
    if index==-1:
        print(index)
        break
    K+=1
    pos=max
    jo_vonatok.append(index+1)

if index!=-1:
    print('While vege')
    print(K)
    for i in jo_vonatok:
        print(i)