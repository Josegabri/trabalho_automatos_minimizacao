import Questao_1.primeira_questao as q1
import Questao_2.segunda_questao as q2
import Questao_3.terceira_questao as q3

#Escolha de questão pelo usuário
escolher_questao = int(input('\nEscolha a questão que deseja para realizar o teste: \nDigite "1" para a primeira questão (AFD para reconhecer linguagens) \nDigite "2" para a segunda questão (AFD para reconhecer a recorrência de palavras "computador") \nDigite "3" para a terceira questão (Transdutor Finito) \nDigite "4" para finalizar o teste \nEscolha a questão ou finalize o teste: '))

#Variável de alternativas da questão e das respectivas validações
alternativas = 'abcd'
linguagens = ['(ab*c*)*', 'aaa(b|c)*|(b|c)*aaa', 'a*b|ab*', 'a*b*(a|ac*)']

#laço para as questões e finalização do programa.
while (escolher_questao != 4):
    if escolher_questao == 1:
        print('\nVocê escolheu a questão 1. \n\nAgora escolha a alternativa que deseja para testar: ')
        #laço para a descrição das alternativas.
        for c in range(0, 4):
            print(f'Digite "{alternativas[c]}" para escolher a linguagem "{linguagens[c]}"')
        escolher_alternativa = input('\nEscolha a alternativa: ')
        print() #pular linha

        while (escolher_alternativa != "0"):
            #Esta condição faz o teste da linguagem (ab*c*)*, sendo q0 e q2 estados finais.
            if escolher_alternativa == 'a':
                cadeia = input('Você escolheu validar a linguagem "(ab*c*)*" \nDigite a cadeia para ser validada: ')
                print(q1.automato_a(cadeia))
            #Esta condição faz o teste da linguagem aaa(b|c)*|(b|c)*aaa, sendo q3 e q7 estados finais.
            elif escolher_alternativa == 'b':
                cadeia = input('Você escolheu validar a linguagem "aaa(b|c)*|(b|c)*aaa" \nDigite a cadeia para ser validada: ')
                print(q1.automato_b(cadeia)) 
            #Esta condição faz o teste da linguagem a*b|ab*, sendo q1, q3, q4 e q5 estados finais.
            elif escolher_alternativa == 'c':
                cadeia = input('Você escolheu validar a linguagem "a*b|ab*" \nDigite a cadeia para ser validada: ')
                print(q1.automato_c(cadeia)) 
            #Esta condição faz o teste da linguagem a*b|ab*, sendo q1 e q3 estados finais.
            elif escolher_alternativa == 'd':
                cadeia = input('Você escolheu validar a linguagem "a*b*(a|ac*)" \nDigite a cadeia para ser validada: ')
                print(q1.automato_d(cadeia)) 
            #Caso o usuário erre a alternativa
            else:
                escolher_alternativa = input('Você escolheu uma alternativa inexistente. \nEscolha novamente: ')
                print() #pular linha
                continue
            escolher_alternativa = input('Escolha a mesma ou outra alternativa para fazer o teste, ou digite 0 para sair da questão: ')
            print() #pular linha
    elif escolher_questao == 2:
        #Validação da questão 2 redigida na lista passada pelo professor
        print('''Você escolheu a alternativa 2 para ser válidada.
              O programa irá apontar em quais posições ocorreram o casamento exato da palavra "Computador"
              no texto descrito na questão pelo professor.
              ''')
        print(q2.segunda_questao())

    elif escolher_questao == 3:
        #Transdutor finito baseado na Máquina de Mealy, com uma entrada sendo inserida pelo usuário e o programa retornando uma saída.
        q3.terceira_questao()
    
    escolher_questao = int(input('\nEscolha outra questão ou digite "4" para finalizar o teste: '))

