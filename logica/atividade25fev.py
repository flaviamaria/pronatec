def idade(idade):
    return idade * 365

print(idade (15))



def verifica(a):
    if(a%2 ==0):
        return "par"
    else:
        return "impar"
   
print(verifica(1))



def verifica (a,b,c):
        if(a>b):
            return a 
        elif (b>c):
            return (b)
        else:
            return c

print(verifica(2, 3 , 90))







def calcular(a, b,c):
 calculo = (a + b + c) /3
 
 if(calculo >= 6):
    return "aprovado"
 else:
    return("reprovado")
    
 
print(calcular(10, 10, 4))



def n(a):
     if (a>=1):
         return "positivo"
     elif (a<0):
         return "negativo"
     else: 
         return "nulo"
print(n(1))



def qua (a):
    return a*a
print (qua(3))


def soma(a,b):
    return a+b
print(soma(10,10))



def sa (a,b,c,d):
    return a*c, b+d
print(sa(2,10,5,9))


def reais (a):
    return a * 5.79
print(reais(100))


def calcular_litro( preco_litro, valor_abastecer):
    litros_comprados= valor_abastecer/ preco_litro
    return litros_comprados
preco_litro= 6.19
valor_abastecer= 50 
litros= calcular_litro(preco_litro, valor_abastecer)
print(f"você poderá comprar {litros: .2f} litros de combustível.")