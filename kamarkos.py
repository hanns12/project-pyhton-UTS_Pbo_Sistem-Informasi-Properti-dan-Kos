from properti import Properti

class KamarKos(Properti):
    def __init__(self, id_properti, alamat, harga_sewa, nomor_kamar, fasilitas, status):
        super().__init__(id_properti, alamat, harga_sewa)
        self.__nomor_kamar = nomor_kamar
        self.__fasilitas = fasilitas
        self.__status = status

    def get_nomor_kamar(self):
        return self.__nomor_kamar

    def get_fasilitas(self):
        return self.__fasilitas

    def get_status(self):
        return self.__status

    def ubah_status(self, status_baru):
        if status_baru in ["Tersedia", "Terisi"]:
            self.__status = status_baru
            return True
        return False

    def tampilkan_info(self):
        print("\n--- INFORMASI KAMAR KOS ---")
        super().tampilkan_info()
        print("Nomor Kamar :", self.get_nomor_kamar())
        print("Fasilitas   :", self.get_fasilitas())
        print("Status      :", self.get_status())
