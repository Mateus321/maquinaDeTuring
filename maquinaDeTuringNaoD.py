class MaquinaTuringNaoDeterministica:
    def _init_(self, nome_arquivo):
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

        formatted_transicoes = []
        for transicao in transicoes:
            estado_atual, entrada_escrita, proximo_estado, movimento = transicao
            entrada, escrita = entrada_escrita.split(';')
            formatted_transicoes.append([estado_atual, entrada, escrita, proximo_estado, movimento])

        transicoes = formatted_transicoes
        return estados, alfabeto, marcadores, naoFinais, finais, inicial, formatted_transicoes

    def iniciar(self, fita):
        self.fita = fita
        estado_atual = self.inicial
        posicao_cabecote = 0

        # Create a stack to manage branches of computation
        stack = [(estado_atual, posicao_cabecote, self.fita)]

        while stack:
            estado_atual, posicao_cabecote, fita = stack.pop()

            if estado_atual in self.finais:
                # If a branch reaches a final state, the input is accepted
                return fita

            simbolo_atual = fita[posicao_cabecote]

            for transicao in self.transicoes:
                if int(transicao[0]) == int(estado_atual) and transicao[1] == simbolo_atual:
                    print('-----------')
                    proximo_estado = transicao[2]
                    proximo_simbolo = transicao[3]
                    direcao = transicao[4]

                    # Clone the current configuration and update it with the transition
                    nova_fita = fita[:posicao_cabecote] + proximo_simbolo + fita[posicao_cabecote + 1:]
                    nova_posicao = posicao_cabecote + 1 if direcao == 'R' else posicao_cabecote - 1

                    # Push the new configuration onto the stack
                    stack.append((proximo_estado, nova_posicao, nova_fita))
            
            print(estado_atual + ": " + self.fita)
            
        return "A Máquina de Turing não aceita a entrada."

# Exemplo de uso:
nome_arquivo = 'MT-nao-deterministica.txt'
maquina_turing = MaquinaTuringNaoDeterministica(nome_arquivo)
fita = input("Digite a palavra contendo o alfabeto " + ', '.join(maquina_turing.alfabeto) + ": ")
resultado = maquina_turing.iniciar(fita + '_')
print("Resultado da Máquina de Turing:", resultado)