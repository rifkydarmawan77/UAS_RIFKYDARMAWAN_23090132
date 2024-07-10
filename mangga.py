from buah import Buah

class Mangga(Buah):
    def _init_(self, nama, jenis):
        super()._init_(nama)
        self.jenis = jenis
    
    def deskripsi(self):
        return f"Mangga: {self.nama}, Jenis: {self.jenis}"
    