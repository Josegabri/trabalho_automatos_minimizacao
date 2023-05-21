# Função que define o automato 

def automato(funcao_transicao,q0,conj_est_finais, cadeia):
    estado_atual=q0
    for simbolo in cadeia:
        print(f'({estado_atual}, {simbolo}) ---> {funcao_transicao.get((estado_atual, simbolo))}')
        estado_atual=funcao_transicao.get((estado_atual, simbolo))
        if estado_atual == None:
            break
    return estado_atual in conj_est_finais
  
# LETRA A 
def automato_a(cadeia:str):
  estados_a = ['q0', 'q1', 'q2']
  alfabeto_a = ['a', 'b', 'c']
  funcao_transicao_a = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): None,
    ('q0', 'c'): 'q0',
    ('q1', 'a'): None,
    ('q1', 'b'): 'q2',
    ('q1', 'c'): None,
    ('q2', 'a'): 'q1',
    ('q2', 'b'): None,
    ('q2', 'c'): 'q2'
  }
  estado_inicial_a = 'q0'
  estados_finais_a = ['q0', 'q2']

  return automato(funcao_transicao_a, estado_inicial_a, estados_finais_a, cadeia)



# LETRA B
def automato_b(cadeia:str):
  estados_b = ['q0','q1','q2','q3','q4','q5','q6','q7']
  alfabeto_b = ['a','b','c']
  funcao_transicao_b={
    ('q0','a'):'q1',
    ('q0','b'):'q4',
    ('q0','c'):'q4',
    ('q1','a'):'q2',
    ('q1','b'):None,
    ('q1','c'):None,
    ('q2','a'):'q3',
    ('q2','b'):None,
    ('q2','c'):None,
    ('q3','a'):None,
    ('q3','b'):'q3',
    ('q3','c'):'q3',
    ('q4','b'):'q4',
    ('q4','c'):'q4',
    ('q4','a'):'q5',
    ('q5','a'):'q6',
    ('q5','b'):None,
    ('q5','c'):None,
    ('q6','a'):'q7',
    ('q6','b'):None,
    ('q6','c'):None   
  }
  estado_inicial_b= 'q0'
  estados_finais_b= ['q3','q7']

  return automato(funcao_transicao_b, estado_inicial_b, estados_finais_b, cadeia)


# LETRA C 

# LETRA D 

def automato_d (cadeia:str):
  estados_d= ['q0','q1','q2','q3']
  alfabeto_d= ['a','b','c']
  funcao_transicao_d= {
      ('q0','a'):'q1',
      ('q0','b'):'q2',
      ('q0','c'):None,
      ('q1','a'):'q1',
      ('q1','b'):'q2',
      ('q1','c'):'q3',
      ('q2','a'):'q3',
      ('q2','b'):'q2',
      ('q2','c'):None,
      ('q3','a'):None,
      ('q3','b'):None,
      ('q3','c'):'q3',
  }
  estado_inicial_d= 'q0'
  estados_finais_d=['q1','q3']
  
  return automato(funcao_transicao_d,estado_inicial_d,estados_finais_d,cadeia)


