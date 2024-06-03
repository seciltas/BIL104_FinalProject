class Doktor:
    def __init__(self,uzmanlik,deneyim_yili,hastane):
        self.__uzmanlik=uzmanlik
        self.__deneyim_yili=deneyim_yili
        self.__hastane=hastane



    def get_uzmanlik(self):
        return self.__uzmanlik
    

    def set_uzmanlik(self,uzmanlik):
        self.__uzmanlik= uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili
    
    def set_deneyim_yili(self,deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_hastane(self):
        return self.__hastane
    
    def set_hastane(self,hastane):
        self.__hastane= hastane

    #__str__ metodu içerisinde doktor bilgileri yazılması
    def __str__(self):
        return f"Doktor Bilgileri:\n Uzmanlik Alani:{self.get_uzmanlik} Deneyim Yili:{self.get_deneyim_yili} Hastane:{self.set_hastane}"
    
    def maas_arttir(self):
        pass