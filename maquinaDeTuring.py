with open('MT-deterministica.txt', 'r') as deterministico:
    automato = deterministico.readlines()


def tirar_virgula(texto):
    virgula = ","
    for rem in texto:
        if rem in virgula:
            texto = texto.replace(rem, '')
    
    return texto

estados = automato[0]
estados = tirar_virgula(estados)

alfabeto = automato[1]
alfabeto = tirar_virgula(alfabeto)

marcadores = automato[2]
marcadores = tirar_virgula(marcadores)


naoFinais = automato[len(automato) -1 ]
naoFinais = tirar_virgula(naoFinais)

finais = automato[len(automato) -2]
finais = tirar_virgula(finais)

inicial = automato[len(automato) -3]
inicial = tirar_virgula(inicial)

transicoes = automato[3: (len(automato) - 3)]

transicoes = [palavra.replace("\n", "") for palavra in transicoes]

trans = []

for linha in transicoes:
    transicoes = tirar_virgula(linha)
    trans.append(transicoes)
transicoes = trans


