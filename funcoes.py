from math import *

def menu():
    print("Escolha uma das opções abaixo")
    print("1. Movimento horizontal")
    print("2. Movimento vertical")
    print("3. Distância entre o projétil e a origem")
    print("4. Módulo da velocidade")
    print("5. Tempo de subida")
    print("6. Equação da trajetória")
    print("7. Altura máxima")
    print("8. Tempo de alcance")
    print("9. Alcance")
    print("0. Sair")

    opcao = int(input("Opção: "))
    return opcao

def menu_2():
    print("Que dado quer saber?")
    print("1. Altura")
    print("2. Vx")
    print("3. Vy")
    opcao = int(input("Opção: "))
    return opcao

'''mov horizontal'''
def mov_horizontal():
    x0 = float(input("Valor de x0: "))
    v0x = float(input("Valor de v0x: "))
    t = float(input("Valor de t: "))
    return x0 + v0x*t

'''mov vertical'''
def mov_vertical():
    y0 = float(input("Valor de y0: "))
    v0y = float(input("Valor de v0y: "))
    t = float(input("Valor de t: "))
    print(t)
    return y0 + v0y*t - (5*(pow(t,2)))

def vx():
    v = float(input("Valor de v: "))
    angulo = float(input("Valor do ângulo(em graus): "))
    return v*cos(radians(angulo))

def vy():
    v = float(input("Valor de v: "))
    angulo = float(input("Valor do ângulo: "))
    return v*sin(radians(angulo))

def tg():
    vx = float(input("Valor de vx: "))
    vy = float(input("Valor de vy: "))
    return vy / vx

'''Distância entre o projétil e a origem'''
def dist_proj_orig():
    x = float(input("Valor de x: "))
    y = float(input("Valor de y: "))
    return sqrt(pow(x,2) + pow(y,2))

''' Módulo velocidade'''
def v():
    vx = float(input("Valor de vx: "))
    vy = float(input("Valor de vy: "))
    return sqrt(pow(vx,2) + pow(vy,2))

'''Tempo subida'''
def tempo_sub():
    v0 = float(input("Valor de v0: "))
    angulo = float(input("Valor do ângulo(em graus): "))
    return (v0*sin(radians(angulo)) / 10)

'''Eq trajetoria'''
def eq_traj():
    angulo = float(input("Valor do ânuglo(em graus): "))
    x = float(input("Valor de x: "))
    v0 = float(input("Valor de v0: "))
    return tan(radians(angulo)*x - (0.5*10*(pow(x,2)/(pow(v0,2)*pow(cos(radians(angulo)),2)))))

'''Altura máxima'''
def alt_max():
    v0 = float(input("Valor de v0: "))
    angulo = float(input("Valor do ângulo(em graus): "))
    return 0.5*((pow(v0,2)*pow(sin(radians(angulo)), 2))/10)

'''tempo alcance'''

def temp_alc():
    tempo_sub = float(input("Valor do tempo de subida: "))
    return tempo_sub * 2

'''Alcance'''
def alcance():
    v0 = float(input("Valor de v0: "))
    angulo = float(input("Valor do ângulo(em graus): "))
    return (pow(v0,2) * sin(2*radians(angulo))) / 10

