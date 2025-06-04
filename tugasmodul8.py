import os
os.system("cls")
list = [
    ("DICKY", "2031", "A", "ketua:acara", 92, "acara"),
    ("ADE", "2025", "C", "anggota:acara", 80, "acara"),
    ("APRIOCA", "2024", "C", "anggota:acara", 75, "acara"),
    ("MARCELLA", "2019", "A", "anggota:humas", 85, "acara"),
    ("ZHAFRAN", "3009", "A", "ketua:perlengkapan", 90, "perlengkapan"),
    ("MEISYA", "1038", "KBI", "anggota:perlengkapan", 85, "perlengkapan"),
    ("RAHMA", "2023", "C", "anggota:humas", 82, "perlengkapan"),
    ("AYSI", "1008", "A", "anggota:pelengkapan", 78, "perlengkapan"),
    ("LALA", "2031", "A", "ketua:danus", 90, "danus"),
    ("ANGGY", "1032", "B", "anggota:acara", 78, "danus"),
    ("RIVALDO", "1005", "A", "anggota:mediskom", 90, "danus"),
    ("SUCI", "3034", "A", "anggota:perlengkapan", 75, "danus"),
    ("DINDA", "2042", "B", "ketua:pubdok", 85, "pubdok"),
    ("PUJI", "1019", "C", "anggota:danus", 80, "pubdok"),
    ("DWI", "2045", "C", "anggota:humas", 80, "pubdok")]

def simpan_data(nama_file, list):
    with open("OrPSB22.txt", 'w') as file:
        for isi in list:
            baris = f"{isi[0]},{isi[1]},{isi[2]},{isi[3]},{isi[4]},{isi[5]}\n"
            file.write(baris)
simpan_data("OrPSB22.txt", list)

def pengalaman_sebelumnya(pengalaman_kepanitiaan):
    pengalaman = {}
    for data in pengalaman_kepanitiaan.split(';'):
        if ":" in data:
            peran, bidang = data.split(':')
            pengalaman[bidang.strip()] = peran.strip()
    return pengalaman

def hitung_nilai(pengalaman, bidang_dipilih, nilai_wawancara):
    nilai_plus = 0
    nilai_plus += len(pengalaman)
    if any(peran.lower() == "ketua" for peran in pengalaman.values()):
        nilai_plus += 2
    if bidang_dipilih in pengalaman:
        nilai_plus += 3
    return nilai_wawancara + nilai_plus

def proses_file(nama_file):
    with open(nama_file, 'r') as f:
        lines = f.readlines()
    data_bidang = {}
    for line in lines:
        nama, nim, kelas, pengalaman_kepanitiaan, nilai_wawancara, bidang = line.strip().split(',')
        pengalaman = pengalaman_sebelumnya(pengalaman_kepanitiaan)
        nilai_wawancara = float(nilai_wawancara)
        skor = hitung_nilai(pengalaman, bidang, nilai_wawancara)
        if bidang not in data_bidang:
            data_bidang[bidang] = []
        data_bidang[bidang].append({'nama': nama, 'nim': nim, 'kelas': kelas, 'bidang': bidang,'nilai': skor})
    
    print ("-"*50)
    print ("     HASIL REKRUTMEN KOORDINATOR BIDANG PSB 22")
    print ("-"*50)
    for bidang, peserta in data_bidang.items():
        print(f"\nTop 2 Calon Presidium Bidang {bidang.upper()}:")
        peserta_sorted = sorted(peserta, key=lambda x: x['nilai'], reverse=True)
        for i, c in enumerate(peserta_sorted[:2], 1):
            print(f"{i} Nama : {c['nama']} ({c['nim']}), (kelas {c['kelas']}) dengan skor : {c['nilai']}")
proses_file("OrPSB22.txt")
print()