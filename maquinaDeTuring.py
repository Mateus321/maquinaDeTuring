class MaquinaTuringDeterministica:
    def __init__(self, nome_arquivo):
        self.estados, self.alfabeto, self.marcadores, self.naoFinais, self.finais, self.inicial, self.transicoes = self.ler_automato_de_arquivo(nome_arquivo)
        self.fita = ""

    def ler_automato_de_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as deterministico:
            automato = deterministico.readlines()

        def tirar_virgula(texto):
            virgula = ","
            for rem in texto:
                if rem in virgula:
                    texto = texto.replace(rem, '')
            return texto

        estados = automato[0]
        estados = tirar_virgula(estados).split()

        alfabeto = automato[1]
        alfabeto = tirar_virgula(alfabeto).split()

        marcadores = automato[2]
        marcadores = tirar_virgula(marcadores).split()

        naoFinais = automato[len(automato) - 1]
        naoFinais = tirar_virgula(naoFinais).split()

        finais = automato[len(automato) - 2]
        finais = tirar_virgula(finais).split()

        inicial = automato[len(automato) - 3]
        inicial = tirar_virgula(inicial)

        transicoes = automato[3: (len(automato) - 3)]
        transicoes = [linha.replace("\n", "").split(',') for linha in transicoes]

        return estados, alfabeto, marcadores, naoFinais, finais, inicial, transicoes

    def iniciar(self, fita):
        self.fita = fita
        estado_atual = self.inicial
        posicao_cabecote = 0

        while estado_atual not in self.finais:
            simbolo_atual = self.fita[posicao_cabecote]
            proximo_estado = None
            proximo_simbolo = None
            direcao = None

            for transicao in self.transicoes:
                if transicao[0] == estado_atual and transicao[1] == simbolo_atual:
                    proximo_estado = transicao[2]
                    proximo_simbolo = transicao[3]
                    direcao = transicao[4]
                    break

            if proximo_estado is None:
                print("A máquina de Turing parou - transição indefinida.")
                break

            self.fita = self.fita[:posicao_cabecote] + proximo_simbolo + self.fita[posicao_cabecote + 1:]

            if direcao == "D":
                posicao_cabecote += 1
            elif direcao == "E":
                posicao_cabecote -= 1

            estado_atual = proximo_estado

        return self.fita

# Exemplo de uso:
nome_arquivo = 'MT-deterministica.txt'
maquina_turing = MaquinaTuringDeterministica(nome_arquivo)
fita = input("Digite a palavra contendo o alfabeto " + ', '.join(maquina_turing.alfabeto) + ": ")
resultado = maquina_turing.iniciar(fita)
print("Resultado da Máquina de Turing:", resultado)
