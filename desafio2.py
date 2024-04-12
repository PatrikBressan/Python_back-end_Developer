# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []


# TODO: Crie um loop para solicita os itens ao usuário:
for i in range (0, 3):
  item = input(f'Digite o item número {i+1} de 3 itens possíveis: ')
  itens.append(item)

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")