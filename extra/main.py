# from increment import M
from statsmodels import regression
from add import M
from functools import wraps
from time import time
import matplotlib.pyplot as plt
import statsmodels.api as sm

timings = []

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        timings.append(te-ts)
        # print ('func:%r args:[%r, %r] took: %2.4f sec' % \
        #   (f.__name__, args, kw, te-ts))
        return result
    return wrap

def delta(mt, estado, simbolo):
    try:
        prox_estado, novo_simbolo, direcao = mt[3][(estado,simbolo)]
        return prox_estado, novo_simbolo, direcao
    except:
        return(None,None,None)

def move_strip(strip, pointer, direction, blank='B'):
    new_strip = strip
    new_pointer = pointer

    if direction == 'L':
        new_pointer = pointer - 1
        if new_pointer < 0:
            new_pointer = 0
            new_strip = [blank, *strip]
    
    if direction == 'R':
        new_pointer = pointer + 1
        if new_pointer >= len(strip):
            new_strip = [*strip, blank]
    
    return new_strip, new_pointer

@timing
def movimento(mt, palavra):
    strip = [*palavra]
    current_state = mt[4]
    final_states = mt[-1]
    pointer = 0
    blank = mt[5]
    i = 0
    while current_state not in final_states:
        result = delta(mt, current_state, strip[pointer])
        current_state, new_symbol, direction = result

        strip[pointer] = new_symbol
        strip, pointer = move_strip(strip, pointer, direction)

        # print(strip)
        i += 1
        # if i > 10:
        #     exit()

    return strip, pointer

def read_strip_until_end(strip, pointer, blank='B'):
    strip = strip[pointer:] 

    # limpando a fita dos blanks
    strip = [s for s in strip if s != blank]
    return strip

if __name__ == '__main__':
    
    n_sucesso = 0
    len_palavras = []

    for i in range(20):
        for j in range(20):
            n1 = bin(i)
            n2 = bin(j)
            fita = [*n1[2:], '+', *n2[2:]]
            len_palavras.append(len(fita))
            result = bin(i + j)[2:]

            fita_resultante, ponteiro = movimento(M, fita)

            result_mt = ''.join(read_strip_until_end(fita_resultante, ponteiro))

            print(n_sucesso)
            if result == result_mt:
                print('Sucesso')
                n_sucesso += 1

    X = sm.add_constant(len_palavras)
    model = sm.OLS(timings, X)
    result = model.fit()

    line = [result.params[0] + result.params[1]*len_palavra for len_palavra in len_palavras]

    plt.plot(len_palavras, line)
    plt.scatter(len_palavras, timings)
    plt.show()    



