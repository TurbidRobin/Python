

class Animal:
    noise = "Rrrr"
    color = "red"
    def make_noise(self):
         print(f"{self.noise}")
#noise the animal makes
    def get_noise(self):
        return self.noise
    def set_noise(self, new_noise):
        self.noise = new_noise
#color of the animal
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color
        
class Wolf(Animal):
    noise = "grrr"
    color = "grey"

class BabyWolf(Wolf):
    color = "yellow"