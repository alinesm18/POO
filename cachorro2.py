class Cachorro:

    def __init__(self,nome,raca,comida):
     self.nome = nome 
     self.raca = raca
     self.comida = comida
     self.energia = 100
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
      if not self.acordado:
        return f"{self.nome} está dormindo e não pode brincar agora."
      if self.energia > 20:
        self.energia -= 20
        self.feliz = True
        return f"{self.nome} está feliz e brincando! Eenergia atual:{self.energia}."
      return f"{self.nome} está cansado e não pode brincar, precisa dormir."
     
    
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
print (bob.brincar ())
print (bob.brincar ())
print (lua.brincar ())
print (lua.acordar ())
print (lua.ignorar ())
print (bob.latir ())
print (bob)
print (lua)

# Fazendo Bob dormir para restaurar energia e brincar:
print (bob.brincar ())
print (bob.brincar ())
print (bob.dormir ())
print (bob.acordar ())
print (bob.brincar)