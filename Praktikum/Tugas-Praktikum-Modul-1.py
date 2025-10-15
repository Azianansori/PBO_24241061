class PersegiPanjang:
    # Constructor untuk menginisialisasi atribut panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
            # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# Program utama
print("=== Program Menghitung Luas dan Keliling Persegi Panjang ===")

# Input dari pengguna
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar  : "))

# Membuat objek dari class PersegiPanjang
persegi_panjang = PersegiPanjang(p, l)

# Menampilkan hasil
print("\n=== Hasil Perhitungan ===")
print(f"Panjang      : {persegi_panjang.panjang}")
print(f"Lebar        : {persegi_panjang.lebar}")
print(f"Luas         : {persegi_panjang.hitung_luas()}")
print(f"Keliling     : {persegi_panjang.hitung_keliling()}")