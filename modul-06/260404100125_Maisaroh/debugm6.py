data_absensi = [
    ('andi', 'hadir'),
    ('sinta','hadir'),
    ('citra', 'izin'),
    ('susi', 'izin'),
    ('fajar','alpa'),
    ('lani','alpa'),
    ]

hadir = []
izin = []
alpa = []

for nama, status in data_absensi:
    if status == "hadir":
        hadir.append(nama)
    elif status == "izin":
        izin.append(nama)
    else:
        status = alpa.append(nama)
   
print("===HASIL ABSENSI MAHASISWA===")
print("mahasiswa hadir:", hadir)
print( "mahasiswa hadir:", izin)
print("mahasiswa hadir:", alpa)