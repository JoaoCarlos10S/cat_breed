def madlib():
    print("Vamos jogar Mad Libs!")
    print("Preencha as palavras abaixo:\n")

    nome = input("Digite um nome: ")
    lugar = input("Digite um lugar: ")
    animal = input("Digite um animal: ")
    verbo = input("Digite um verbo (no infinitivo): ")
    adjetivo = input("Digite um adjetivo: ")
    objeto = input("Digite um objeto: ")

    print("\n--- Sua história maluca ---\n")
    print(f"Era uma vez {nome}, que morava em {lugar}.")
    print(f"Um dia, encontrou um {animal} muito {adjetivo} que sabia {verbo}!")
    print(f"Eles se tornaram amigos e juntos foram explorar o mundo com apenas um {objeto} nas mãos.")
    print("E assim começou a aventura mais estranha de todas...\n")

if __name__ == "__main__":
    madlib()
