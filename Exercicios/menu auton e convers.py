print("bem - vindo ao menu!")
print("1 - Autonomia de combustivel na viagem ")
print("2 - Conversor de temperatura de Celsius a Fahrenheit ")
print("0 - sair ")
menu = int(input("qual o menu que deseja: "))

# conversão de Celsius para Fahrenheit  = (9 * Celsius + 160) / 5

def lendo_celsius():
    celsius = float(input("Digite a temperatura em Graus Celsius: "))
    return celsius

def conversao(celsius):
    Fahrenheit  = (9 * celsius + 160) / 5
    return Fahrenheit

def resultado_conversao(Fahrenheit):
    print("A temperatura em Fahrenheit é de: ", Fahrenheit)

# fórmula dos devidos cálculos da autonomia de combustível 

def lendo_valores():
    tempo_gasto = float(input("Qual o tempo gasto na viagem em horas : "))
    vel_media = float(input("Qual velocidade média da viagem em KM/h: "))
    return tempo_gasto, vel_media
        
def calculo_distancia(tempo_gasto, vel_media): 
    distancia = tempo_gasto * vel_media
    return distancia

def quantidade_litros(distancia):
    litros_usados = distancia / 12 
    return litros_usados

def resultados(vel_media, tempo_gasto, distancia, litros_usados):
    print("A velocidade média foi de:",vel_media)
    print("O tempo gasto foi de:",tempo_gasto,"H")
    print("A distância em KM foi de:", distancia)
    print("O total de litros usados foram de :",litros_usados)

# condicionais

if menu ==1:
    tempo_gasto, vel_media = lendo_valores()
    distancia = calculo_distancia(tempo_gasto, vel_media)
    litros_usados = quantidade_litros(distancia)
    resultados(vel_media, tempo_gasto, distancia, litros_usados)
else:
    if menu==2:
        celsius = lendo_celsius  
        Fahrenheit = conversao(celsius)
        resultado_conversao(Fahrenheit) 
    else:
        if menu==0:
            print("O programa foi encerrado :) ")
            breakpoint

