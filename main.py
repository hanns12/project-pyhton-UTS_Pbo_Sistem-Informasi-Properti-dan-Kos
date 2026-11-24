from properti import Properti
from kamarkos import KamarKos
from kontrakan import Kontrakan
from penyewa import Penyewa

daftar_properti = []
daftar_penyewa = []


# Method untuk mencari properti berdasarkan ID
def cari_properti(id_properti):
    for properti in daftar_properti:
        if properti.get_id_properti() == id_properti:
            return properti
    return None


# 1. Method untuk menambahkan properti
def tambah_properti():
    print("       TAMBAH PROPERTI    ")
    print("1. Kamar Kos")
    print("2. Kontrakan")

    pilihan = input("Pilih jenis properti: ")

    if pilihan != "1" and pilihan != "2":
        print("Pilihan tidak tersedia!")
        return

    id_properti = input("ID Properti: ")

    if cari_properti(id_properti) is not None:
        print("ID properti sudah digunakan!")
        return

    alamat = input("Alamat: ")

    try:
        harga = int(input("Harga Sewa: "))

        if harga <= 0:
            print("Harga harus lebih dari 0!")
            return

        if pilihan == "1":
            nomor = input("Nomor Kamar: ")
            fasilitas = input("Fasilitas: ")

            properti = KamarKos(
                id_properti, alamat, harga,
                nomor, fasilitas, "Tersedia"
            )

        else:
            jumlah = int(input("Jumlah Kamar: "))
            luas = float(input("Luas Bangunan (m2): "))

            if jumlah <= 0 or luas <= 0:
                print("Jumlah kamar dan luas harus lebih dari 0!")
                return

            properti = Kontrakan(
                id_properti, alamat, harga,
                jumlah, luas, "Tersedia"
            )

        daftar_properti.append(properti)
        print("Data properti berhasil ditambahkan!")

    except ValueError:
        print("Input harus berupa angka yang valid!")


# 2. Method untuk menampilkan semua properti
def tampilkan_properti():
    print("      DAFTAR PROPERTI    ")

    if len(daftar_properti) == 0:
        print("Belum ada data properti.")
    else:
        for properti in daftar_properti:
            properti.tampilkan_info()
            print()


# 3. Method untuk mencari properti
def menu_cari_properti():
    print("      CARI PROPERTI    ")
    id_properti = input("Masukkan ID Properti: ")

    properti = cari_properti(id_properti)

    if properti is not None:
        print("Data properti ditemukan!")
        properti.tampilkan_info()
    else:
        print("Data properti tidak ditemukan!")


# 4. Method untuk mengubah harga properti
def ubah_properti():
    print("      UBAH HARGA PROPERTI    ")
    id_properti = input("Masukkan ID Properti: ")

    properti = cari_properti(id_properti)

    if properti is not None:
        try:
            harga_baru = int(input("Masukkan harga sewa baru: "))

            if harga_baru <= 0:
                print("Harga harus lebih dari 0!")
                return

            if properti.ubah_harga(harga_baru):
                print("Harga berhasil diubah!")
                properti.tampilkan_info()
            else:
                print("Harga tidak valid!")

        except ValueError:
            print("Harga harus berupa angka!")

    else:
        print("Data properti tidak ditemukan!")


# 5. Method untuk mengecek status properti
def cek_status():
    print("      CEK STATUS PROPERTI    ")
    id_properti = input("Masukkan ID Properti: ")

    properti = cari_properti(id_properti)

    if properti is not None:
        if isinstance(properti, KamarKos):
            print("Status Kamar:", properti.get_status())

        elif isinstance(properti, Kontrakan):
            print("Status Kontrakan:", properti.get_status())

    else:
        print("Data properti tidak ditemukan!")


# 6. Method untuk menambahkan penyewa
def tambah_penyewa():
    print("     TAMBAH PENYEWA    ")
    id_properti = input("Masukkan ID Kamar Kos: ")

    properti = cari_properti(id_properti)

    if isinstance(properti, KamarKos):

        if properti.get_status() == "Tersedia":

            id_penyewa = input("ID Penyewa: ")

            # Memeriksa ID penyewa
            for penyewa in daftar_penyewa:
                if penyewa.get_id_penyewa() == id_penyewa:
                    print("ID penyewa sudah digunakan!")
                    return

            nama = input("Nama Penyewa: ")

            penyewa = Penyewa(id_penyewa, nama, properti)
            daftar_penyewa.append(penyewa)

            properti.ubah_status("Terisi")

            print("Data penyewa berhasil ditambahkan!")

        else:
            print("Kamar sudah terisi!")

    else:
        print("Kamar kos tidak ditemukan!")


# 7. Method untuk menampilkan penyewa
def tampilkan_penyewa():
    print("      DAFTAR PENYEWA    ")

    if len(daftar_penyewa) == 0:
        print("Belum ada data penyewa.")
    else:
        for penyewa in daftar_penyewa:
            penyewa.tampilkan_info()
            print()


# PROGRAM UTAMA
while True:
    print("     SISTEM PROPERTI DAN KOS")
    print("1. Tambah Properti")
    print("2. Tampilkan Properti")
    print("3. Cari Properti")
    print("4. Ubah Harga Properti")
    print("5. Cek Status Properti")
    print("6. Tambah Penyewa")
    print("7. Tampilkan Penyewa")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_properti()

    elif pilihan == "2":
        tampilkan_properti()

    elif pilihan == "3":
        menu_cari_properti()

    elif pilihan == "4":
        ubah_properti()

    elif pilihan == "5":
        cek_status()

    elif pilihan == "6":
        tambah_penyewa()

    elif pilihan == "7":
        tampilkan_penyewa()

    elif pilihan == "0":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak tersedia! Silakan pilih kembali.")