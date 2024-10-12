def tampilUtama():
    print("=========SELAMAT DATANG DI APLIKASI PINJOL=========")
    print("1. Kelola Debitur")
    print("2. Kelola pInjaman / Debitur")
    print("0. Keluar Program")

def tampilMenuKelolaDebitur():
    print("======KELOLA DEBITUR========")
    print("1. Tampilkan debitur")
    print("2. Cari Nama Debitur")
    print("3. Tambah Debitur")
    print("0. Kembali Ke Menu Utama")

def tampilKelolaPinjaman():
    print("=========KELOLA PINJAMAN========")
    print("1 Tambahkan Pinjaman Berdasarkan Nama")
    print("2. Tampilkan Seluruh Pinjaman")
    print("0. Kembali ke menu utama")


nama = []
listpinjaman = []

class Debitur:
    def __init__(self, nama, KTP, limit) -> None:
        self.nama = nama
        self.__KTP = KTP
        self._limit = limit

    @property
    def KTP(self):
        return self.__KTP
    
    @property
    def limit(self):
        return self._limit
    

# Memmbuat class turunan dari Debtiur - artinya debitur meminjam 
class Pinjaman(Debitur):
    def __init__(self, nama, KTP, limit, pinjaman, bunga, bulan ,angsuran) -> None:
        super().__init__(nama, KTP, limit)
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = angsuran


def tampilDebitur():
    for i in nama:
        # print(f"Peminjam Ke - {i+1}")
        print(f"Nama : {i.nama}")
        print(f"KTP : {i.KTP}")
        print(f"Limit Pinjaman : {i.limit} \n")

def caridebiturBerdasarkanNama():
    carinama = input("INPUTKAN NAMA YANG AKAN DICARI: ")
    for i in nama:
        if carinama == i.nama:
            print(f"Nama : {i.nama}")
            print(f"KTP : {i.KTP}")
            print(f"Limit Pinjaman : {i.limit} \n")
            return True
    print("Nama Tidak Ditemukan")

def cari(ktp):
    for i in nama:
        if ktp == i.KTP:
            return False
    return True

def TambahDebiturBerdasarkanKTP():
    while True:
        KTPstr = input("Masukkan NIK: ")
        cek = KTPstr.isdigit()
        if cek == True:
            KTP = int(KTPstr)
            cekAda = cari(KTP)
            if cekAda == True:
                namaBaru = input("Masukkan Nama Debitur Baru: ")
                while True:
                    limitPinjamanStr = input("Masukkan Limit Pinjaman: ")
                    cekLimit = limitPinjamanStr.isdigit()
                    if cekLimit == True:
                        limitPinjaman = int(limitPinjamanStr)
                        # objekDebiturBaru = input("Masukan Nama objek(Terserah): ")
                        objekDebiturBaru = Debitur(namaBaru, KTP, limitPinjaman)
                        nama.append(objekDebiturBaru)
                        return True
                    else:
                        print("LIMIT PINJAMAN HARUS BERUPA ANGKA\n")
            elif cekAda == False:
                print("NO. KTP SUDAH ADA DALAM DATABASE")
                return True
        else:
            print("NIK ATAU NOMOR KTP HARUS BERUPA ANGKA")


def cekNama(namaPeminjam):
    for i in nama:
        if namaPeminjam == i.nama:
            return True
    return False
    
def CekLimit(namaPeminjam, Pinjaman):
    for i in nama:
        if namaPeminjam == i.nama:
            limitPeminjam = i.limit
            if Pinjaman <= limitPeminjam:
                return True
            else:
                return False
            

def hitungAngsuranPerBulan(pinjaman, bunga, bulan):
    angsuranPokok = pinjaman * bunga/100 #PERSEN
    angsuranBulanan = angsuranPokok / bulan
    totalAngsuranPerBulan = angsuranPokok + angsuranBulanan
    return totalAngsuranPerBulan


            
