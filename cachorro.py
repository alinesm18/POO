class Cachorro:

    def __init__(self,nome,raca,comida):
     self.nome = nome 
     self.raca = raca
     self.comida = comida
     self.acordado = True
     self.feliz = False

    def __str__(self):
       return f"Nome:{self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"

    def comer (self):
     if self.comida>0:
        self.comida-=1
        self.feliz = True
        return f"{self.nome} comeu e agora está feliz!"
     else: return f"{self.nome} está sem comida!"
    
    def dormir (self):
      self.acordado = False
      return f"{self.nome} está dormindo."
      
    def acordar (self):
      self.acordado = True
      return f"{self.nome} está acordado!"
    
    def brincar (self):
      if self.acordado is True:
        self.feliz
        return f"{self.nome} está feliz e brincando!"
      else: return f"{self.nome} não pode brincar, está dormindo."
    
    def ignorar (self):
      self.feliz = False
      return f"{self.nome} está triste porque foi ignorado. :("
    
    def latir (self):
      if self.acordado:
        return f"{self.nome} está latindo: au au!"
      else: return f"{self.nome} está dormindo e não pode latir."
    
# Criando os cachorros:
bob = Cachorro ("Bob","Labrador",3)
lua = Cachorro ("Lua","Shitzu", 2)

# Interagindo com os cachorros:
print (bob.comer ())
print (lua.dormir ())
print (bob.brincar ())
print (bob.ignorar ())
print (lua.latir ())
print (bob)
print (lua)