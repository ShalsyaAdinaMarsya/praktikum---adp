print("")
print("----------------- BUAT PASSWORD------------------------- ")
print("")
print("SILAHKAN BUAT PASSWORD YANG MEMENUHI KRITERIA BERIKUT :")
print("1. Harus terdiri dari minimal 8 digit ")
print("2. Harus mengandung minimal 1 huruf kecil")
print("3. Harus mengandung minimal 1 huruf kapital")
print("4. Harus mengandung minimal 1 karakter khusus")
print("   contoh : !@#$%^&*()-_=+[]{}|;:'\",.<>?/`~).")
print("")
print("=========================================================")
print("")

while True : 
    password = input("SILAHKAN BUAT PASSWORD ANDA: ")
    panjang = False
    huruf_kecil = False
    huruf_kapital = False
    angka = False 
    simbol = False
    karakter_khusus = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~)."


    for karakter in password :
        if len(password) >= 8 :
            panjang = True
        if "a" <= karakter <= "z":
            huruf_kecil = True
        elif "A" <= karakter <= "Z":
            huruf_kapital = True
        elif "1" <= karakter <= "9":
            angka = True
        elif karakter in karakter_khusus :
            s  = True
        
    else :
        if not panjang  :
            print("Password harus memuat 8 digit!")
        if not huruf_kecil :
            print("Password harus memuat minimal 1 huruf kecil!")
        if not huruf_kapital :
            print("Password harus memuat minimal 1 huruf besar!")
        if not simbol :
            print ("Password harus memuat minimal 1 karakter!")
        if not angka :
            print("Password harus memuat minimal 1 angka!")
        print("")

    
    if panjang and huruf_kecil and huruf_kapital and karakter  and angka :
        print("PASSWORD ANDA SUDAH VALID!")
        print("")
        print("=======================================================")
        break

    else :
        print("SILAHKAN BUAT PASSWORD BARU YANG SESUAI KRITERIA DIATAS!")  
        print("")
        print("========================================================")
        print("")