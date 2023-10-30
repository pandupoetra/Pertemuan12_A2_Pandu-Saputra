import lingkaran
import segitiga
import persegi_panjang
def menu(): 
    while True:
        print()
        print ("Pilih Bentuk 2D") 
        print ()
        print ("1. Persegi Panjang")
        print ("2. Lingkaran") 
        print ("3. Segitiga") 
        print ("4. Keluar")
        pilihan=input("pilihan= ")
        if pilihan=="1":
            persegi_panjang.luas_persegi_panjang()
        elif pilihan=="2":
            lingkaran.luas_lingkaran()
        elif pilihan=="3":
            segitiga.luas_segitiga()
        elif pilihan=="4":
            break
        else:
            print("tak ada dalam menu")
menu()