def tambahPinjaman():
    namaP = input("Masukkan Nama Peminjam: ")
    namaAda = cekNama(namaP)
    if namaAda == True:
        while True:
            pinjamanBaruStr = input("Masukkan Nominal Pinjaman: ")
            cek = pinjamanBaruStr.isdigit()
            if cek == True:
                pinjamanBaru = int(pinjamanBaruStr)
                cekLimitnya = CekLimit(namaP, pinjamanBaru)
                if cekLimitnya == True:
                    while True:
                        sukubungastr = input("Masukan Suku Bunga: ")
                        limitwaktustr = input("Masukkan Limit Waktu (dalam bulan): ")
                        ceksuku = sukubungastr.isdigit()
                        cekwaktu = limitwaktustr.isdigit()
                        if ceksuku == True and cekwaktu == True:
                            sukubunga = int(sukubungastr)
                            limitWaktu = int(limitwaktustr)
                            # objekBaruPeminjam = ''
                            for i in nama:
                                if namaP == i.nama:
                                    # MEMBUAT FUNGSI MENGHITUNG ANGSURAN
                                    # pinjaman bunga bulan
                                    angsuranPerBulan = hitungAngsuranPerBulan(pinjamanBaru, sukubunga, limitWaktu)
                                    objekBaruPeminjam = Pinjaman(i.nama, i.KTP, i.limit, pinjamanBaru, sukubunga, limitWaktu, angsuranPerBulan)
                                    listpinjaman.append(objekBaruPeminjam)
                                    return True
                        else:
                            print("Masukan Harus Berupa Angka")
                else:
                    print("PINJAMAN MELEBIHI LIMIT / VALIDASI GAGAL")
                    return True
            else:
                print("NOMINAL PINJAMAN HARUS BERUPA ANGKA")
    else:
        print("Nama Tidak Ada / Validasi Nama Gagal")
        return True



def tampilkanPinjaman():
    for i in listpinjaman:
        # print(f"PEMINJAM KE- {i+1}")
        print(f"Nama Debitur: {i.nama}")
        print(f"Pinjaman: {i.pinjaman}")
        print(f"Bunga: {i.bunga}")
        print(f"Limit Waktu (bulan): {i.bulan}")
        print(f"Angsuran per Bulan: {i.angsuran}\n")

def menuutama():
    while True:
        tampilUtama()
        pilih = input("Masukkan Pilihan Menu Anda: ")
        if pilih == "1":
            SubMenuKelolaDebitur()
        elif pilih == "2":
            submenuKelolaPinjaman()
        elif pilih == "0":
            print("ANDA KELUAR PROGRAM")
            return True
        else:
            print("Inputan Anda Salah")

def SubMenuKelolaDebitur():
    while True:
        tampilMenuKelolaDebitur()
        pilih = input("Masukkan Pilihan Menu: ")
        if pilih == "1":
            tampilDebitur()
        elif pilih == "2":
            caridebiturBerdasarkanNama()
        elif pilih == "3":
            TambahDebiturBerdasarkanKTP()
        elif pilih == "0":
            print("KEMBALI KE MENU UTAMA\n")
            return True
        else:
            print("INPUTAN ANDA SALAH")

def submenuKelolaPinjaman():
    while True:
        tampilKelolaPinjaman()
        pilih = input("Masukkan pilihan menu: ")
        if pilih == "1":
            tambahPinjaman()
        elif pilih == "2":
            tampilkanPinjaman()
        elif pilih == "0":
            print("KEMBALI KE MENU UTAMA\n")
            return True
        else: 
            print("INPUTAN ANDA SALAH")


def tambahPinjamanVerManual(namabaru,pinjaman, bunga, bulan):
    objekBaruPeminjam = ""
    for i in nama:
        if namabaru == i.nama:
            angsuranPerBulan = hitungAngsuranPerBulan(pinjaman, bunga, bulan)
            objekBaruPeminjam = Pinjaman(i.nama, i.KTP, i.limit, pinjaman, bunga, bulan,angsuranPerBulan)
            listpinjaman.append(objekBaruPeminjam)
            return True


# MANUAL ATAU DEFAULT ISI
Irfan = Debitur("Irfan", 5230411327, 70000000)
# IrfanPinjam = Pinjaman("Irfan", 5230411327, 70000000, 50000000, 10, 24, )
nama.append(Irfan)
tambahPinjamanVerManual("Irfan", 5000000, 10, 12)

Asep = Debitur("Asep", 3401, 20000000)
nama.append(Asep)
tambahPinjamanVerManual("Asep", 5000000, 10, 12)


menuutama()






        






