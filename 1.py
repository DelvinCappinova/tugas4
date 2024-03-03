# def cek_angka(a,b,c):
#     if a!=b!=c!=a:
#         if a == b + c or b == a + c or c == a + b: 
#             return True
#         return False
# print (cek_angka (1,2,3))
# print (cek_angka (3,2,5))
# print (cek_angka (8,3,5))
# print (cek_angka (1,2,6))


cek_angka = lambda a, b, c: True if (a!=b!=c!=a and (a+b==c or b+c==a or c+a==b)) else False

print (cek_angka (1,2,3))
print (cek_angka (3,2,5))
print (cek_angka (8,3,5))
print (cek_angka (1,2,6))