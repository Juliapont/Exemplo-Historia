import random

# Função que gera a introdução da historia 
def gerar_introducao():
    introducoes = ["Era uma vez","Há muio tempo atrás","Num reino distante"]
    return random.choice(introducoes)

# Função que gera o desenvolvmento da história 
def gerar_desenvolvimento():
    desenvolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro", "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(desenvolvimentos)

# Função que gera o final da históri
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.","descobrindo um tesouro escodindo.", "salvando o reino da escuridão.","encontrando um amor verdadeiro."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada 
if __name__=="__main__":
   print(gerar_historia())
