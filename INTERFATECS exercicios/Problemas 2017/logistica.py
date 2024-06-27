# 1 4 2 4 3 1 2 4 2 1 1 4 2 3
# 10
# 5
# 2
# containers > 8 metros
class Gerenciar:
    id = 1
    gerenciar = [ []
       
    ]

    def __init__(self,tamanho):
        self.id = Gerenciar.id
        self.tamanho = int(tamanho)
        Gerenciar.alocar(self)
        Gerenciar.id +=1
    def __repr__(self):
        return f"Isso é meu pallet> id={self.id}//com tamanho de {self.tamanho}\n"   
    def alocar(self):
        for container in Gerenciar.gerenciar: 
           
            if Gerenciar.somar(container) == 8:
                
                pass
            elif self.tamanho + Gerenciar.somar(container) < 8:
                container.append(self)
                break
            elif self.tamanho + Gerenciar.somar(container) == 8:
                container.append(self)
                if Gerenciar.gerenciar.index(container) == len(Gerenciar.gerenciar) - 1: 
                    Gerenciar.gerenciar.append([])
            
                break
            elif self.tamanho + Gerenciar.somar(container) > 8:
                if Gerenciar.gerenciar.index(container) == len(Gerenciar.gerenciar) - 1:
                    novocontainer = []
                    novocontainer.append(self)
                    Gerenciar.gerenciar.append(novocontainer) 
                    break
                else:
                    pass
    """
Método somar: Mudado para @staticmethod já que não depende de instâncias ou atributos da classe.
Método exibirsoma: Mudado para @classmethod já que opera sobre a classe Gerenciar.
Métodos topo e retirar: Mudados para @staticmethod já que operam de forma independente da classe ou instância.
Método identificar: Mudado para @classmethod já que opera sobre a classe Gerenciar.
"""
    @staticmethod
    def somar(container:list):
        retorno = 0
        for pallet in container:
            retorno += pallet.tamanho
        
        return retorno
    @classmethod
    def exibirsoma(cls):
        for container in cls.gerenciar:
            print(cls.somar(container))
    @staticmethod
    def topo(lista:list,self):
        if lista.index(self) == len(lista)-1:
            return True
        else:
            return False
    @staticmethod    
    def retirar(container:list,self):
        retirar = []
        for pallet in container:
            retirar.insert(0,pallet.id)
            if pallet == self:
                retirar = []
        minhastring = ""
        for ids in retirar:
            minhastring += str(ids) + " "
        minhastring.strip()
        return minhastring
    @classmethod
    def identificar(cls,id):
        for container in cls.gerenciar:
            for pallet in container:
                if pallet.id == id:
                    if cls.topo(container,pallet) == True:
                        print(f"Pallet {pallet.id} Container {cls.gerenciar.index(container)+1} TOPO")
                    else:
                        print(f"Pallet {pallet.id} Container {cls.gerenciar.index(container)+1} Retirar",cls.retirar(container,pallet))


    # def __add__(self,another): #nao vou usar, só p lembrar de verificar dps
    #     self.tamanho + another.tamanho
    # def __str__(self):#essa eu to com bastante duvida p ver diferenca entre __repr__ e __str__
    #     pass
   
def main():
    pallets = input().split(' ')
    for pallet in pallets:
        Gerenciar(pallet)
    entrada_usuario = int()
    while True:
        entrada_usuario=int(input())
        if entrada_usuario == 0:
            break
        Gerenciar.identificar(entrada_usuario)

main()
