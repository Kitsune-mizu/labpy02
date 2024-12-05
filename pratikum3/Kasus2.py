# Fungsi kalkulator sederhana
def kalkulator(angka1, angka2, operator):
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2
    elif operator == '*':
        return angka1 * angka2
    elif operator == '/':
        # Menangani pembagian dengan nol
        if angka2 == 0:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
        return angka1 / angka2
    else:
        return "Error: Operator tidak dikenal."

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Menghitung hasil
hasil = kalkulator(angka1, angka2, operator)

# Menampilkan hasil
print(f"Hasil: {hasil}")
