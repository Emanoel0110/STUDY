import random

%%%-----------------------Dicionario de simbolos-----------------------%%%
abc = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,
       'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
       'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,' ':36,
       '1':37,'2':38,'3':39,'4':40,'5':41,'6':42,'7':43,'8':44,'9':45,
       '0':46,'!':47,'@':48,'#':49,'$':50,'%':51,'¨':52,'&':53,'º':54,
       '^':55,'~':56,'.':57,'>':58,'=':59}

%%%--------------------------RSA--------------------------%%%
#Numeros Primos
p = 457
q = 347
#Modulo
n = p*q
#Phi(n)
phi_n = (p-1)*(q-1)
#Chave pública
e = 107

def RSA(valor_entrada):
    for i in range(0, len(valor_entrada)):
        lista_de_restos.append(int((int(valor_entrada[i])**e)%n))

    return lista_de_restos

%%%-----------------------Chave Privada-----------------------%%%
def Chave_Privada(chave_publica):
    for i in range(1,phi_n):
        if i*e%phi_n==1:
            return i

d = int(Chave_Privada(e))

%%%-----------------------Lista de valores-----------------------%%%
lista_string = []
lista_de_restos = []

def Lista_de_valores(valor_entrada):
   for i in range(0,len(valor_entrada)):
       lista_string.append((abc[valor_entrada[i]]))
   return lista_string

%%%-----------------------Palavra Cifrada-----------------------%%%
def Gerar_String(valor_entrada):
    valor_cifrado = ''
    for i in range(0, len(valor_entrada)):
        valor_cifrado += str(valor_entrada[i])
    return  valor_cifrado

lista_novos_valores = []
def Valor_Cifrado(valor_entrada):
        ind  = 0
        for i in range(0,len(valor_entrada)):
            valor = random.randint(1, 5)
            lista_novos_valores.insert(ind, str(valor) + str(valor_entrada[ind]))

            ind += 1
            if (ind == len(valor_entrada)):
                break
        return lista_novos_valores

def Palavra_Cifrada(valor_entrada):
    list_of_key = list(abc.keys())
    list_of_value = list(abc.values())
    palavra_cifrada = ''

    for valor in valor_entrada:
        position = list_of_value.index(int(valor))
        palavra_cifrada+=list_of_key[position]
    return palavra_cifrada

%%%-----------------------Decifrar RSA-----------------------%%%
lista_valores_decifrados = []
def Decifrar_RSA(valor_entrada):
    ind = 0
    for i in valor_entrada:
        valor = int(i)**d%n
        lista_valores_decifrados.insert(ind, valor)

        ind+=1
    return lista_valores_decifrados

def Palavra_Decifrada(valor_entrada):
        list_of_key = list(abc.keys())
        list_of_value = list(abc.values())
        palavra_decifrada = ''

        for valor in valor_entrada:
            position = list_of_value.index(int(valor))
            palavra_decifrada += list_of_key[position]
        return palavra_decifrada

%%%-----------------------Entrada de dados-----------------------%%%
palavra = input("Digite uma palavra: ")
palavra=palavra.upper()

a = Lista_de_valores(palavra)
b = RSA(a)
c = Gerar_String(b)
k = Valor_Cifrado(c)

print("Palavra Cifrada: "+str(Palavra_Cifrada(k)))
