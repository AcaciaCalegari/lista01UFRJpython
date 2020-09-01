#Lista01
#Nome:AcaciaCalegari


#1- Funcao q calcula a area de um retangulo
def retangulo (a,b):
        """Dado dois valores calcula a Area do retangulo"""
    return a*b
        

#2- Funcao que calcula a area da superf́iciede um cubo que tem c por aresta
def cubo (c):
    """Calculando a area da superfıcie do cubo que tem c por aresta."""
    return c**3
    

#3-Funcao q calcula a area da coroa circular formada por dois cı́rculos de raios r1 e r
def coroa (r1,r2):
        """Area da coroa"""
        pi=3.14
        area=pi*(r1**2-r2**2)
        return area
        

#4- Funcao q calcula a media de dois numeros
def media (a,b):
        """Media de 2 numeros"""
    return (a+b)/2
        

#5- Funcao q calcula a ordenada de uma função de segundo grau dados os parâmetros a, b, c e a abscissa
def ordenada (a,b,c,x):
        """Ordenada de uma funcao de segundo grau"""
    return a*x**2+b*x+c
        

#6- Funcao que calcula a media ponderada de dois números com os respectivos pesos
def mediapond(a,p1,b,p2):
        """Media ponderada de 2 numeros"""
        p1=float(p1)
        return (a*p1+b*p2)/(p1+p2)

#7- Funcao q calcula o erro entre o valor da soma de uma PG infinita a partir de 1.0 e a soma dos n primeiros termos dessa PG.
def PG(n,q,a1=1.0):
    """Erro entre o valor da soma de uma PG inﬁnita a partir de 1.0
    e a soma dos n primeiros termos.  q eh a razao e 0 ≤ q < 1."""
    Sinf=1/(1-q)
    Sn=a1*(1-q**n)/(1-q)
    return Sinf-Sn,Sinf,Sn

    
#8- Funcao que Calcula a gorjeta do garçom, considerando 10% do valor da conta
def gorjeta(valor):
        """Gorjeta do garcao"""
        return valor*0.1
        

#9-Nova Funcao q Calcula o valor da gorjeta dado o valor da conta de um restaurante e a porcentagem exigida pela legislação para a gorjeta.
def novagorjeta(valor,gorjeta=10):
    """gorjeta do garcon eh 10"""
    return valor+valor*gorjeta/100.0
    
    
#10 Funcao q calcula o saldo final de uma conta dado o saldo inicial, o número de meses e a taxa de juros mensal
def saldoFinal(saldoInit, meses, juros):
    """Saldo ﬁnal de uma conta, dado o saldo inicial, o numero de meses e a taxa de juros mensal."""
    return saldoInit*(1+juros*meses/100)
    
    
#11 Funcao q calcula a distância que a correnteza arrasta um barco que atravessa um rio
def distancia(rio,correnteza,barco):
    """Distancia que a correnteza arrasta um barco que atravessa um rio. Sao conhecidas: a velocidade da correnteza, a largura do rio e a velocidade do barco perpendicular a correnteza."""
    return correnteza*(rio/barco)
    
