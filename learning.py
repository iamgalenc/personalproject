def hitung_kecepatan():
    print("\nhitung kecepatan ready!\n")
    jarak = float(input("masukkan jarak: "))
    waktu = float(input("masukkan waktu: "))
    kecepatan = jarak * waktu
    print("\nkecepatan: ", kecepatan, "\n")
    
def hitung_luas_segitiga():
    print("\nhitung luas segitiga ready!\n")
    alas = float(input("masukkan alas: "))
    tinggi = float(input("masukkan tinggi: "))
    luas_segitiga = 0.5 * (alas * tinggi)
    print("\nluas: ", luas_segitiga, "\n")
   
def hitung_luas_balok():
    print("\nhitung luas balok ready!\n")
    panjang = float(input("masukkan panjang: "))
    lebar = float(input("masukkan lebar: "))
    tinggi = float(input("masukkan tinggi: "))
    luas_balok = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("\nluas: ", luas_balok, "\n")

def hitung_luas_bola():
    print("\nhitung luas bola ready!\n")
    radius = float(input("masukkan radius: "))
    luas_bola = 4 * 3.14 * (radius**2)
    print("\nluas: ", luas_bola, "\n")

while True:
    userInput = int(input(
        "Pilih rumus yang akan dipakai: \n\n1. Hitung kecepatan\n2. luas segitiga\n3. luas balok\n4. luas bola\n\n0. keluar program\n\npilih angka yang tertera: "))
    if(userInput == 1):
        hitung_kecepatan()
    elif(userInput == 2):
        hitung_luas_segitiga()
    elif(userInput == 3):
        hitung_luas_balok()
    elif(userInput == 4):
        hitung_luas_bola()
    else:
        break