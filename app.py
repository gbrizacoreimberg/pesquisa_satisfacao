print ("Pesquisa de Opinião")

contador_excelente = 0
contador_ruim = 0

for repeticoes in range (50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao_cliente = int(input("De 1 a 3 (onde 1 é excelente e 3 é ruim), qual seu nível de satisfação com nossos serviços? "))
    if opiniao_cliente == 1:
        print ("Excelente!")
        contador_excelente = contador_excelente + 1
    elif opiniao_cliente == 2:
        print ("Bom")
    elif opiniao_cliente == 3:
        print ("Ruim")
        contador_ruim = contador_ruim + 1

print (f"Quantidade de excelentes: {contador_excelente}")
print (f"Quantidade de ruins: {contador_ruim}")