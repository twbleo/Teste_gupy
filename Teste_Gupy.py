Linguaguem utilizada: Python


Exercício 1) Observe o trecho de código abaixo: ao final do processamento, qual será o valor da variável SOMA?

Resposta : 91 pois , 1+2+3+4+5+6+7+8+9+10+11+12+13 = 91


Exercício 2 :

numero = int(input("Digite um número para verificar se existe na sequencia fibonnaci: "))

fb = [0, 1]

while fb[-1] < numero:
    numero_apos = fb[-1] + fb[-2]
    fb.append(numero_apos)

if numero in fb:
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")



Exercício 3 :


a) 1, 3, 5, 7, ___ --> 9

b) 2, 4, 8, 16, 32, 64, ___ --> 128

c) 0, 1, 4, 9, 16, 25, 36, ____ --> 49

d) 4, 16, 36, 64, ___ --> 108

e) 1, 1, 2, 3, 5, 8, ____ --> 13

f) 2,10, 12, 16, 17, 18, 19, __ --> 20



4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta: Eu ligaria um interruptor e o deixaria ligado , iria ate a sala e ligaria e desligari outro interruptor . com isso na 2 ida eu teria ideia de todas lampadas conectadas a tal interuptores.


ex: NA 2 visita a lampada acessa seria do 1 interruptor , quando eu ligasse o 2 , a lampada que acendesse me mostraria o proximo e logo sobraria o ultimo interruotor com respectiva lampada



5)

Frase_original = str(input("Insiria a frase: "))

frase_invertida = Frase_original[::-1]

print("frase invertida: ", frase_invertida)
