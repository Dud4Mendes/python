lista = ["acotar", "o principe cruel", "harry potter e o talice de fogo", "icebreaker"]
 
while True:
    print("\n1 - aicionar a lista")
    print("2 - mandar item para o inferno")
    print("3 - lista atual")
    print("4 - get out")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        novo_item = input("Digite o novo item: ")
        lista.append(novo_item)
        print("Item adicionado à lista!")
    
    elif opcao == "2":
        if lista:
            print("Lista atual:", lista)
            item_excluir = input("Digite o número do item que deseja excluir: ")
            if item_excluir.isdigit() and int(item_excluir) <= len(lista):
                del lista[int(item_excluir)-1]
                print("Item excluído!")
            else:
                print("Opção inválida!")
        else:
            print("A lista está vazia!")
    
    elif opcao == "3":
        print("Lista atual:", lista)
    
    elif opcao == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")