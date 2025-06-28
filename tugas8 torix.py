# Data harga
harga_normal = 15.5935
harga_diskon = 16.45987
harga_retail = 14.96884

# Fungsi untuk mengambil 1 dan 2 digit di belakang koma
def ambil_digit(angka):
    angka_str = str(angka)
    pecah = angka_str.split(".")
    angka_desimal = pecah[1] if len(pecah) > 1 else "0"
    
    satu_digit = angka_desimal[:1] if len(angka_desimal) >= 1 else "0"
    dua_digit = angka_desimal[:2] if len(angka_desimal) >= 2 else angka_desimal + "0"

    return satu_digit, dua_digit

# Ambil digit dari setiap harga
for label, harga in {
    "Harga Normal": harga_normal,
    "Harga Diskon": harga_diskon,
    "Harga Retail": harga_retail
}.items():
    satu, dua = ambil_digit(harga)
    print(f"{label}:")
    print(f"  Satu digit di belakang koma: {satu}")
    print(f"  Dua digit di belakang koma: {dua}")
    print()