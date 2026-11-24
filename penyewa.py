class Penyewa:
    def __init__(self, id_penyewa, nama_penyewa, kamar_kos):
        self.__id_penyewa = id_penyewa
        self.__nama_penyewa = nama_penyewa
        self.__kamar_kos = kamar_kos

    def get_id_penyewa(self):
        return self.__id_penyewa

    def get_nama_penyewa(self):
        return self.__nama_penyewa

    def get_kamar_kos(self):
        return self.__kamar_kos

    def ubah_nama(self, nama_baru):
        if nama_baru != "":
            self.__nama_penyewa = nama_baru
            return True
        return False

    def tampilkan_info(self):
        print("\n--- INFORMASI PENYEWA ---")
        print("ID Penyewa   :", self.get_id_penyewa())
        print("Nama Penyewa :", self.get_nama_penyewa())
        print("Kamar        :", self.get_kamar_kos().get_nomor_kamar())
        print("Alamat Kos   :", self.get_kamar_kos().get_alamat())
