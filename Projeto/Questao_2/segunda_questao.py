def automato(funcao_transicao,q0,conj_est_finais, cadeia):
    estado_atual=q0
    for simbolo in cadeia:
        # print(f'({estado_atual}, {simbolo}) ---> {funcao_transicao.get((estado_atual, simbolo))}')
        estado_atual=funcao_transicao.get((estado_atual, simbolo))
        if estado_atual == None:
            break
    return estado_atual in conj_est_finais

def automato_segunda_questao (cadeia:str): 
    estados= ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10']
    alfabeto=['c','o','m','p','u','t','a','d','o','r']
    funcao_transicao={
                    ('q0','c'):'q1', 
                    ('q1','o'):'q2',
                    ('q2','m'):'q3',
                    ('q3','p'):'q4',
                    ('q4','u'):'q5',
                    ('q5','t'):'q6',
                    ('q6','a'):'q7',
                    ('q7','d'):'q8',
                    ('q8','o'):'q9',
                    ('q9','r'):'q10',
                    }
    estado_inicial='q0'
    estados_finais=['q10']
    
    return automato(funcao_transicao,estado_inicial,estados_finais,cadeia)

def segunda_questao():
    texto = 'O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.'
    posicoes=[]
    cont=0
    for i, palavra in enumerate(texto.split()): 
        if automato_segunda_questao(palavra) == True: 
            posicoes.append(i+1)
            cont+=1

    if cont == 0: 
        retorno= 'Não contem no texto a palavra computador.'
    else: 
        retorno= (f'''
            A palavra 'computador' aparece {cont} vezes no texto.
            Nas posições {posicoes}
        ''')
    return retorno 
