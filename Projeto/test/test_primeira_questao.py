from Projeto.Questao_1 import primeira_questao

# TESTE LETRA A 

def test_valida_a_1():
    teste= 'abbbc'
    assert primeira_questao.automato_a(teste)

def test_valida_a_2():
    teste= 'a'
    assert primeira_questao.automato_a(teste)

def test_valida_a_3():
    teste= 'ab'
    assert primeira_questao.automato_a(teste)

def test_valida_a_4():
    teste= 'abc'
    assert primeira_questao.automato_a(teste)

def test_valida_a_5():
    teste= ''
    assert primeira_questao.automato_a(teste)

def test_valida_a_6():
    teste= 'abcabcabcabcabc'
    assert primeira_questao.automato_a(teste)

def test_valida_a_7():
    teste= 'abbbbbbbbcccccabbbbbbbbccccc'
    assert primeira_questao.automato_a(teste)

def test_valida_a_8():
    teste= 'abababababab'
    assert primeira_questao.automato_a(teste)

def test_valida_a_9():
    teste= 'abbbbbabbbbbabbbbbabbbbb'
    assert primeira_questao.automato_a(teste)

def test_valida_a_10():
    teste= 'aaaaaaaa'
    assert primeira_questao.automato_a(teste)

def test_valida_a_11():
    teste= 'acccccacccccacccccaccccc'
    assert primeira_questao.automato_a(teste)

def test_valida_a_12():
    teste= 'acacacacacacacac'
    assert primeira_questao.automato_a(teste)

def test_valida_a_13():
    teste= 'acbacbacbacbacbacb'
    assert primeira_questao.automato_a(teste)

def test_valida_a_14():
    teste= 'acccccbbbacccccbbb'
    assert primeira_questao.automato_a(teste)

def test_valida_a_15():
    teste= 'acb'
    assert primeira_questao.automato_a(teste)

# TESTE LETRA B

def test_valida_b_1():
    teste= 'aaab'
    assert primeira_questao.automato_b(teste)

def test_valida_b_2():
    teste= 'aaac'
    assert primeira_questao.automato_b(teste)

def test_valida_b_3():
    teste= 'aaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_4():
    teste= 'aaabbbb'
    assert primeira_questao.automato_b(teste)

def test_valida_b_5():
    teste= 'aaaccc'
    assert primeira_questao.automato_b(teste)

def test_valida_b_6():
    teste= 'baaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_7():
    teste= 'caaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_8():
    teste= 'bbbbbbbbbbaaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_9():
    teste= 'ccccccccaaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_10():
    teste= 'aaabbbbbbbb'
    assert primeira_questao.automato_b(teste)

def test_valida_b_11():
    teste= 'aaacccccccccccccccccccc'
    assert primeira_questao.automato_b(teste)

def test_valida_b_12():
    teste= 'bbbbbbbbbbbbbbbbbbbbbbbaaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_13():
    teste= 'cccccccccccccccccccaaa'
    assert primeira_questao.automato_b(teste)

def test_valida_b_14():
    teste= 'aaabbbbbbbbbbbbbbbbbbbbbbbbbbbb'
    assert primeira_questao.automato_b(teste)

def test_valida_b_15():
    teste= 'aaacccccccccccccccccccccccc'
    assert primeira_questao.automato_b(teste)

# TESTE LETRA C 

def test_valida_c_1():
    teste='ab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_2():
    teste='b'
    assert primeira_questao.automato_c(teste)

def test_valida_c_3():
    teste='ab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_4():
    teste='abababababababababab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_5():
    teste='aab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_6():
    teste='abab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_7():
    teste='aaaaaaaab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_8():
    teste='ababababab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_9():
    teste='aaaaaaaaaaab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_10():
    teste='ababababababababababababababababababababab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_11():
    teste='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_12():
    teste='ababababababababababababababababababababababababab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_13():
    teste='aaaaab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_14():
    teste='ababababab'
    assert primeira_questao.automato_c(teste)

def test_valida_c_15():
    teste='aaaaaaaaab'
    assert primeira_questao.automato_c(teste)

# TESTE LETRA D 

def test_valida_d_1():
    teste='a'
    assert primeira_questao.automato_d(teste)

def test_valida_d_2():
    teste='ac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_3():
    teste='acac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_4():
    teste='aba'
    assert primeira_questao.automato_d(teste)

def test_valida_d_5():
    teste='abac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_6():
    teste='aacacacacacacac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_7():
    teste='bacacacacacac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_8():
    teste='aaaaaaaaaaa'
    assert primeira_questao.automato_d(teste)

def test_valida_d_9():
    teste='bbbbbbbbbbba'
    assert primeira_questao.automato_d(teste)

def test_valida_d_10():
    teste='aaaaaaaaaaaaaaaabbbbbbbbbbba'
    assert primeira_questao.automato_d(teste)

def test_valida_d_11():
    teste='aaaaaaaaaaac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_12():
    teste='bbbbbbbbbbbac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_13():
    teste='aaaaaaaaaaaaaaaaabbbbbbbbbbbbac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_14():
    teste='aaaaaaaaaaaaabbbbbbbbbbbbacacacacacac'
    assert primeira_questao.automato_d(teste)

def test_valida_d_15():
    teste='acacacacacac'
    assert primeira_questao.automato_d(teste)

