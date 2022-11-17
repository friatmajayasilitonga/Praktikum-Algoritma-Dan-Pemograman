import time

address=("Jl. jatiwaringin - pondok gede - Jawa Barat")
np=input("masukkan nama pelanggan : ")
nt=("081361183625")
ltime = time.asctime( time.localtime(time.time()))

pilihan="y"
while pilihan=="y":
    print(""" 
    ==============================
    
             Makanan sederhana
                menu makanan 
 
    ==============================
    A. nasi goreg  : Rp 15.000
    B. mie ayam : Rp 17.000
    C. mie shop : Rp 15.000
    D. nasi pecel : Rp 18.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu makanan = "))
    jumlahpesan=int(input("masukkan jumlah pesanan = "))
    if pesan == "a":
        listnama= "nasi goreng"
        h=11000
        harga=(h*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "mie ayam"
        h=12000
        harga = (h*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "mie shop"
        h=11000
        harga=int(h*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "nasi pecel"
        h=14000
        harga=int(h*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        ltime = "-"
        listnama = "-"
        harga = "-"
        ppn = "-" 
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("-"*45)
    print(" makanan".center(45))
    print(address.center(45))
    print(nt.center(45))
    print()
    print(ltime)
    print("-"*45)
    print("nama pelanggan \t:", np)
    print("Menu \t\t:", listnama)
    print("Harga/Pcs \t:", h)
    print("Jumlah Pesan \t:", jumlahpesan)
    print("Harga \t\t:", harga)
    print("Diskon \t\t:", diskon)
    print("PPN \t\t:", ppn)
    print("-"*45)
    print("Jumlah Bayar \t:", totalharga)
    print("-"*45)
    pilihan=input("apakah anda ingin order kembali Y/N =")