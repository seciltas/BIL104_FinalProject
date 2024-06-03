class Hemsire:
    def __init__(self,calisma_saati,sertifika,hastane):
        self.__calisma_saati=calisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane
        
    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def set_calisma_saati(self,calisma_saati):
        self.__calisma_saati=calisma_saati

    def get_sertifika(self):
        return self.__sertifika
    
    def set_sertifika(self,sertifika):
        self.__sertifika=sertifika

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self,hastane):
        self.__hastane=hastane

    #__str__ metodu içerisinde hemşire bilgileri yazılması

    def __str__(self):
        return f"Hemşire Bilgileri:\n Calisma Saati:{self.get_calisma_saati} Sertifika:{self.get_sertifika} Hastane:{self.set_hastane}"
    
    def maas_arttir(self):
        pass