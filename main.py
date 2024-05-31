import statistics

array_numeros = []

print("""Bem-vindo(a) a calculadora de estatística simples: 
         Informe os valores que serão calculados e a operação logo em seguida.
         Lembre-se de informar 00 toda vez que quiser parar de informar números.
      """)
while (True):
    num = float(input("""Digite um número: """))
    if num == 00:
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
                soma += array_numeros[i]
            print(f"A média dos valores informados é: {soma/len(array_numeros)}")
        case 2: #mediana
            mediana = statistics.median(array_numeros)
            print(f"A mediana padrão dos valores inseridos é: {mediana}")

        case 3: #moda
            moda = statistics.mode(array_numeros)
            print(f"A mediana padrão dos valores inseridos é: {moda}")
        
        case 4: #desvio padrão
            desvio_padrao = statistics.stdev(array_numeros)
            print(f"O Desvio padrão dos valores inseridos é: {desvio_padrao}")

        case default:
            break


