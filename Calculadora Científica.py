import math
import os
from decimal import Decimal

# Mensagens de erro:
divisao_zero = "Erro! A divisão por zero é impossível."                                            # Erro quando o usuário tenta fazer divisões por zero.
raiz_neg = "Erro! Não é possível calcular raiz de números negativos."                              # Erro quando o usuário tenta calcular a raiz quadrada de números negativos.
arcosen_inv = "Erro! O arco-seno só é definido para valores entre -1 e 1."                         # Erro quando o usuário digita qualquer número que não esteja entre -1 e 1, incluindo os próprios.
arcocosen_inv = "Erro! O arco-cosseno só é definido para valores entre -1 e 1."                    # Erro quando o usuário digita qualquer número que não esteja entre -1 e 1, incluindo os próprios.
valor_inv = "Erro! O valor precisa ser 1 ou maior para realizar o cálculo."                        # Erro colocando qualquer número abaixo de 1 para calcular.
arco_inv = "Erro! O arco-tangente hiperbólica só é definido para valores entre -1 e 1."            # Erro quando o usuário digita qualquer número que não esteja entre -1 e 1, incluindo os próprios.
fator_neg = "Erro! O fatorial não é definido para números negativos."                              # Erro na fatoração de números negativos.
log_neg = "Erro! Não é possível calcular o logaritmo de números negativos."                        # Erro no cálculo de logaritmo de números negativos (tanto os de base 10, quanto os de base 2).

# Códigos ANSI para formatação:
bold = '\033[1m'                                                                                   # Colocar o texto em negrito.
reset = '\033[0m'                                                                                  # Resetar o negrito.
sub = '\033[4m'                                                                                    # Sublinhar os textos.

#Códigos ANSI para cores:
azul = '\033[34m'                                                                                  # Colorir os elementos em azul.
vermelho = '\033[31m'                                                                              # Colorir os elementos em vermelho.
verde = '\033[32m'                                                                                 # Colorir os elementos em verde.
amarelo = '\033[33m'                                                                               # Colorir os elementos em amarelo.
azulc = '\033[36m'                                                                                 # Colorir os elementos em azul claro.
verdec = '\033[92m'                                                                                # Colorir os elementos em verde claro.
vermelhoc = '\033[91m'                                                                             # Colorir os elementos em vermelho claro.

def limpeza():
    if os.name == 'nt':                                                                            # Verifica o sistema operacional.
        os.system('cls')                                                                           # Se for Windows, utiliza o cls para limpar o terminal.
    else:
        os.system('clear')                                                                         # Se for qualquer outro sistema operacional, utiliza o clear.
    
def Soma(x, y):
    return x + y

def Subtração(x, y):
    return x - y

def Multiplicação(x, y):
    return x * y

def Divisão(x, y):
    if x == 0:
        return divisao_zero
    elif y == 0:
        return divisao_zero
    else:
        return x / y

def Potenciação(x, y):
    return x ** y

def Módulo(x, y):
    return x % y

def Porcentagem(x, y):
    return (x / y) * 100

def Raiz(x):
    if x < 0:
        return raiz_neg
    else:
        return math.sqrt(x)

def Seno(x):
    return math.sin(x)

def Cosseno(x):
    return math.cos(x)

def Tangente(x):
    return math.tan(x)

def Arcoseno(x):
    if -1 <= x <= 1:
        return math.asin(x)
    else:
        raise ValueError(arcosen_inv)

def Arcocosseno(x):
    if -1 <= x <= 1:
        return math.acos(x)
    else:
        raise ValueError(arcocosen_inv)

def Arcotangente(x):
    return math.atan(x)

def Arcotangente2(y, x):
    return math.atan2(y, x)

def Seno_hip(x):
    return math.sinh(x)

def Cosseno_hip(x):
    return math.cosh(x)

def Tangente_hip(x):
    return math.tanh(x)

def Arcoseno_hip(x):
    return math.asinh(x)

def Arcocosseno_hip(x):
	if x < 1:
		return (valor_inv)
	else:
		return math.acosh(x)

def Arcotan_hip(x):
    if x <= -1 or x >= 1:
        return arco_inv
    else:
        return math.atanh(x)

def Radiano(x):
    return math.radians(x)

