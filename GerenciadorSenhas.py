import random
import string
import os

class Pessoa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade
        self.senha = self.gerarSenhaUnica(prioridade)

    def gerarSenhaUnica(self, prioridade):
        while True:
            letra_prioridade = "P" if prioridade == "S" else "N"
            algarismos = ''.join(random.choices(string.digits, k=4))
            senha = letra_prioridade + algarismos
            return senha

class FilaDeEspera:
    def __init__(self):
        self.fila = []
    
    def adicionarPessoa(self, pessoa):
        ultimaPrioridade = None
        finalFila = len(self.fila)
        if pessoa.prioridade == "S":         
            for i in range(finalFila - 1, -1, -1):
                    #Acha a última pessoa com prioridade na fila               
                        if self.fila[i].prioridade == "S" and ultimaPrioridade == None:
                            ultimaPrioridade = i
                            #Se a pessoa anterior a última prioridade não tiver prioridade, a pessoa é inserida logo após a última pessoa com prioridade               
                            if self.fila[ultimaPrioridade -1].prioridade != "S":
                                self.fila.insert(ultimaPrioridade + 1, pessoa)
                            else:
                                #Se a última pessoa com prioridade tiver pelo menos 2 pessoas após ela, a pessoa é inserida 3 posições após a última pessoa com prioridade
                                if finalFila - ultimaPrioridade >= 3:
                                    self.fila.insert(ultimaPrioridade + 3, pessoa)                   
                                else:
                                    self.fila.append(pessoa)
            if ultimaPrioridade == None:
                self.fila.insert(0,pessoa)
        else:
            self.fila.append(pessoa)
    
    def removerPessoa(self):
        if len(self.fila) == 0:
            print("A fila está vazia.")
            return None
        else:
            return self.fila.pop(0)
    
    def mostrarFila(self):
        print("************** Fila de espera: **************\n")
        for pessoa in self.fila:
            print(f'Nome: {pessoa.nome} - Senha: {pessoa.senha}')


class Menu:
    def __init__(self):
        self.menu = {
            1: "Adicionar pessoa",
            2: "Registrar atendimento",
            3: "Sair"
        }

    def mostrarMenu(self):
        print("\n\n************** Menu **************\n")
        for key, value in self.menu.items():
            print(f'{key} - {value}')
    
    def escolherOpcao(self):
            opcao = int(input("Escolha uma opção: "))
            return opcao

    def limparconsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def executarOpcao(self, opcao):
        if opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            prioridade = input("A pessoa tem prioridade? (S/N): ").upper()
            pessoa = Pessoa(nome, prioridade)
            fila_espera.adicionarPessoa(pessoa)
            fila_espera.mostrarFila()
        elif opcao == 2:
            fila_espera.removerPessoa()
            fila_espera.mostrarFila()
        elif opcao == 3:
            print("Saindo...")
            return False
        return True

    


if __name__ == "__main__":
    fila_espera = FilaDeEspera()
    menu = Menu()
    while True:
        menu.limparconsole()
        fila_espera.mostrarFila()
        menu.mostrarMenu()
        opcao = menu.escolherOpcao()
        continuar = menu.executarOpcao(opcao)
        if not continuar:
            break


