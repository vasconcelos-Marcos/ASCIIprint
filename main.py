from pyexcel_ods3 import save_data
from collections import OrderedDict
from re import search

lista = [['Numero', 'Bit 0', 'Bit 1', 'Bit 2', 'Bit 3', 'Bit 4', 'Bit 5', 'Bit 6', 'Bit 7', 'Char', 'Observações']]
temp = []
data = OrderedDict()

for x in range(128):
    temp.append(x)
    for c in list(str(format(x, "b")).zfill(8)):
      temp.append(c)
    if search('[\0\a\b\t\n\v\f\r]', chr(x)):
      temp.append(f'\\{chr(x)}')
    else:
      temp.append(chr(x))
    lista.append(temp[:])
    temp.clear()

data.update({'Tabela ASCII': lista})
save_data('teste.ods', data)