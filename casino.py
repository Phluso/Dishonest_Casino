import random

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sorteio(aposta):
    '''
        recebe uma probabilidade e sorteia um número aleatório com base nela
        se o valor for maior que um valor proporcional à probabilidade, o retorno é positivo
    '''
    global nApostas
    global tValor
    global tVitoria
    sort = random.randint(0, 100)
    if (sort >= nApostas + (tValor / 5) * (tVitoria / 100 * aposta)):
        return True
    else:
        return False

def destaque(s):
    print("+", "-" * len(s), "+")
    print("|", s, "|")
    print("+", "-" * len(s), "+\n")

def clamp(n, min, max):
    if (n < min):
        n = min
    elif (n > max):
        n = max
    return n

menuInicial = ("Fazer aposta", "Instruções", "Sair")
banca       = 0     #saldo atual do jogador
tBanca      = 0     #valor total depositado
nApostas    = 0     #numero total de apostas
tValor      = 0     #valor total gasto no cassino
tVitoria    = 0     #sequencia de vitorias atual

#limpar o terminal antes de iniciar o programa
clear()

while True:
    try:
        destaque("Tela inicial")
        for i in range(len(menuInicial)):
            print(f"[{i}] {menuInicial[i]}")

        opt = int(input("\nInsira um número: "))
        
        if (opt > len(menuInicial) -1):
            print("Insira um número válido")
            continue
        
        print(f"Você selecionou: {menuInicial[opt]}\n")
        clear()
        if (opt == 0):
            destaque("Área de apostas")
            while True:     #enquanto estiver na sala
                while True: #enquanto não apostar dinheiro
                    try:
                        print(f"Saldo da banca = {banca}\n")
                        print("Digite '0' para cancelar e voltar")
                        valor = float(input("Insira um valor para apostar: "))
                        break
                    except:
                        print("Insira um número válido")
                        continue
                #sair
                if (valor == 0):
                    clear()
                    print("Voltando à tela inicial")
                    break
                #saldo insuficiente
                if (banca <= 0) or (valor > banca):
                    clear()
                    destaque("Saldo insuficiente")
                    print(f"Seu saldo é de: {banca}\n")
                    try:
                        print("Digite '0' para voltar, ou")
                        deposito = float(input("Faça um depósito para continuar jogando: "))
                        clear()
                        destaque(f"Depósito de {deposito} realizado com sucesso!")
                        if (deposito == 0):
                            break
                        #incrementar o valor da banca e o total gasto no cassino
                        banca += deposito
                        tValor += banca
                        #somar o valor total depositado no cassino
                        tBanca += banca
                    except:
                        print("Erro")
                    continue
                clear()
                #descontar valor da aposta do saldo da banca
                banca -= valor
                if (sorteio(valor)):
                    destaque(f"Você apostou {valor} e ganhou {valor * 2.5} B)")
                    #incrementar a sequencias de vitorias atual
                    tVitoria += 1
                    #somar o dobro do valor apostado no saldo da banca
                    banca += valor * 2.5
                else:
                    #resetar a sequencia de vitorias
                    tVitoria -= .5
                    destaque("Você perdeu D:")

                #incrementar o total de tentativas
                nApostas += 1

                #limitar o valor total apostado para não criar probabilidades impossíveis
                tValor = clamp(tValor, 0, 10000)

        elif (opt == 1):
            clear()
            print("Instruções:")
            continue

        elif (opt == 2):
            clear()
            print(f"Você gastou {tBanca - banca} no cassino! Muito obrigado :)")
            print("Saindo")
            break
    except:
        clear()
        print("Insira apenas números")
        continue