x = input().split()

h0,m0,hf,mf = int(x[0]),int(x[1]),int(x[2]),int(x[3])
h,m = 0,0

while True:
    if h == 24:
        break

    m0 += 1
    m += 1

    if h0 == hf and m0 == mf:
        break
    if m0 == 60:
        m0 = 0
        h0 += 1 
     
    if m == 60:
        h += 1
        m = 0
  
    
print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)"%(h,m))