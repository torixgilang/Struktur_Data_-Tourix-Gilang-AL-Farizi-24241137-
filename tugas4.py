# Program untuk mengecek kategori umur

# Meminta input umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Mengecek kategori umur
if umur < 18:
    print("Anda termasuk anak-anak.")
elif umur > 18:
    print("Anda termasuk dewasa.")
else:
    print("Umur Anda tepat 18 tahun.")