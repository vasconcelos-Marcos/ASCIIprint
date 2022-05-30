dicio = {
    r'\0': 'byte nulo',
    r'\a': 'apito',
    r'\b': 'backspace',
    r'\t': 'tabulação',
    r'\n': 'fim da linha',
    r'\v': 'tabulação vertical',
    r'\f': 'fim de página',
    r'\r': 'carriage return',
    ' ': 'espaço',
    '!': 'exclamação',
    '"': 'aspas',
    '#': 'cerquilha',
    '$': 'cifrão',
    '%': 'percentagem',
    '&': 'ampersand',
    "'": 'apóstrofe',
    '(': 'abre parênteses',
    ')': 'fecha parênteses',
    '*': 'asterisco',
    '+': 'adição',
    ',': 'vírgula',
    '-': 'hífen',
    '.': 'ponto',
    '/': 'barra',
    ':': 'dois pontos',
    ';': 'ponto e vírgula',
    '<': 'menor',
    '=': 'igual',
    '>': 'maior',
    '?': 'interrogação',
    '@': 'arroba',
    '[': 'abre colchete',
    '\\': 'contra barra',
    ']': 'fecha colchete',
    '^': 'circunflexo',
    '_': 'underscore',
    '`': 'apóstrofe esquerda',
    '{': 'abre chave',
    '|': 'barra vertical',
    '}': 'fecha chave',
    '~': 'til'
}


def descricao(caractere):
    if caractere in dicio:
        return dicio[caractere]
    return ' '