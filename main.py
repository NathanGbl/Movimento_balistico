from funcoes import *

opcao = -1
while opcao != 0:
    opcao = menu()
    if opcao == 1:
        print(f"Posição: {mov_horizontal()}")
    elif opcao == 2:
        opcao2 = menu_2()
        if opcao2 == 1:
            print(f"Altura: {mov_vertical()}")
        elif opcao2 == 2:
            print(f"Vx: {vx()}")
        elif opcao2 == 3:
            opcao3 = int(input("Qual modo de calcular vy? "))
            if opcao3 == 1:
                print(f"Vy: {vy()}")
            else:
                print(f"Vy: {vy2()}")
    elif opcao == 3:
        print(f"Distância: {dist_proj_orig()}")
    elif opcao == 4:
        print(f"Módulo da velocidade: {v()}")
    elif opcao == 5:
        print(f"Tempo de subida: {tempo_sub}s")
    elif opcao == 6:
        print(f"Equação da trajetória: {eq_traj()}")
    elif opcao == 7:
        print(f"Altura: máxima: {alt_max()}")
    elif opcao == 8:
        print(f"Tempo de alcance: {temp_alc()}s")
    elif opcao == 9:
        print(f"Alcance: {alcance()}")

