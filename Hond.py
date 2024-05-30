import datetime
x = datetime.datetime.now()
jaar = int(x.year)

class Hond:
    def __init__(self,naam,geboortejaar,leeftijd):
        self.naam = naam
        self.geboortejaar = geboortejaar
        self.leeftijd = leeftijd
    def __str__(self):
        return ("Deze hond heet {}, en hij is {} jaar oud en in {} geboren.".format(self.naam, self.leeftijd, self.geboortejaar))

    def blaf(self):
        print("{} zegt woef".format(self.naam))

loop = False
while not loop:
    try:
        honden = int(input("Hoeveel honden heeft u?: "))
        loop = True
    except ValueError as ve:
        print(ve)
for x in range(0,honden):
    try:
        naam = input("Hoe heet uw hond?: ")
        geboortejaar = int(input("In welk jaar is je hond geboren?: "))
        leeftijd = jaar-geboortejaar 
    except ValueError as ve:
        print(ve)
        hond1 = Hond(naam,geboortejaar,leeftijd)
        print(hond1)
        hond1.blaf()
