print("Bem-vindo à Floresta Encantada!")
nome = input("Qual é o teu nome? ")
print(f"{nome}, queres jogar?")
escolha = input("Sim(S) ou Não(N) ").lower()
if escolha == "s":
    print("OK, vamos lá!")
elif escolha == "n":
    print("OK, obrigado!")
    exit()
print("Tu estás na Floresta Tropical!")
direcao1 = input(f"{nome}, queres ir pela esquerda, pela direita ou pela frente? ")
if direcao1 == "esquerda":
    print("tu andaste e encontraste um rio com animais selvangens,GAME OVER!")
    exit()
elif direcao1 == "frente":
    print("tu foste a andar a caminhar por um caminho de terra.")
print("queres continuar a explorar o caminho?")
escolha2 = input("Sim(S) ou Não(N)").lower()
print("continuaste a andar e encontraste uma espada, desejas pegar nela?")
escolha3 = input("Sim(S) ou Não(N)").lower()
print("Prepara-te encontraste um Goblin Gigante!")
print("queres atacar o goblin gigante?")
escolha4 = input("Sim(S) ou Não(N)").lower()
if escolha4 == "Sim(S)":
    print("MUITO BEM!, tu conseguiste matar o gigante,GANHASTE!")
    exit()
elif escolha4 == "Não(N)":
    print("o goblin gigante atacou-te e tu morreste! GAME OVER!")
    exit()
if direcao1 == "direita":
    print("encontraste uma casa!")
print("queres entrar na casa?")
escolha5 = input("Sim(S) ou Não(N)").lower()
if escolha5 == "SIM(s)":
    print("entraste na casa, a tua frente tem umas escadas queres subir?")
escolha6 = input("Sim(S) ou Não(N)").lower()
if escolha6 == "SIM(s)":
    print("JA FOSTE!, encontraste um dragão e morreste!")
if escolha6 == "Não(N)":
    print("Encontraste muitas armas!")
print("queres pegar nas armas e depois subir as escadas?")
escolha7 = input("Sim(S) ou Não(N)").lower()
print("OK, agora sobe as escadas!")
print("esta ali o dragão!")
print("queres atirar no dragão para ganhar?")
escolha8 = input("Sim(S) ou Não(N)").lower()
if escolha8 == "SIM(S)":
    print("Parabéns,Tu conseguiste, GANHASTE!")
elif escolha8 == "NÃO(N)":
    print("o dragão matou-te GAME OVER!")
    exit()