import math

array_numeros = []

print("""Bem-vindo(a) a calculadora de estatística simples: 
         Informe os valores que serão calculados e a operação logo em seguida.
         Lembre-se de informar X quando quiser parar de informar números.
      """)
while (True):
    num = input("""Digite um número: """)
    if str(num) == 'X':
        break
    else:
        array_numeros.append(num)
        
    
    

print(f"Valores inseridos: {array_numeros}")
print("""Valores inseridos!
        Informe a operação que quer realizar com os números inseridos>
      1- Calcular a média
      2- Calcular a mediana
      3- Calcular a moda
      4- Calcular o desvio padrão      
    """)

while(True):
    opc = int(input("Digite a opção: "))
    soma = 0
    match(opc):
        case 1: #média
            for i in range (len(array_numeros)):
                soma += float(array_numeros[i])
            print(f"A média dos valores informados é: {soma/len(array_numeros)}")
        case 2: #mediana
            array_numeros.sort()
            resto = len(array_numeros)%2
            if resto == 1:
                posicao = round(len(array_numeros)/2)
                mediana = array_numeros[posicao]
            
            elif resto == 0:
               posicao = round(len(array_numeros)/2)
               mediana = (float(array_numeros[posicao]) + float(array_numeros[posicao-1]))/2
                 
            print(f"A mediana dos valores inseridos é: {mediana}")

        case 3: #moda
            moda_Count = []
            moda_Count.clear()
            for i in range(len(array_numeros)):
                controle = array_numeros[i]
                moda_M = array_numeros.count(controle)
                moda_Count.append(moda_M)
                if moda_M > moda_Count[i]:
                    maior_C_moda = moda_M
                    moda = array_numeros[i] 
                else:
                    maior_C_moda = moda_Count[i] 
                    moda = array_numeros[i]


            print(f"A moda dos valores inseridos é: {moda}")
        
        case 4: #desvio padrão
            soma = 0
            dp_S = 0
            array_somatorio = []
            for i in range(len(array_numeros)):
                soma += float(array_numeros[i])
            media = soma/len(array_numeros)
            print(media)
            for j in range(len(array_numeros)):
                dp_S += (float(array_numeros[j]) -  media)**2
                array_somatorio.append(dp_S)
            print(array_somatorio)
            Desvio_Padrao = math.sqrt(dp_S)/math.sqrt(len(array_numeros))

            print(f"O Desvio padrão dos valores inseridos é: {Desvio_Padrao}")

        case default:
            break


