def kecepatan_akhir (v0, a, t) :
    kecepatan_akhir = v0 + a*t
    return kecepatan_akhir
def jarak_ditempuh (v0, a, t) :
    jarak_ditempuh = v0*t + 1/2*a*t**2
    return jarak_ditempuh

n = int(input("Masukkan nilai n : "))
nilai = []

for i in range (n):
    print(f"Data ke-{1+i} :")
    v0 = float(input("Masukkan nilai kecepatan awal(vo) : "))
    a = float(input("Masukkan nilai percepatan(a) : "))
    t = float(input("Masukkan nilai waktu(t) : "))

    v_akhir = kecepatan_akhir(v0, a, t)
    jarak_akhir = jarak_ditempuh(v0, a, t) 

    nilai.append((v0, a, t, v_akhir, jarak_akhir))


print()
print ("TABEL HASIL PERHITUNGAN")
def print_nilai(data_nilai) :
    print ("-" *70)
    print(" | n | Kecepatan awal | Percepatan | Waktu | Kecepatan Akhir | Jarak |")
    print ("-" *70)
    
    i = 1
    for kecepatan_awal, percepatan, waktu, v_akhir, jarak in data_nilai:
        print(f" | {i:<1} | {kecepatan_awal:<14.0f} | {percepatan:<10.0f} | {waktu:<5.0f} | {v_akhir:<15.1f} | {jarak:<5.0f} |")
        i+=1
    print ("-" *70)
    
print_nilai(nilai)