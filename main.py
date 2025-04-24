def interface(): #criando a interface do game.
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2])) #Inserindo a array na interface.
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2])) #Inserindo a array na interface.
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2])) #Inserindo a array na interface.
    
def validar(rodada): #Criando uma função para validar a vitória.
    global parar #Comando usado para deixar a variavel "parar" para ser global.
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada): #Validando a vitória em horizontal.
        interface() 
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada): #Validando a vitória em horizontal.
        interface() 
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada): #Validando a vitória em horizontal.
        interface() 
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada): #Validando a vitória em vertical.
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada): #Validando a vitória em vertical.
        print ("O {} Venceu!".format(rodada))
        interface()
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada): #Validando a vitória em vertical.
        print ("O {} Venceu!".format(rodada))
        interface()
        print ("O {} Venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada): #Validando a vitória em diagonal.
        print ("O {} Venceu!".format(rodada))
        interface()
        print ("O {} Venceu!".format(rodada))
        parar = True
    if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada): #Validando a vitória em diagonal.
        interface()
        print ("O {} Venceu!".format(rodada))
        parar = True
        
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] #Criando a array do tableiro.

parar = False #Criando a variável "parar".
rodada = "X"  #Criando a variável para começar a jogada com o X.
jogadas = 0 #Criando a variável jogadas.

while parar == False: #Criando um laço de repetição (Em quanto for falso irá executar).
    if jogadas == 9: #Validando o Empate.
        interface()
        print("Empate!")
        parar = True #trocando False para True para não executar mais.
              
    interface() #Mostrar a interface.
    
    linha = int(input("Digite a linha escolhida:")) #Pedindo para o usuário escolher a linha para qual ele quer marcar.
    coluna = int(input("Digite a coluna escolhida:")) #Pedindo para o usuário escolher a coluna para qual ele quer marcar.
    
    if rodada == "X":
        tabuleiro[linha][coluna] = "X" #Validando a escolha do usuário e adicinando o "X".
        validar(rodada)
        jogadas += 1 #Aumentando a quantidade que ja foi jogada.
        rodada = "O" #Trocar a rodada para o "O".
        
    elif rodada == "O":
        tabuleiro[linha][coluna] = "O" #Validando a escolha do usuário e adicionando o "O".
        validar(rodada)
        jogadas += 1
        rodada = "X" #Trocar a rodada para o "X" novamente.