def Fatorial(x):
    if x < 0:
        return fator_neg
    else:
        return math.factorial(x)

def Valor_Absoluto(x):
    return math.fabs(x)

def Logaritmo10(x):
    if x < 0:
        return log_neg
    else:
        return math.log10(x)

def Logaritmo2(x):
    if x < 0:
        return log_neg
    else:
        return math.log2(x)

def Equação2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não tem raízes reais."                                                             # Se a operação não tiver nenhuma raiz real, o usuário recebe essa mensagem.
    elif delta == 0:
        x = -b / (2*a)
        return f"A única raiz real é {x}."                                                         # Se a operação tiver apenas uma raiz real, o usuário vai ter essa mensagem exibida.
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes reais são {x1} e {x2}."                                                 # Se não for nenhuma das opções acima, e tiver duas raízes reais, o usuário recebe essa mensagem.

def Exponencial(x):
    return math.exp(x)

def Média_Aritmética(a, b, c, d):
    numero = [a, b, c, d]
    somanumero = sum(numero)
    quantidade = len(numero)
    aritmetica = somanumero / quantidade
    return aritmetica


def retomar():
    while True:
        resposta = input("Presione Enter para continuar...")                                       # Função que retoma o código se o usuário apertar a tecla Enter.
        print()
        if resposta == "":
            return True
        
