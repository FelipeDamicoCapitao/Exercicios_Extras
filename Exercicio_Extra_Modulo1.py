##################################################
# Cores
# \033[style; text; back m
NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"

##################################################
# Input da população

#Definição de função
def erroN():
    #Se nao der erro:
    try:
        N = int(input(f"\n{NAmarelo}Digite a população da cidade:{Corfim} "))
        if N <= 0:
            print (f'{NVermelho}A população é sempre maior que zero{Corfim}')
            N = False
        
    #Se der erro:
    except:
        print(f"{NVermelho}Digite apenas numeros{Corfim}")
        N = False
    
    # Retorna a reposta, Se nao atender será False
    finally:
        return N

#Define N como retorno da Função
N = erroN()
while True:
    # Se Nao for um valor Maior que Zero, execute a função eternamente
    if N == False:
        N = erroN() #Define N como retorno da Função
    # Se atender os parametros, pare
    else:
        break

##################################################
# Input da Margem de Erro

#Definição de função
def ErroE():
    try:
        # Input de Margem de Erro
        E = float(input(f"\n{NAmarelo}digite a Margem de erro [%]:{Corfim}"))
        # Caso seja fora de 0% e 100%
        if E < 0 or E > 100:
            print (f'{NVermelho}A margem de erro deve ser um valor entre 0 e 100{Corfim}')
            E = False
        else:
            E = E/100
    
     # Retorna a reposta, Se nao atender será False
    except:
        print(f"{NVermelho}digite apenas numeros{Corfim}")
        E = False
        
    finally:
        return E
             
#Define E como retorno da Função
E = ErroE()
while True:
    # Se Nao for um valor entre 0 e 100, execute a função eternamente
    if E == False:
        E = ErroE()
    else:
        break

##################################################
# Grau de Confiança
print (f"\n{NAmarelo}o grau de confiaça é um valor tabelado, escolha entre uma das opçoes uns abaixo:{Corfim}\n")
print (f"{NBranco}1 - 80% de confiança")
print (f"2 - 85% de confiança")
print (f"3 - 90% de confiança")
print (f"4 - 95% de confiança")
print (f"5 - 99% de confiança{Corfim}")

#Definição da função
def erroZ():
    try:
        Z1 = int(input(f"\n{NAmarelo}Escolha o grau de confiança entre as Opçoes acima digitando entre 1 e 5:{Corfim} "))
        #Se nao for 1,2,3,4 ou 5:
        if Z1 < 1 or Z1 > 5:
            print (f"{NVermelho}Escolha entre 1 a 5{Corfim}")
            Z1 = False
    # Se você botar algo diferente de um numero:
    except:
        print(f"{NVermelho}digite apenas numeros{Corfim}")
        Z1 = False
    
    # Retorna a reposta, Se nao atender será False
    finally:
        return (Z1)


#Define Z1 como o Retono da função erroZ()
Z1 = erroZ()
while True:
    # Se Nao for um valor entre 0 e 100, execute a função eternamente
    if Z1 == False:
        Z1 = erroZ()
    # Se atender os parametros, pare
    else:
        break


#definindo grau de confiança a partir das opçoes
if Z1==1:
    Z = 1.28
elif Z1==2:
    Z = 1.44
elif Z1==3:
    Z = 1.65
elif Z1==4:
    Z = 1.96
elif Z1==5:
    Z = 2.58

##################################################
# Calculos
P = 0.5 # desvio padrao = 0.5, valor máximo para f(P) = P*(1-P)
A1 = (((Z**2)*P*(1-P))/E**2)
A2 = 1+(A1/N)
A = A1/A2
A = int(round(A+0.5)) # aredonda para cima e transforma em inteiro


##################################################
# Impressao de resultado
print (f"\n{NVerde}O tamanho da amostra será de {A} pessoas{Corfim}\n")

#amostra = (((Z**2)*p*(1-p))/e**2)/(1=(((z**2)*p*(1-p))/e**2*N))