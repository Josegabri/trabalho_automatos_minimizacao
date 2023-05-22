# Função que define o automato 

def automato_1(funcao_transicao,q0,conj_est_finais, cadeia):
    '''
      Gerador de automato 
      Args: 
        Transições presentes no automato -> um dicionario com strings. Tendo do lado direito o estado e o simbolo a ser analisado.
        lado esquerdo, para qual estado irá. 

        q0 -> estado inicial do automato

        Estados finais do automato -> string

        cadeia -> sequencia de string a ser analizada pelo automato criado

      Return:
        Print com a ilustração da ocorrência das transições 
        
        Valor booleano para a validação da cadeia para com o automato 
    '''
    estado_atual=q0
    for simbolo in cadeia:
        print(f'({estado_atual}, {simbolo}) ---> {funcao_transicao.get((estado_atual, simbolo))}')
        estado_atual=funcao_transicao.get((estado_atual, simbolo))
        if estado_atual == None:
            break
    return estado_atual in conj_est_finais
  
# LETRA A 
def automato_a(cadeia:str):
  '''
   Validação de cadeia no automato da primeira questão, letra A
   É usado uma chamada de outra função (automato_1), para a criação do automato,
   sendo passado o automato desenvolvido para a alternativa
   
   Args: 
    cadeia de string a ser analizada no automato criado

   Return: 
    Return da função automato. Print da transições utilizadas.
    Valor booleano da validação da cadeia.
  '''
  estados_a = ['q0', 'q1', 'q2']
  alfabeto_a = ['a', 'b', 'c']
  funcao_transicao_a = {
    ('q0', 'a'): 'q1',
    ('q1', 'b'): 'q1',
    ('q1', 'c'): 'q2',
    ('q2', 'c'): 'q2'
  }
  estado_inicial_a = 'q0'
  estados_finais_a = ['q0', 'q1', 'q2']

  return automato_1(funcao_transicao_a, estado_inicial_a, estados_finais_a, cadeia)



# LETRA B
def automato_b(cadeia:str):
  '''
   Validação de cadeia no automato da primeira questão, letra B
   É usado uma chamada de outra função (automato_1), para a criação do automato,
   sendo passado o automato desenvolvido para a alternativa
   
   Args: 
    cadeia de string a ser analizada no automato criado

   Return: 
    Return da função automato. Print da transições utilizadas.
    Valor booleano da validação da cadeia.
  '''
  estados_b = ['q0','q1','q2','q3','q4','q5','q6','q7']
  alfabeto_b = ['a','b','c']
  funcao_transicao_b={
    ('q0','a'):'q1',
    ('q0','b'):'q4',
    ('q0','c'):'q4',
    ('q1','a'):'q2',
    ('q2','a'):'q3',
    ('q3','b'):'q3',
    ('q3','c'):'q3',
    ('q4','b'):'q4',
    ('q4','c'):'q4',
    ('q4','a'):'q5',
    ('q5','a'):'q6',
    ('q6','a'):'q7',  
  }
  estado_inicial_b= 'q0'
  estados_finais_b= ['q3','q7']

  return automato_1(funcao_transicao_b, estado_inicial_b, estados_finais_b, cadeia)


# LETRA C 

def automato_c(cadeia:str):
  '''
   Validação de cadeia no automato da primeira questão, letra C
   É usado uma chamada de outra função (automato_1), para a criação do automato,
   sendo passado o automato desenvolvido para a alternativa
   
   Args: 
    cadeia de string a ser analizada no automato criado

   Return: 
    Return da função automato. Print da transições utilizadas.
    Valor booleano da validação da cadeia.
  '''
  estados_c = ['q0','q1','q2','q3','q4','q5']
  alfabeto_c = ['a','b']
  funcao_transicao_c={
    ('q0','a'):'q1',
    ('q0','b'):'q3',
    ('q1','a'):'q2',
    ('q1','b'):'q4',
    ('q2','b'):'q3',
    ('q2','a'):'q2',
    ('q4','b'):'q5',
    ('q5','b'):'q5',  
  }
  estado_inicial_c= 'q0'
  estados_finais_c= ['q1','q3','q4','q5']

  return automato_1(funcao_transicao_c,estado_inicial_c,estados_finais_c,cadeia)


# LETRA D 

def automato_d (cadeia:str):
  '''
   Validação de cadeia no automato da primeira questão, letra D
   É usado uma chamada de outra função (automato_1), para a criação do automato,
   sendo passado o automato desenvolvido para a alternativa
   
   Args: 
    cadeia de string a ser analizada no automato criado

   Return: 
    Return da função automato. Print da transições utilizadas.
    Valor booleano da validação da cadeia.
  '''
  estados_d= ['q0','q1','q2','q3']
  alfabeto_d= ['a','b','c']
  funcao_transicao_d= {
      ('q0','a'):'q1',
      ('q0','b'):'q2',
      ('q1','a'):'q1',
      ('q1','b'):'q2',
      ('q1','c'):'q3',
      ('q2','a'):'q3',
      ('q2','b'):'q2',
      ('q3','c'):'q3',
  }
  estado_inicial_d= 'q0'
  estados_finais_d=['q1','q3']
  
  return automato_1(funcao_transicao_d,estado_inicial_d,estados_finais_d,cadeia)



