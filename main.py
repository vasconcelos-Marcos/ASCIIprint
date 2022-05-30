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
    #adicionando a coluna de descrição
    if x != 127:
      add(descricao(temp[-1]))
    else:
      add('delete')
  else: #IF 1; espaços vazios e descrição
    add(' ')
    add('não usamos')
  #enfim adicionamos a lista temp como se fosse uma linha e depois limpamos ela
  linhas.append(temp[:])
  temp.clear()
  
#agora é só colocar no congelador
data.update({'Tabela ASCII': linhas}) #como na biblioteca que usei é necessário passar um dicionário como parâmetro,
#eu estou passando minha lista de listas como valor da chave 'Tabela ASCII' que logo mais séra o título da nossa planilha

#e tá pronto o sorvetinho
save_data('teste.ods', data)