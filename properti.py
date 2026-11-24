class Properti:
    def __init__(self, id_properti, alamat, harga_sewa):
        self.__id_properti = id_properti
        self.__alamat = alamat
        self.__harga_sewa = harga_sewa

    def get_id_properti(self):
        return self.__id_properti

    def get_alamat(self):
        return self.__alamat

    def get_harga_sewa(self):
        return self.__harga_sewa

    def ubah_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga_sewa = harga_baru
            return True
        return False

    def tampilkan_info(self):
        print("ID Properti :", self.get_id_properti())
        print("Alamat      :", self.get_alamat())
        print("Harga Sewa  :", self.get_harga_sewa())
