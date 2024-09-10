import random

palavras = ['computador', 'mulher', 'cachorro', 'gato', 'televisão']

palavra = random.choice(palavras)

print(palavra)

numero_tentativas = 0
chances = 5
letra_escolhida = []

estado_atual = ['_'] * len(palavra)


print('bem vindo ao jogo, seu objetivo é descobrir a palavra secreta! boa sorte')

while numero_tentativas < chances and ''.join(estado_atual) != palavra: 

    letra =  input('\nqual letra você quer tentar? ')
    
    while letra in letra_escolhida:
        print('você escolheu uma letra que ja tinha tentado. escolha outra')
        letra =  input('\nqual letra você quer tentar? ')
    

    letra_escolhida.append(letra)
    
    if letra in palavra:
       print('\n\nparabéns você acertou a letra!')
       for i in range(len(palavra)):
           if letra == palavra[i]:
               estado_atual[i] = letra 
   
    else:
        print('você errou a letra, tente novamente!')
        numero_tentativas += 1
    
    print('restam', chances - numero_tentativas, 'tentativas')
    
    print('esse é o estado atual da sua palavra: ')
    print(estado_atual)
    
    
    print('as letras que você ja tentou são: ') 
    for item in letra_escolhida:
        print(item, end=' ')

if numero_tentativas == chances:
    print('\n\nvocê perdeu, acabaram suas tentativas!')
else:
    print('você ganhou! parabéns.')
    
print('a palavra era', palavra)
