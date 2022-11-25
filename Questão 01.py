import random

class structure:

    def __init__(self):
        self.__structure = []

#Adiciona o valor (value) ao final da pilha 
    def push(self, value):       
        self.__structure.append(value)

#Remove o último valor da pilha
    def pop(self):
        return self.__structure.pop()
    
#imprime a pilha
    def show(self):
        print("Imprimir Ordem ")
        print(f'structure: {self.__structure}\n')
        
#imprimir de trás para frente pilha
    def tras(self):
        print("Imprimir ordem Invera")
        print(f'structure: {self.__structure[::-1]}\n')
        
def main():
    
    #Cria uma pilha e utiliza os métodos show, pop e push
    estrutura = structure()

    for _ in range(0, 10):
        estrutura.push(random.randint(10, 99))
    
    #Imprimir os valoress randomicos
    estrutura.show()
    
    #Teste para remover valor
    estrutura.pop()
    estrutura.pop()
    
    #imprimir os valores Ordem Inversa
    estrutura.tras()

if __name__ == '__main__':
    main()