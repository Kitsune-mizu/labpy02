# Fungsi untuk menghitung total harga tiket
def hitung_harga_tiket(tipe_tiket, status_member):
    # Harga tiket
    harga_reguler = 50000
    harga_vip = 100000

    # Menentukan harga berdasarkan tipe tiket
    harga_tiket = harga_reguler if tipe_tiket.lower() == 'reguler' else harga_vip

    # Menghitung diskon jika user adalah member
    diskon = 0.2 if status_member.lower() == 'ya' else 0
    total_harga = harga_tiket * (1 - diskon)

    return total_harga

# Input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ")
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")

# Menghitung total harga
total_harga = hitung_harga_tiket(tipe_tiket, status_member)

# Menampilkan hasil
print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
