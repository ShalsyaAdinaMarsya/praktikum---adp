import math

riwayat_penerbangan = []

def hitung_jarak(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def gerak(arah, x, y):
    if arah in ['U','S','T','B']:
        d = float(input("Perpindahan : "))
        if arah == 'U': 
            return x, y+d
        if arah == 'S': 
            return x, y-d
        if arah == 'T': 
            return x+d, y
        if arah == 'B': 
            return x-d, y
        
    elif arah in ['TL','BL','TG','BD']:
        dx = float(input("Perpindahan x: "))
        dy = float(input("Perpindahan y: "))
        if arah == 'TL': 
            return x+dx, y+dy
        if arah == 'BL': 
            return x-dx, y+dy
        if arah == 'TG': 
            return x+dx, y-dy
        if arah == 'BD': 
            return x-dx, y-dy

    else:
        print("Arah tidak tersedia!")
        return x, y

def input_penerbangan():
    print("\n=== INPUT ===")
    nama = input("Nama Maskapai: ")
    jam = input("Jam Lepas Landas: ")
    n = int(input("Jumlah Pergerakan: "))

    x, y = 0, 0
    lintasan = [(0,0)]
    total_jarak = 0

    for i in range(n):
        print(f"\nPergerakan ke-{i+1}")
        arah = input("Arah (U/S/T/B/TL/BL/TG/BD): ").upper()

        x_baru, y_baru = gerak(arah, x, y)
        jarak = hitung_jarak(x, y, x_baru, y_baru)

        total_jarak += jarak
        x, y = x_baru, y_baru
        lintasan.append((x,y))
        print(f"Posisi: ({x},{y})")

    riwayat_penerbangan.append({
        "nama": nama,
        "jam": jam,
        "posisi": (x,y),
        "jarak": round(total_jarak,2),
        "lintasan": lintasan})

    print("\nKoordinat akhir:", (x,y))
    print("Total jarak:", round(total_jarak,2))

def tampilkan():
    print("\n=== RIWAYAT PENERBANGAN ===")

    if not riwayat_penerbangan:
        print("Belum ada riwayat penerbangan")
        return

    print("="*120)
    print(f"{'No':<4} {'Nama':<12} {'Jam':<12} {'Posisi Akhir':<18} {'Jarak':<10} {'Lintasan'}")
    print("-"*120)

    for i, data in enumerate(riwayat_penerbangan, 1):
        posisi = f"({data['posisi'][0]}, {data['posisi'][1]})"
        lintasan = " -> ".join([f"({p[0]}, {p[1]})" for p in data["lintasan"]])

        print(f"{i:<4} {data['nama']:<12} {data['jam']:<12} {posisi:<18} {data['jarak']:<10} {lintasan}")

    print("="*120)

def main():
    while True:
        print("\n" + "="*40)
        print("SISTEM PENCATATAN LINTASAN PESAWAT")
        print("="*40)
        print("1. Input Penerbangan")
        print("2. Riwayat Penerbangan")
        print("3. Keluar program")
        print("="*40)

        pilih = input("Pilih: ")

        if pilih == '1':
            input_penerbangan()
        elif pilih == '2':
            tampilkan()
        elif pilih == '3':
            print("\n")
            print("Terima kasih telah menggunakan program ini!")
            print("\n")
            break
        else:
            print("\n")
            print("Pilihan Anda Tidak Tersedia!")
            print("\n")

main()