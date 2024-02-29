class karyawan:
    def __init__ (self, gaji, posisi, nama):
        self.gaji = gaji
        self.posisi = posisi
        self.nama = nama

    def h(self):
        print(self.nama + " mendapatkan gaji sebesar " + self.gaji + " dengan posisi sebagai " + self.posisi)

pegawai = karyawan(gaji="10.000.000", posisi="data analyst", nama="gibran")
print(pegawai.h())