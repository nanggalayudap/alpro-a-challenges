"""
Kerjakan disini!!!


"""
def hitung_nilai(nama,tugas, uts, uas):

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    return nilai_akhir

def hitung_predikat(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 75:
        return "B"
    elif nilai_akhir >= 65:
        return "C"
    else:
        return "D"

def hitung_status(nilai_akhir):
    if nilai_akhir >= 65:
        return "Lulus"
    else:
        return "Tidak Lulus"

    
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Memanggil function
nilai_akhir = hitung_nilai(nama, tugas, uts, uas)
predikat = hitung_predikat(nilai_akhir)
status = hitung_status(nilai_akhir)

print("\n=== HASIL NILAI MAHASISWA ===")
print("Nama Mahasiswa :", nama)
print("Nilai Tugas    :", tugas)
print("Nilai UTS      :", uts)
print("Nilai UAS      :", uas)
print("Nilai Akhir    :", nilai_akhir)
print("Grade          :", predikat)
print("Keterangan     :", status)

