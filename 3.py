
pilih = str(input("Pilih hasil yang anda inginkan, R untuk Reamur, dan F untuk Fahrenheit :")).upper()

if pilih == "R":
    celcius = float(input("Masukkan Suhu dalam Celcius: "))
    hasil_reamur = lambda: (0.8 * celcius)
    print("suhu dalam Reamur :" ,hasil_reamur()) 
elif pilih == "F":
    celcius = float(input("Masukkan Suhu dalam Celcius: "))
    hasil_fahrenheit = lambda: ((9/5) * celcius + 32)
    print("suhu dalam Fahrenheit :" ,hasil_fahrenheit()) 
else:
    print("salah input")
    