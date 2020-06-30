bgst = "HELLO WORLD"

print("String :" + (bgst))

asw= ' '.join(format(ord(i), 'b') for i in bgst)
a1= (asw[0:4])
a2= (asw[7])
a3= (asw[11:14])
a4= (asw[22:26])
a5= (asw[38:42])
a6= (asw[56:60])
a7= (asw[61:65])
a8= (asw[-17 : -7])
p = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
print("NRZ-L :" + (p))