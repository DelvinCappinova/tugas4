cek_digit_belakang = lambda digit1, digit2, digit3: len(set(int(str(num)[-1])for num in [digit1, digit2, digit3]))<3

digit1 = int(input("Masukkan angka 1 :"))
digit2 = int(input("Masukkan angka 2 :"))
digit3 = int(input("Masukkan angka 3 :"))
print(cek_digit_belakang(digit1, digit2, digit3))
    
# print(cek_digit_belakang(30, 20, 18))  
# print(cek_digit_belakang(145, 5, 100))  
# print(cek_digit_belakang(71, 187, 18))  
# print(cek_digit_belakang(1024, 14, 94))  
# print(cek_digit_belakang(53, 8900, 658)) 