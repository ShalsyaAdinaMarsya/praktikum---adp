import math 

mis = 'y'
while (mis.lower() == 'y'):
    print("Berikut adalah tabel fungsi yang digunakan untuk menghitung sebuah nilai.")
    print("1. Jika x = 0, f(x) = 4x^3 + 7x - 5")
    print("   Jika x > 0, f(x) = 4x^3 + 7x - 5")
    print("   Jika x < 0, f(x) = 3x^2 - 5x + 1")
    print("2. g(x) = (f(x))^2 - (f(x))")
    print("3. h(x) = f(x) * g(x)")
    print()

    n = int(input("Masukkan banyak data n yang ingin dihitung = "))
    x = []
    for i in range(n):
        x.append(float(input(f"Input nilai x ke-{i+1} = ")))
    print()

    print("|-------------------------------------------------------------------------|")
    print("| No.   || (x)     || f(x)      || g(x)        || h(x)       |")
    print("|-------------------------------------------------------------------------|")

    for i in range(n):
        #f(X)
        if x[i] == 0:
            f_x = 4 * x[i] ** 3 + 7 * x[i] - 5
        elif x[i] > 0:
            f_x = 4 * x[i] ** 3 + 7 * x[i] - 5
        else:
            f_x = 3 * x[i] ** 2 - 5 * x[i] + 1
        
        #g(x)
        g_x = f_x ** 2 - f_x 
        #h(x)
        h_x = f_x * g_x
        
        print("| {:<6}|| {:<8}|| {:<10.2f}|| {:<11.3f}|| {:<11.2f}|".format(i + 1, x[i], f_x, g_x, h_x))
    
    print("|-------------------------------------------------------------------------|")
    print()
    
    mis = input("Apakah anda ingin memasukkan nilai x lagi ? (Y/N)\n")
    print()
