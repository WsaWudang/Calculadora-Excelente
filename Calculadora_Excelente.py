#Wesley Almeida 26/08/2021 Calculadora Excelente calculadora basica para estudos 

def main():
	print("BEM VINDO A CALCULADORA EXCELENTE \n ".center(100)) 
	
	print ("Qual tipo de operação iremos realizar ? \n ") 

	print ("Aperte + Para Adição ") 
	print ("Aperte - Para Subtração ")
	print ("Aperte * Para Multiplicação ")

	operacao = (input("Aperte / Para Divisão: "))

	if (operacao == "+"):
		adicao()
	elif (operacao == "-"):
		subtracao()
	elif (operacao == "*"):
		multiplicacao()
	elif (operacao == "/"):
		divisao()
	else: 
		main()

def adicao():
	a = numero()
	b = numero()
	c = a + b

	resultado("soma", a, b, c)

	novaOperacao()
			
def subtracao():
	a = numero()
	b = numero()
	c = a - b

	resultado("subtração", a, b, c)

	novaOperacao()

def multiplicacao():
	a = numero()
	b = numero()
	c = a * b

	resultado("multiplicacao", a, b, c)

	novaOperacao()


def divisao():
	a = numero()
	b = numero()
	c = a / b

	resultado("divisao", a, b, c)

	novaOperacao()

def novaOperacao():
	resposta = input("Deseja fazer uma nova operação? S/N ")

	if (resposta == "S" or resposta == "s" or resposta == "sim" or resposta == "SIM"):
		main()
	elif (resposta == "N" or resposta == "n" or resposta == "nao" or resposta == "NAO"):
		exit()
	else:
		novaOperacao()

def numero():
	a = int(input("Digite o numero: "))
	return a 
	
def resultado(operador, a, b, c):
	print("A ", operador, " de ", a, " e ", b, "é igual:", c)

main()


