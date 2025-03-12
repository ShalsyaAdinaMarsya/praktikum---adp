
b = (input("Masukkan nama : "))
print ('\n')
print("DAFTAR HARGA TIKET BIOSKOP")
print ("Kode Film : 1")
print (" Judul : Captain Amerika")
print ("Harga Tiket Satuan : Rp.50000")
print ("Kode Film : 2")
print (" Judul : Keluarga Cemara")
print ("Harga Tiket Satuan : Rp.40000")
print ("Kode Film : 3")
print (" Judul : Attack On Titan")
print ("Harga Tiket Satuan : Rp.45000")
print ("Kode Film : 4")
print (" Judul :  Perayaan Mati Rasa")
print ("Harga Tiket Satuan : Rp.30000")
print ("Kode Film : 5")
print (" Judul : Qodrat")
print ("Harga Tiket Satuan : Rp.35000")
print ('\n')
print("=========================================")
a = int(input("Masukkan kode film (1-5) : "))

if a==1 :
    print (a, " Captain Amerika")
    print ("Harga Tiket Satuan : Rp.50000")
    print('\n')
    print("=========================================")
    x = 50000 
    y = int(input("Masukkan jumlah pembelian :"))
    z = x * y
    print(f'Harga Tiket : {x}')
    print (f'Total biaya : {z}')
if a==2 :
    print (a, " Keluarga Cemara")
    print ("Harga Tiket Satuan : 40000")
    print('\n')
    print("=========================================")
    x = 40000 
    y = int(input("Masukkan jumlah pembelian :"))
    z = x * y
    print(f'Harga Tiket : {x}')
    print (f'Total biaya : {z}')
elif a==3 :
    print (a, " Attack on Titan")
    print ("Harga Tiket Satuan : Rp.45000")
    print('\n')
    print("=========================================")
    x = 45000 
    y = int(input("Masukkan jumlah pembelian :"))
    z = x * y
    print(f'Harga Tiket : {x}')
    print (f'Total biaya : {z}')
elif a==4 :
    print (a, " Perayaan Mati Rasa")
    print ("Harga Tiket Satuan : Rp.30000")
    print('\n')
    print("=========================================")
    x = 30000 
    y = int(input("Masukkan jumlah pembelian :"))
    z = x * y
    print(f'Harga Tiket : {x}')
    print (f'Total biaya : {z}')
elif a==5:
    print (a, " Qodrat")
    print ("Harga Tiket Satuan : Rp.35000")
    print('\n')
    print("=========================================")
    x = 35000 
    y = int(input("Masukkan jumlah pembelian :"))
    z = x * y
    print(f'Harga Tiket           : Rp.{x}')
    print (f'Total biaya          : Rp.{z}')
else :
    print("Tidak Ditemukan")

if z>250000 :
        diskon = (z - ( 35 / 100 * z))
        potongan_harga = (35 / 100 * z)
        print(f'Harga sesudah diskon : Rp.{diskon}')
elif z>100000 :
        diskon = (z - ( 15 / 100 * z))
        potongan_harga = (15 / 100 * z)
        print(f'Harga sesudah diskon : Rp.{diskon}')
else :
        diskon = (z - ( 0 / 100 * z))
        potongan_harga = (0 / 100 * z)
        print(f'Harga sesudah diskon : Rp.{diskon}')
print('\n')

print("=========================================")
print ("        STRUCK PEMESANAN")
print("=========================================")
print(f'NAMA                  : {b}')
print(f'JUDUL FILM            : {a}') 
if a==1 :  print ("                        CAPTAIN AMERIKA")
elif a==2 :  print ("                        KELUARGA CEMARA")
elif a==3 :  print ("                        ATTACK ON TITAN")
elif a==4 :  print ("                        PERAYAAN MATI RASA")
elif a==5 :  print ("                        QODRAT")
else : print ("                 Tidak ditemukan")
print(f'JUMLAH TIKET          : {y}')
print(f'HARGA SATUAN          : Rp.{x}')
print(f'HARGA SEBELUM DISKON  : Rp.{z}')
print(f'POTONGAN HARGA        : Rp.{potongan_harga}')
print(f'HARGA SESUDAH DISKON  : Rp.{diskon}')
print("=========================================")














