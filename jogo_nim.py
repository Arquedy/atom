
#Comeco para selecao de modo de jogo
def main():
    print("Escolha:")
    print("1 - Para uma partida isolada")
    print("2 - Para um campeonato ")
    comeco = int(input(""))
    if comeco == 1:
        #vai escolher partida solo e puxar os parametros da partida
        print("OKs uma so entao")
        partida_unica()
    elif comeco == 2:
        #vai escolher campeonato e puxar os parametros da partida
        print("Fmz, melhor de 3")
        campeonato()
    elif comeco != 1 or 2:
        #enquanto o cabaco n escolher a opao correta vai ficar em loop
        main()
#se o pc comecar a jogada vai usar esse def
def computador_escolhe_jogada(n, m):
    num = n
    quantia = 0
    while num > 0:
        #nesse caso o pc ganhar pq dara 0
        if n < m:
            n = n - n
            num = n
        #verifica se pode um multiplo, se nao puder, pega a quantidade maxima
        else:
            quantia = n % (m + 1)
            if quantia > 0:
                n = n - quantia
                num = num - quantia
            else:
                n = n - m
                num = num - m
        if num == 0:
            print("Tirei", m, "ganhei do humano kkkkkkkkk")
            print("Fim de novo")
            break
        if quantia > 0:
            print("Tirei ", quantia, "pecas e sobou", n, "pecas")
        else:
            print("Tirei ", m, "pecas e sobou", n, "pecas")
        user = int(input("Sua vez: "))
        if user > m:
           print("Voce cagou digitando um numero maior que as pecas restantes, vamos de novo")
           return computador_escolhe_jogada(n, m)
        num = n - user
        n = n - user
        print("OKs agora sobrou", n, "pecas")
        if num == 0:
            print("Fim de jogo")

#usuario escolhe jogada
def usuario_escolhe_jogada(n, m):
    user = int(input("Lembre da quantidade de pecas que vc pode tirar: "))
    num = n
    while num > 0:
        n = n - user
        num = num - user
        if n == 0:
            print("Fim de jogo")
            break
        print("Tirou", user,"pecas")
        print("Minha vez")
        if n < m:
            n = n - n
            num = n
        #verifica se pode um multiplo, se nao puder, pega a quantidade maxima
        else:
            quantia = n % (m + 1)
            if quantia > 0:
                n = n - quantia
                num = num - quantia
            else:
                n = n - m
                num = num - m
        if num == 0:
            print("Tirei", m, "ganhei do humano kkkkkkkkk")
            print("Fim de novo")
            break
        if quantia > 0:
            print("Tirei ", quantia, "pecas e sobou", n, "pecas")
        else:
            print("Tirei ", m, "pecas e sobou", n, "pecas")
        print("Restou", n, "pecas, sua vez")
        user = int(input(""))

#comeco da partida unica
def partida_unica():
    partida()

def campeonato():
    partida()
    con = 2
    while con > 0:
       con = con - 1
       partida()
       if con == 0:
           print("******Ganhou a partida*******")


#definicao da partida
def partida():
    n = int(input("Quantidades de pecas?: "))
    m = int(input("Limite de pecas tiradas?: "))
    com_comeca = (n % (m + 1))
    if com_comeca == 0:
        print("Voce comeca!!!")
        return usuario_escolhe_jogada(n, m)
    else:
        print("Muito lento ja comecei")
        return computador_escolhe_jogada(n, m)
print("Bem vindo ao jogo do NIM")
main()
