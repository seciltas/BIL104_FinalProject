from Personel import Personel

class Doktor(Personel):

    #Initializer metod yazıldı
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    #Get/Set metotları yazıldı
    def get_uzmanlik(self):
        return self.__uzmanlik

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self,oran):
        yeni_maas = self.get_maas() * (1 + oran / 100)
        self.set_maas(yeni_maas)

    #__str__ metodu içinde doktor bilgileri yazdırıldı
    def __str__(self):
        return "Doktor Bilgileri\n" + super().__str__() + f"Uzmanlık: {self.get_uzmanlik()}, Deneyim Yılı: {self.get_deneyim_yili()}, Hastane: {self.get_hastane()}"