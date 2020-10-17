"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""


def both_ends(s):
    # +++ SUA SOLUÇÃO +++

    #return f"{'' if len(s) < 3 else '%s%s' % (s[:2], s[len(s)-2:])}"

   # if len(s) < 3:
   #     return ''
   # else:
   #     return '%s%s' % (s[:2], s[len(s)-2:])

    cont_incial = 0
    new_string = ''
    cont_final = len(s)
    while True:
        if cont_final < 2:
            return ''
        if cont_incial < 2:
            new_string += s[cont_incial]
        if cont_incial >= cont_final - 2:
            new_string += s[cont_incial]
        cont_incial += 1
        if cont_incial == cont_final:
            return new_string


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
