nilai_huruf = ["A", "A-", "B+", "B", "B-", "C+", "C", "D", "E"]
nilai_angka=  [4.00, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0.00]
mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
data_mahasiswa = []

for i in range(mahasiswa):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    while True:
        indeks = input("Masukkan nilai huruf (A, A-, B+, B, B-, C+, C, D, E): ").upper()
        if indeks in nilai_huruf:
            posisi = nilai_huruf.index(indeks)
            ip = nilai_angka[posisi]
            break
        else:
            print("Nilai yang dimasukkan tidak valid, coba lagi")
    data_mahasiswa.append([nama, indeks, ip])

#untuk membuat tampilan data berurutan dari yang terbesar hingga trekecil
data_mahasiswa.sort(key=lambda x: x[2], reverse=True)
print()

print(" --------------Data Mahasiswa---------------")
print()

# untuk membuat lebar kolom
lebar_nama = 10
lebar_indeks = 17
lebar_ip = 6

print("-" * 45)
print(f"| {"Nama  ":<{lebar_nama}} || {"Nilai Angka ":<{lebar_indeks}} || {"IP  ":>{lebar_ip}} |")
print("-" * 45)

for row in data_mahasiswa:
    nama, indeks, ip = row
    print(f"| {nama:<{lebar_nama}} || {indeks:<{lebar_indeks}} || {ip:>{lebar_ip}.2f} |")
    print("-" * 45)