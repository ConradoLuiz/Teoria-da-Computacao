from add import M
from main import movimento, read_strip_until_end

for i in range(2):
    for j in range(2):

        # Tranformando os indices para binário (tipo string)
        n1 = bin(i)
        n2 = bin(j)

        # Montando a fita inicial
        fita = [*n1[2:], '+', *n2[2:]]
        
        # Calculado o resultado esperado e transformando para binário
        result = bin(i + j)[2:]

        # Computando a resposta com a MT
        fita_resultante, ponteiro = movimento(M, fita)

        # Lendo a resposta da fita e juntando numa string para comparar
        result_mt = ''.join(read_strip_until_end(fita_resultante, ponteiro))

        # Criando a função de teste parametrizada
        test_name = f'test_{i}_{j}'
        exec(
            f"""def {test_name}(): assert {result} == {result_mt}"""
        )

