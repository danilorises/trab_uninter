class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.numero_amarelo = 1
        self.numero_verde = 201

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
        if cor == 'A':
            numero = self.numero_amarelo
            self.numero_amarelo += 1
        elif cor == 'V':
            numero = self.numero_verde
            self.numero_verde += 1
        else:
            print("Cor inválida!")
            return

        nodo = Nodo(numero, cor)
        if not self.head:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        else:
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão {atual.cor} número {atual.numero}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
            return
        paciente = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente com cartão {paciente.cor} número {paciente.numero}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                break
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.menu()