while True:
    limpeza()                                                                                      # Limpa o terminal a partir do Menu de Operações.
    print()
    print("----------------------------------------------------")
    print(f"{bold}{"Menu de Operações".center(53)}{reset}")
    print("----------------------------------------------------")
    print()
    print(f"{bold}{sub}{verdec}{"Funções Matemáticas Básicas"}{reset}")
    print()
    print(f"{bold}{'1.':<3}{reset} Soma {bold}(+){reset}")
    print(f"{bold}{'2.':<3}{reset} Subtração {bold}(-){reset}")
    print(f"{bold}{'3.':<3}{reset} Multiplicação {bold}(x){reset}")
    print(f"{bold}{'4.':<3}{reset} Divisão {bold}(÷){reset}")
    print(f"{bold}{'5.':<3}{reset} Potência {bold}(^){reset}")
    print(f"{bold}{'6.':<3}{reset} Módulo {bold}(|a| % b) {reset}")
    print(f"{bold}{'7.':<3}{reset} Porcentagem {bold}(%) {reset}")
    print(f"{bold}{'8.':<3}{reset} Raiz Quadrada {bold}(√){reset}")
    print()
    print(f"{bold}{sub}{azulc}{"Funções Trigonométricas"}{reset}")
    print()
    print(f"{bold}{'9.':<3}{reset} Seno {bold}(sin){reset}")
    print(f"{bold}{'10.':<3}{reset} Cosseno {bold}(cos){reset}")
    print(f"{bold}{'11.':<3}{reset} Tangente {bold}(tan){reset}")
    print(f"{bold}{'12.':<3}{reset} Arcoseno {bold}(asin){reset}")
    print(f"{bold}{'13.':<3}{reset} Arcocosseno {bold}(acos){reset}")
    print(f"{bold}{'14.':<3}{reset} Arcotangente {bold}(atan){reset}")
    print(f"{bold}{'15.':<3}{reset} Arcotangente² {bold}(atan²){reset}")
    print(f"{bold}{'16.':<3}{reset} Seno hiperbólico {bold}(sinh){reset}")
    print(f"{bold}{'17.':<3}{reset} Cosseno hiperbólico {bold}(cosh){reset}")
    print(f"{bold}{'18.':<3}{reset} Tangente hiperbólica {bold}(tanh){reset}")
    print(f"{bold}{'19.':<3}{reset} Arcoseno hiperbólico {bold}(asinh){reset}")
    print(f"{bold}{'20.':<3}{reset} Arcocosseno hiperbólico {bold}(acosh){reset}")
    print(f"{bold}{'21.':<3}{reset} Arcotangente hiperbólica {bold}(atanh){reset}")
    print(f"{bold}{'22.':<3}{reset} Radiano {bold}(rad){reset}")
    print()
    print(f"{bold}{sub}{azul}{"Funções Matemáticas Avançadas"}{reset}")
    print()
    print(f"{bold}{'23.':<3}{reset} Fatorial {bold}(!){reset}")
    print(f"{bold}{'24.':<3}{reset} Valor absoluto {bold}(|a|){reset}")
    print(f"{bold}{'25.':<3}{reset} Logaritmo de base 2 {bold}(log₂){reset}")
    print(f"{bold}{'26.':<3}{reset} Logaritmo de base 10 {bold}(log₁₀){reset}")
    print(f"{bold}{'27.':<3}{reset} Equação de 2º grau {bold}(ax²){reset}")
    print(f"{bold}{'28.':<3}{reset} Exponencial {bold}(exp){reset}")
    print(f"{bold}{'29.':<3}{reset} Média Aritmética {bold}(x̄){reset}")
    print()
    print(f"{bold}{vermelhoc}{'0.':<3}{reset} {bold}{sub}{vermelhoc}Sair{reset}")
    print()

    operacao = input("Selecione uma operação para seguir (1/29): ")
    print()

    if operacao == "0":
        print("Saindo...")                                                                         # Condicional que quebra o código se o usuário escolher a opção (Sair) no menu.
        print()
        break

    elif operacao == "1":
        print("-------------------- Soma (+) ---------------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} + {n2} = {Soma(n1, n2)}')
        print()
    
    elif operacao == "2":
        print("----------------- Subtração (-) -------------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} - {n2} = {Subtração(n1, n2)}')
        print()

    elif operacao == "3":
        print("----------------- Multiplicação (x) ---------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} * {n2} = {Multiplicação(n1, n2)}')
        print()

    elif operacao == "4":
        print("-------------------- Divisão (÷) ------------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        resultado = Divisão(n1, n2)
        if isinstance(resultado, str):
            print(resultado)
            print()
        else:
            print(f'{n1} / {n2} = {Divisão(n1, n2)}')
            print()
    
    elif operacao == "5":
        print("----------------- Potenciação (^) -----------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} ** {n2} = {Potenciação(n1, n2)}')
        print()
    
    elif operacao == "6":
        print("-------------------- Módulo (%) -------------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} % {n2} = {Módulo(n1, n2)}')
        print()

    elif operacao == "7":
        print("----------------- Porcentagem (%) -----------------")
        print()
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        print()
        print(f'{n1} / {n2} * 100 = {Porcentagem(n1, n2)}')
        print()
    
    elif operacao == "8":
        print("--------------- Raiz Quadrada (√) -----------------")
        print()
        n1 = Decimal(input('Digite o número: '))
        print()
        resultado = Raiz(n1)
        if isinstance(resultado, str):                                                             # O isinstance faz o usuário receber a mensagem de erro no formato de string,
            print(resultado)                                                                       # se não der erro, recebe o valor normal.
            print()
        else:
            print(f'A raiz quadrada de {n1} é {resultado}')
            print()
    
    elif operacao == "9":
        print("-------------------- Seno (sin) -------------------")
        print()
        n1 = Decimal(input('Digite o número: '))
        print()
        print(f'O seno de {n1} é {Seno(n1):.2f}')
        print()

    elif operacao == "10":
        print("------------------ Cosseno (cos) ------------------")
        print()
        n1 = Decimal(input('Digite o número: '))
        print()
        print(f'O cosseno de {n1} é {Cosseno(n1):.2f}')
        print()
    
    elif operacao == "11":
        print("----------------- Tangente (tan) ------------------")
        print()
        n1 = Decimal(input('Digite o número: '))
        print()
        print(f'A tangente de {n1} é {Tangente(n1):.2f}')
        print()

    elif operacao == "12":
        print("------------------ Arcoseno (asin) ----------------")
        print()
        try:
            n1 = float(input("Digite o número: "))
            print()
            print(f'O arco-seno de {n1} é {Arcoseno(n1)}')
            print()
        except ValueError:
            print("Erro! Insira um número válido!")                                                # Esse trecho funciona da mesma maneira que o outro, é apenas outra maneira de exibir uma mensagem de
            print()                                                                                # erro ao usuário, nesse caso, uma exceção, se o usuário digitar um número inválido.
    elif operacao == "13":
        print("---------------- Arcocosseno (acos) ---------------")
        print()
        try:
            n1 = float(input('Digite o número: '))
            print()
            print(f'O arco-cosseno de {n1} é {Arcocosseno(n1)}')
            print()
        except ValueError:
            print("Erro! Insira um número válido!")
            print()
    
    elif operacao == "14":
        print("----------------- Arcotangente (atan) -------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'O arco-tangente é {Arcotangente(n1):.2f}')
        print()
    
    elif operacao == "15":
        print("---------------- Arcotangente² (atan²) ------------")
        print()
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print()
        print(f'O arco-tangente² é {Arcotangente2(n1, n2)}')
        print()
    
    elif operacao == "16":
        print("------------ Seno hiperbólico (sinh) --------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'O seno hiperbólico de {n1} é {Seno_hip(n1):.2f}')
        print()
    
    elif operacao == "17":
        print("----------- Cosseno hiperbólico (cosh) ------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'O cosseno hiperbólico de {n1} é {Cosseno_hip(n1):.2f}')
        print()
    
    elif operacao == "18":
        print("---------- Tangente hiperbólica (tanh) ------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'A tangente hiperbólica de {n1} é {Tangente_hip(n1):.2f}')
        print()
    
    elif operacao == "19":
        print("--------- Arcoseno hiperbólico (asinh) ------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'O arcoseno hiperbólico de {n1} é {Arcoseno_hip(n1):.2f}')
        print()

    elif operacao == "20":
        print("-------- Arcocosseno hiperbólico (acosh) ----------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        resultado = Arcocosseno_hip(n1)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f'O arcocosseno hiperbólico de {n1} é {Arcocosseno_hip(n1):.2f}')
        print()
    
    elif operacao == "21":
        print("-------- Arcotangente hiperbólica (atanh) ---------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        resultado = Arcotan_hip(n1)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f'O arcotangente hiperbólica de {n1} é {Arcotan_hip(n1)}')
        print()
    
    elif operacao == "22":
        print("----------------- Radiano (rad) -------------------")
        print()
        n1 = Decimal(input('Digite o número: '))
        print()
        print(f'O radiano de {n1} é {Radiano(n1)}')
        print()

    elif operacao == "23":
        print("------------------ Fatorial (!) -------------------")
        print()
        n1 = int(input('Digite o número: '))
        print()
        resultado = Fatorial(n1)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f' O fatorial de {n1} é {Fatorial(n1)}')
        print()

    elif operacao == "24":
        print("------------ Valor absoluto (|a|) -----------------")
        print()
        n1 = int(input('Digite o número: '))
        print()
        print(f'O valor absoluto de {n1} é {Valor_Absoluto(n1)}')
        print()
    
    elif operacao == "25":
        print("------------ Logaritmo de base 2 (log₂) -----------")
        print()
        n1 = int(input('Digite o número: '))
        print()
        resultado = Logaritmo2(n1)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f'O logaritmo de base 2 de {n1} é {Logaritmo2(n1):.2f}')
        print()
    
    elif operacao == "26":
        print()
        n1 = int(input('Digite o número: '))
        print()
        resultado = Logaritmo10(n1)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f'O logaritmo de base 10 de {n1} é {Logaritmo10(n1):.2f}')
        print()
    
    elif operacao == "27":
        print("-------- Equação de 2º grau (ax²) -----------------")
        print()
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        n3 = float(input('Digite o terceiro número: '))
        print()
        print(Equação2(n1, n2, n3))
        print()
    
    elif operacao == "28":
        print("---------------- Exponencial (exp) ----------------")
        print()
        n1 = float(input('Digite o número: '))
        print()
        print(f'O exponencial de {n1} é {Exponencial(n1)}')
        print()
    
    elif operacao == "29":
        print("----------- Média Aritmética (x̄) -----------------")
        print()
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        n3 = float(input('Digite o terceiro número: '))
        n4 = float(input('Digite o quarto número: '))
        print()
        print(f'A média aritmética é {Média_Aritmética(n1, n2, n3, n4)}')
        print()

    else:
        print("----------------------------------------------------")
        print(f"{bold}{'Erro! Escolha uma opção válida'.center(51)}{reset}")                       # Imprime o erro se o usuário digitar qualquer coisa que não esteja no Menu de Operações.
        print("----------------------------------------------------")
        print()
    
    if not retomar():                                                                              # Condicional que executa a função break se o usuário não quiser retomar.
        break