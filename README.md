<h1>TextBasedGame<h1>
print("Bem-vindo à Floresta Encantada!")
nome = input("Qual é o teu nome? ")
print(f"{nome}, queres jogar?")
escolha = input("Sim(S) ou Não(N) ").lower()
if escolha == "s":
    print("OK, vamos lá!")
elif escolha == "n":
    print("OK, obrigado!")
    import sys
    sys.exit()
print("Tu estás na Floresta Tropical!")
direcao1 = input(f"{nome}, queres ir pela esquerda, pela direita ou pela frente? ")
if direcao1 == "esquerda":
    print("tu andaste e encontraste um rio com animais selvangens,GAME OVER!")
elif direcao1 == "direita":
    print("tu foste a andar a caminhar por um caminho de terra.")
print("queres continuar a explorar o caminho?")

