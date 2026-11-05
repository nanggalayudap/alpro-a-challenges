def hitung_nilai(nama,tugas,uts,uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        predikat = "A"
        status = "LULUS"
    elif nilai_akhir >= 75:
        predikat = "B"
        status = "LULUS"
    elif nilai_akhir >= 65:
        predikat = "C"
        status = "LULUS"
    else:
        predikat = "D"
        status = "TIDAK LULUS"

    print("===== HASIL PENILAIAN =====")
    print("Nama:", nama)
    print("Nilai Akhir:", nilai_akhir)
    print("Predikat:", predikat)
    print("Status:", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)