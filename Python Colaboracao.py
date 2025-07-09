print("=== Bem-vindo ao Restaurante===")

nome = input("Por favor, informe seu nome: ")
quantidade_pessoas = input("Quantas pessoas estarão na reserva? ")
data_reserva = input("Para qual data deseja reservar? (ex: 08/07/2025): ")
horario_reserva = input("Qual horário deseja reservar? (ex: 19:30): ")
if horario_reserva <= "12:00":
    print("=== Menu Café da Manhã ===\n")
    print("1.  Suco natural, Frutas da estação, Mini pudim e Pão de queijo\n")
    print ("2.  Café, Pão francês, Bolo de cenoura e Salada de frutas\n")
    print("3.  Iogurte, Torradas com manteiga e Chá matte\n")
    opcaoUsuario = input("Escolha uma opção do menu: ")
    if opcaoUsuario == "1":
        print("Você escolheu: Suco natural, Frutas da estação, Mini pudim e Pão de queijo")
        valorFinal = 25.00* int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "2":
        print("Você escolheu: Café, Pão francês, Bolo de cenoura e Salada de frutas")
        valorFinal = 30.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "3":
        print("Você escolheu: Iogurte, Torradas com manteiga e Chá matte")
        valorFinal = 20.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
elif horario_reserva <= "18:00" and horario_reserva >= "12:00":
    print("=== Menu Almoço ===\n")
    print("1. Arroz com feijão, Bife acebolado, Salada verde e Suco natural\n")
    print("1. Arroz, strogonoff, e Refrigerante\n")
    print("3. Lasanha de carne, salada e Água com gás\n")
    opcaoUsuario = input("Escolha uma opção do menu: ")
    if opcaoUsuario == "1":
        print("Você escolheu: Arroz com feijão, Bife acebolado, Salada verde e Suco natural")
        valorFinal = 35.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "2":
        print("Você escolheu: Arroz, strogonoff, e Refrigerante")
        valorFinal = 35.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "3":
        print("Você escolheu: Lasanha de carne, salada e Água com gás")
        valorFinal = 35.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
else:
    print("=== Menu Jantar ===\n")
    print("1. Pizza do dia, Refrigerante e Sobremesa do dia\n")
    print("2. Massa ao molho branco, Salada Caesar, Vinho tinto e Sobremesa do dia\n")
    print("3. Camarão ao molho branco gratinado com batata, Suco natural e Sobremesa do dia\n")
    opcaoUsuario = input("Escolha uma opção do menu: ")
    if opcaoUsuario == "1":
        print("Você escolheu: Pizza do dia, Refrigerante e Sobremesa do dia")
        valorFinal = 50.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "2":
        print("Você escolheu: Massa ao molho branco, Salada Caesar, Vinho tinto e Sobremesa do dia")
        valorFinal = 60.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    elif opcaoUsuario == "3":
        print("Você escolheu: Camarão ao molho branco gratinado com batata, Suco natural e Sobremesa do dia")
        valorFinal = 70.00 * int(quantidade_pessoas)
        print(f"Valor total da reserva: R$ {valorFinal:.2f}\n")
    
    
    
    
    
    
    
# Exibindo os detalhes da reserva
print("\n=== Detalhes da Reserva ===")
print(f"Nome: {nome}")
print(f"Número de pessoas: {quantidade_pessoas}")
print(f"Data: {data_reserva}")
print(f"Horário: {horario_reserva}")
print(f"Valor total da reserva: R$ {valorFinal:.2f}")