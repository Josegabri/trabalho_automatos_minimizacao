"""
    Implemente um transdutor finito (máquina de Moore ou Mealy) que, dada uma sequência de
    moedas de 25 e 50 centavos e de 1 real, forneça uma lata de refrigerante quando a sequência
    totalizar 1 real ou mais. Cada moeda inserida deverá corresponder a uma de duas saídas: 0,
    se uma lata não pode ser (ainda) liberada, ou 1, se uma lata deve ser liberada.
"""

def maquina_mealy(funcao_transicao, q0, conj_est_finais):
    estado_atual = q0
    while True:
        simbolo = input('Coloque uma moeda na máquina (Digite 0 para sair da máquina): ')
        if simbolo == '0':
            break
        elif (simbolo != '25' and simbolo != '50' and simbolo != '100'):
            print('\nO valor digitado é inválido, tente novamente. \n')
            continue
        # print(f'Entrada: ({estado_atual}, {simbolo}) ---> {funcao_transicao.get((estado_atual, simbolo))[0]}')
        if int(funcao_transicao.get((estado_atual, simbolo))[1]) >= 100:
            print(f'Saída:   ({estado_atual}, {simbolo}) ---> 1 \n')
        else:
            print(f'Saída:   ({estado_atual}, {simbolo}) ---> 0 \n')
        estado_atual = funcao_transicao.get((estado_atual, simbolo))[0]


def terceira_questao():
    funcao_transicao_q2 = {
        ('q0', '25'): ('q1', '25'),
        ('q0', '50'): ('q2', '50'),
        ('q0', '100'): ('q4', '100'),
        ('q1', '25'): ('q2', '50'),
        ('q1', '50'): ('q3', '75'),
        ('q1', '100'): ('q5', '125'),
        ('q2', '25'): ('q3', '75'),
        ('q2', '50'): ('q4', '100'),
        ('q2', '100'): ('q6', '150'),
        ('q3', '25'): ('q4', '100'),
        ('q3', '50'): ('q5', '125'),
        ('q3', '100'): ('q7', '175'),
        ('q4', '25'): ('q1', '25'),
        ('q4', '50'): ('q2', '50'),
        ('q4', '100'): ('q4', '100'),
        ('q5', '25'): ('q2', '50'),
        ('q5', '50'): ('q3', '75'),
        ('q5', '100'): ('q5', '125'),
        ('q6', '25'): ('q3', '75'),
        ('q6', '50'): ('q4', '100'),
        ('q6', '100'): ('q6', '150'),
        ('q7', '25'): ('q4', '100'),
        ('q7', '50'): ('q5', '125'),
        ('q7', '100'): ('q7', '175')   
    }
    q0 = 'q0'
    estados_finais = ['100', '125', '150', '175']
    maquina_mealy(funcao_transicao_q2, q0, estados_finais)

terceira_questao()
