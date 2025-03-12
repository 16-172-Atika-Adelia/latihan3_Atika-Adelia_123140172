from abc import ABC, abstractmethod

# Kelas abstrak untuk Karyawan
class Karyawan(ABC):
    @property
    @abstractmethod
    def info(self):
        """Metode abstrak untuk menampilkan informasi karyawan"""
        pass

# Kelas untuk Karyawan Tetap
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
    
    # Method overriding dari kelas abstrak
    @property
    def info(self):
        return f"Karyawan Tetap: {self.nama}, Gaji: Rp{self.gaji}"
    
    # Method overloading (simulasi)
    def update_data(self, *args):
        if len(args) == 1:
            self.nama = args[0]
        elif len(args) == 2:
            self.nama = args[0]
            self.gaji = args[1]
    
    # Operator overloading untuk membandingkan gaji
    def __gt__(self, other):
        if isinstance(other, KaryawanTetap):
            return self.gaji > other.gaji
        return NotImplemented

# Kelas untuk Karyawan Kontrak
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, upah_per_jam, jam_kerja):
        self.nama = nama
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    
    # Method overriding dari kelas abstrak
    @property
    def info(self):
        total_upah = self.upah_per_jam * self.jam_kerja
        return f"Karyawan Kontrak: {self.nama}, Upah: Rp{total_upah}"

# Kelas untuk Freelancer
class Freelancer(Karyawan):
    def __init__(self, nama, bayaran_proyek):
        self.nama = nama
        self.bayaran_proyek = bayaran_proyek
    
    # Method overriding dari kelas abstrak
    @property
    def info(self):
        return f"Freelancer: {self.nama}, Bayaran: Rp{self.bayaran_proyek}"

# Fungsi duck typing untuk menampilkan informasi karyawan
def tampilkan_info(karyawan):
    return karyawan.info

# Contoh penggunaan
def main():
    # Membuat objek
    tetap = KaryawanTetap("Budi", 5000000)
    kontrak = KaryawanKontrak("Ani", 50000, 40)
    freelancer = Freelancer("Cici", 3000000)

    # Demonstrasi method overloading
    print(f"Info awal: {tetap.info}")
    tetap.update_data("Budi Santoso")
    print(f"Setelah update nama: {tetap.info}")
    tetap.update_data("Budi Santoso", 6000000)
    print(f"Setelah update nama dan gaji: {tetap.info}")

    # Demonstrasi operator overloading
    tetap2 = KaryawanTetap("Dedi", 4500000)
    print(f"Gaji {tetap.nama} > {tetap2.nama}: {tetap > tetap2}")

    # Demonstrasi duck typing dan abstraksi
    daftar_karyawan = [tetap, kontrak, freelancer]
    
    for karyawan in daftar_karyawan:
        info = tampilkan_info(karyawan)
        print(info)

if __name__ == "__main__":
    main()