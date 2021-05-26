from add import M

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

def movimento(mt, palavra):
    strip = [*palavra]
    current_state = mt[4]
    final_states = mt[-1]
    pointer = 0
    blank = mt[5]
    qtd_passos = 0

    while current_state not in final_states:
        qtd_passos += 1
        result = delta(mt, current_state, strip[pointer])
        current_state, new_symbol, direction = result

        strip[pointer] = new_symbol
        strip, pointer = move_strip(strip, pointer, direction)

    return strip, pointer, qtd_passos

def read_strip_until_end(strip, pointer, blank='B'):
    strip = strip[pointer:] 

    # limpando a fita dos blanks
    strip = [s for s in strip if s != blank]
    return strip 


