from pyexcel_ods3 import save_data
from collections import OrderedDict
from re import search
from descript import descricao

#cada lista é uma linha
linhas = [['Número', 'Bit 0', 'Bit 1', 'Bit 2', 'Bit 3', 'Bit 4', 'Bit 5', 'Bit 6', 'Bit 7', 'Char', 'Observações']]
temp = []
data = OrderedDict()

def add(x):
  temp.append(x)

for x in range(128):
  ascii = chr(x)
  add(x) #número na coluna de título "Número"
  for c in list(str(format(x, "b")).zfill(8)): #cada digito de 8 da versão binária com 0s a esquerda
    add(c)
  if(x == 0 or (x < 14 and x > 6) or x >= 32): #IF 1
    if search('[\0\a\b\t\n\v\f\r]', ascii): #IF 2; tratamento de caractere de escape
      formated = repr(ascii)
      #tradução manual, porque nem tudo vem pronto :/
      if 'x' in formated: #IF 3
        if '00' in formated:
          add(r'\0')
        elif '07' in formated:
          add(r'\a')
        elif '08' in formated:
          add(r'\b')
        elif '0b' in formated:
          add(r'\v')
        elif '0c' in formated:
          add(r'\f')
      else: #IF 3
        add(formated.strip("'"))
    else: #IF 2
      add(ascii)
    if x != 127:
      add(descricao(temp[-1]))
    else:
      add('delete')

  else: #IF 1
    add(' ')
    add('não usamos')
  linhas.append(temp[:])
  temp.clear()

data.update({'Tabela ASCII': linhas})
save_data('teste.ods', data)