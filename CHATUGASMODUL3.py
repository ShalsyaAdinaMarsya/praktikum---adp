print ("")
M = float(input('Masukkan modal awal investasi   : Rp.'))
b = float(input('Masukkan bunga tahunan (%)      : '))
T = float(input('Masukkan target investasi       : Rp.'))
i = 1

while M <= T :
    M = M *  (1 + (b/100))
    print(f"Pada tahun ke-{i} modal : Rp.{M}")

    i = i+1
    
print ("")
print(f"Target investasi tercapai setelah {i-1} tahun")
print ("")

