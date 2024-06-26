from Personel import Personel

class Hemsire(Personel):

    #Initializer metod yazıldı
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    #Get/Set metotları yazıldı
    def get_calisma_saati(self):
        return self.__calisma_saati

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (1 + oran / 100)
        self.set_maas(yeni_maas)

    #__str__ metodu içinde hemşire bilgileri yazdırıldı
    def __str__(self):
        return "Hemsire Bilgileri\n"+ super().__str__() + f"Çalışma Saati: {self.get_calisma_saati()}, Sertifika: {self.get_sertifika()}, Hastane: {self.get_hastane()}"