#CLASSE


class Carro:
    #modelo empresa ano
    def __str__(self):
        return(self.modelo + " " + self.empresa + " " + str(self.ano))

    def __init__(self, modelo, empresa, ano):
        self.modelo = modelo 
        self.empresa = empresa
        self.ano = ano 

    def mudar_ano(self, ano_novo):
        self.ano = ano_novo    

carro = Carro("Focus", "Ford", 2006)
print(carro.ano)

carro.mudar_ano(2001)
print(carro.ano)

class Dono:
    def __init__(self, nome, carro):
        self.nome = nome
        self.carro = carro 

dono1 = Dono("Marcelo", carro)
print(dono1.carro)

#FUNÇÃO
'''
def somar(x, y):
    return(x+y)

x = 5
y = 6

print(somar(x,y))

'''


