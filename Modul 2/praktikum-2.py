class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama         
        self.__saldo = saldo    
    
    def lihat_saldo(self):
        print("Error: Anda tidak memiliki akses langsung ke saldo!")

akun_budi = RekeningBank("Budi", 1000000)
print(f"Nama: {akun_budi.nama}")    

try:
    print(akun_budi.__saldo)  # Ini akan menimbulkan error
except AttributeError:
    print("Error: saldo tidak dapat diakses dari luar class!")

# Jika ingin melihat saldo, harus lewat method:
akun_budi.lihat_saldo()