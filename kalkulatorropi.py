while True:
    # BANNER
    print("\n")
    print("+=========================================+")
    print("|                                          ")
    print("|              KALKULATOR KU               ")
    print("|                                          ")
    print("+=========================================+")
    print("| Jenis Operasi                    ")
    print("+=========================================+")
    print("| [>] Penjumlahan           : Kode [1]")
    print("| [>] Pengurangan           : Kode [2]")
    print("| [>] Perkalian             : Kode [3]")
    print("| [>] Pembagian             : Kode [4]")
    print("+=========================================+")
# INPUT
    bilangan_1 = int(input("| [+] Bilangan Pertama      : "))
    Operasi = int(input("| [!] Jenis Operasi         : "))
    bilangan_2 = int(input("| [+] Bilangan Kedua        : "))
    print("+=========================================+")
# PENJUMLAHAN
    if Operasi == 1:
        nama = "Pertambahan"
        print("| [=] Hasil                 :", bilangan_1 + bilangan_2)
        print("+=========================================+")
        coba_lagi = input("| [!] Coba Lagi [iya|tidak] : ")
        print("+=========================================+")
        if coba_lagi == "iya" or coba_lagi == "IYA":
            continue
        elif coba_lagi == "tidak" or coba_lagi == "TIDAK":
            print("\n")
            break
        else:
            print("| [!] Masukan Tidak Valid.")
            print("+=========================================+")
            break
# PENGURANGAN
    elif Operasi == 2:
        nama = "Pengurangan"
        print("| [=] Hasil                 :", bilangan_1 - bilangan_2)
        print("+=========================================+")
        coba_lagi = input("| [!] Coba Lagi [iya|tidak] : ")
        print("+=========================================+")
        if coba_lagi == "iya" or coba_lagi == "IYA":
            continue
        elif coba_lagi == "tidak" or coba_lagi == "TIDAK":
            print("\n")
            break
        else:
            print("| [!] Masukan Tidak Valid.")
            print("+=========================================+")
            break
# PERKALIAN
    elif Operasi == 3:
        nama = "Pertambahan"
        print("| [=] Hasil                 :", bilangan_1 * bilangan_2)
        print("+=========================================+")
        coba_lagi = input("| [!] Coba Lagi [iya|tidak] : ")
        print("+=========================================+")
        if coba_lagi == "iya" or coba_lagi == "IYA":
            continue
        elif coba_lagi == "tidak" or coba_lagi == "TIDAK":
            print("\n")
            break
        else:
            print("| [!] Masukan Tidak Valid.")
            print("+=========================================+")
            break
# PEMBAGIAN
    elif Operasi == 4:
        nama = "Pertambahan"
        print("| [=] Hasil                 :", bilangan_1 / bilangan_2)
        print("+=========================================+")
        coba_lagi = input("| [!] Coba Lagi [iya|tidak] : ")
        print("+=========================================+")
        if coba_lagi == "iya" or coba_lagi == "IYA":
            continue
        elif coba_lagi == "tidak" or coba_lagi == "TIDAK":
            print("\n")
            break
        else:
            print("| [!] Masukan Tidak Valid.")
            print("+=========================================+")
            break
    else:
        print("| [!] Jenis Operasi Tidak Tersedia.")
        print("+=========================================+")
        break
