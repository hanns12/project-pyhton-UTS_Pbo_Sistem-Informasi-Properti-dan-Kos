from properti import Properti

class Kontrakan(Properti):
    def __init__(self, id_properti, alamat, harga_sewa, jumlah_kamar, luas_bangunan, status):
        super().__init__(id_properti, alamat, harga_sewa)
        self.__jumlah_kamar = jumlah_kamar
        self.__luas_bangunan = luas_bangunan
        self.__status = status

    def get_jumlah_kamar(self):
        return self.__jumlah_kamar

    def get_luas_bangunan(self):
        return self.__luas_bangunan

    def get_status(self):
        return self.__status

    def ubah_status(self, status_baru):
        if status_baru in ["Tersedia", "Terisi"]:
            self.__status = status_baru
            return True
        return False
    def tampilkan_info(self):
        print("\n--- INFORMASI KONTRAKAN ---")
        super().tampilkan_info()
        print("Jumlah Kamar :", self.get_jumlah_kamar())
        print("Luas Bangunan:", self.get_luas_bangunan(), "m2")
        print("Status       :", self.get_status())