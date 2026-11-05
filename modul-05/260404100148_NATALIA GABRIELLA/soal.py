"""
Ubah kode ini dengan menerapkan fungsi untuk menghitung nilai akhir, menentukan predikat, 
dan menentukan status kelulusan.

buat file baru dengan ketentuan NIM_NAMA, lalu kerjakan di file tersebut

"""

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

if nilai_akhir >= 85:
    predikat = "A"
elif nilai_akhir >= 75:
    predikat = "B"
elif nilai_akhir >= 65:
    predikat = "C"
else:
    predikat = "D"

if nilai_akhir >= 65:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("===== HASIL PENILAIAN =====")
print("Nama:", nama)
print("Nilai Akhir:", nilai_akhir)
print("Predikat:", predikat)
print("Status:", status)

