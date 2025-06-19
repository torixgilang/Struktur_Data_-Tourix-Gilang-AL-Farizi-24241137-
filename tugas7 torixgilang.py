# pemisahan string
# buat program untuk memisahkan string berikut
# masukan nama domain anda : edy.net
# nama domain anda : edy
# domain yg anda gunakan : net

# input dari user
domain = input("Masukkan nama domain anda (contoh: edy.net): ")

# pisahkan string berdasarkan titik
nama, ekstensi = domain.split(".")

# tampilkan hasilnya
print("Nama domain anda :", nama)
print("Domain yg anda gunakan :", ekstensi)