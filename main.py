import random
condicao = True
condicao2 = True
cont = 0
i = 1
lista = []
while condicao:
    quantidade = int(input('Quantos números? '))
    int1, int2 = input('Qual o intervalo? ').split()
    if quantidade >  abs(int(int2) - int(int1)):
        print('Erro!')
        print('Não posso gerar {} numeros não repetidos entre {} e {}!'.format(quantidade, int1, int2))
    else:
        while condicao2:
            if cont == 10:
                condicao2 = False
                for ele in lista:
                    print('Elemento {} = {}'.format(i, ele))
                    i = i + 1
            elif cont < 10:
                elemento = str(random.randint(int(int1), int(int2)))
                if elemento in lista :
                    elemento = str(random.randint(int(int1), int(int2)))
                    condicao2 = True
                elif elemento not in lista:
                    lista.append(elemento)
                    cont = cont + 1
                    condicao2 = True
