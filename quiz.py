print("Amankan diskon kalian")
harga = float(input("input harga :"))
total_produk = int(input("input total produk :"))

    
if total_produk >= 1000:
    if harga >= 10000:
        diskon = harga * 0.2
    else:
        diskon = harga * 0.1
elif total_produk >= 500:
    if harga >= 10000:
        diskon = harga * 0.15
    else:
        diskon = harga * 0.05
else:
    diskon = 0
    
harga_total = (harga-diskon)*total_produk
print(int(diskon))
print(int(harga_total))
    
