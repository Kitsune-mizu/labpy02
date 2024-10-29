# Latihan 3: Buat program python untuk kasus berikut:
## Kasus 1: Program Pemesanan Tiket Bioskop

### Contoh Input Program Python3 (Vs code)

![image](https://github.com/user-attachments/assets/efce0295-379b-42a1-9450-26fef7972b08)

#### Penjelasan Program:
1.	#### Fungsi hitung_harga_tiket:
     * Variabel tipe_tiket: Jenis tiket yang diminta di inputkan (reguler atau VIP).
     * Variabel status_member: Status keanggotaan di inputkan (ya/tidak).
     #### Harga Tiket:
     * Tiket regular = Rp50.000
     * Tiket VIP = Rp100.000
     #### Menentukan Harga Tiket:
     * Menggunakan operator ternary, jika tipe tiket adalah "reguler", maka harga tiket adalah Rp50.000, jika tidak, maka Rp100.000.
     #### Diskon:
     * Jika pengguna adalah member, diskon 20% diterapkan; jika tidak, tidak ada diskon.
     #### Menghitung Total Harga:
     * Total harga dihitung berdasarkan harga tiket dan diskon.
2.	Input dari Pengguna:
     * Program meminta pengguna untuk memasukkan tipe tiket dan status keanggotaan.
3.	Menghitung dan Menampilkan Total Harga:
     * Program memanggil fungsi hitung_harga_tiket dan mencetak total harga yang harus dibayar dengan format dua desimal.

#### Contoh Output :

![image](https://github.com/user-attachments/assets/bc628fee-24a5-4add-95c2-820792da26a9)

#### Flowchart Pemesanan Tiket Bioskop:

 ![Copy of Flowchart (1)](https://github.com/user-attachments/assets/848a6c27-341b-461d-b06f-2facd75c5c09)

#### Penjelasan flowchart :
1.	Mulai
2.	Input Tipe Tiket
     * Apakah tipe tiket "reguler"?
         * Jika True, set harga tiket = Rp50.000
         * Jika False, set harga tiket = Rp100.000
3.	Input Status Member
     * Apakah status member "ya"?
         * Jika True, diskon = 20%
         * Jika False, diskon = 0%
4.	Hitung Total Harga
     * Total harga = harga tiket × (1 - diskon)
5.	Tampilkan Total Harga
6.	 Selesai

## Kasus 2: Program Kalkulator Sederhana

### Contoh Input Program Python3 (Vs code)

![image](https://github.com/user-attachments/assets/b0b3de86-1aef-40db-8dce-7feffa5a0a1f)

#### Penjelasan Program:
1. #### Fungsi kalkulator:
     * Variabel angka1: Angka pertama dari yang di Inputkan.
     * Variabel angka2: Angka kedua dari yang Inputkan.
     * Variabel operator: Operator aritmatika yang dipilih.
     #### Operasi Aritmatika:
     * Menggunakan if, elif, dan else untuk menentukan operasi:
         * Jika operator adalah( + ), hasilnya adalah penjumlahan.
         * Jika operator adalah ( - ), hasilnya adalah pengurangan.
         * Jika operator adalah ( * ), hasilnya adalah perkalian.
         * Jika operator adalah ( / ), program memeriksa apakah angka yang di inputkan adalah nol untuk mencegah pembagian dengan nol.
     #### Return:
     * Mengembalikan hasil operasi atau pesan error jika operator tidak dikenal (tidak sesuai dengan ketentuan) atau jika ada pembagian dengan nol.
2.	Input dari Pengguna:
     * Program meminta pengguna untuk memasukkan dua angka dan operator aritmatika.
3.	Menghitung dan Menampilkan Hasil:
     * Program memanggil fungsi kalkulator dan mencetak hasil yang diperoleh.

#### Contoh Output:

![image](https://github.com/user-attachments/assets/f86d57d3-7914-4912-b48b-97445aa63f1f)
 
#### Flowchart Kalkulator Sederhana:

![Copy of Flowchart](https://github.com/user-attachments/assets/5ec3d047-8136-4a0c-b5ec-c9e755f4c0dd)

#### Penjelasan Flowchart:
1.	Mulai
2.	Input Angka Pertama
3.	Input Angka Kedua
4.	Input Operator
5.	Apakah Operator '+'?
     * Jika True, hasil = angka1 + angka2
     * Jika False, lanjut ke langkah berikutnya.
6.	Apakah Operator '-'?
     * Jika True, hasil = angka1 - angka2
     * Jika False, lanjut ke langkah berikutnya.
7.	Apakah Operator '*'?
     * Jika True, hasil = angka1 * angka2
     * Jika False, lanjut ke langkah berikutnya.
8.	Apakah Operator '/'?
     * Jika True, apakah angka2 == 0?
         * Jika True, tampilkan "Error: Pembagian dengan nol tidak diperbolehkan."
         * Jika False, hasil = angka1 / angka2
     * Jika False, tampilkan "Error: Operator tidak dikenal."
9.	Tampilkan Hasil
10.	Selesai


