pesanan = [
    ("es jeruk", "minuman"),
    ("bakso", "makanan"),
    ("laptop", "elektronik")
]

minuman = []
makanan = []
elektronik = []

for nama_produk, kategori in pesanan:
    if kategori == "minuman":
        minuman.append(nama_produk)
    elif kategori == "makanan":
        makanan.append(nama_produk )
    else:
        elektronik.append(nama_produk)

print("daftar minuman:", minuman)
print("daftar makanan:", makanan)
print("daftar elektronik:",elektronik)