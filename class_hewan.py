class hewan:
    def __init__ (self, suara, habitat, nama):
        self.suara = suara
        self.habitat = habitat
        self.nama = nama

    def h(self):
        print(self.nama + " mempunyai suara " + self.suara + " dan berhabitat di " + self.habitat)

animal = hewan(suara="besar", habitat="hutan", nama="singa")
print(animal.h())