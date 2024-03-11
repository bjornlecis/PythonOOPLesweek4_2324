class Medewerker:

    def __init__(self,id,voornaam,achternaam,woonplaats,geslacht,functie,loon):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.woonplaats = woonplaats
        self.geslacht = geslacht
        self.functie = functie
        self.loon = loon

m1 = Medewerker(1,"Jan","Jansen","Bilzen","M","CEO",7000)
m2 = Medewerker(2,"Piet","Pieters","Genk","M","CTO",6000)
m3 = Medewerker(3,"Linda","Leenders","Genk","V","CFO",6000)
m4 = Medewerker(4,"Sofie","Schrooten","Oudsbergen","V","HR Manager",5500)
m5 = Medewerker(5,"Mark","Mertens","Hasselt","M","Sales Manager",5000)

medewerkers = [m1,m2,m3,m4,m5]


