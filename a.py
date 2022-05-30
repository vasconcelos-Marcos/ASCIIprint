from re import search
for x in range(128):
  if (x == 0 or (x < 14 and x > 6) or x >= 32):
    if search(r'[\0\a\b\t\n\v\f\r]', chr(x)):
      a = repr(chr(x))
      if 'x' in a:
        if '00' in a:
          print(r'\0')
        if '07' in a:
          print(r'\a')
        if '08' in a:
          print(r'\b')
        if '0b' in a:
          print(r'\v')
        if '0c' in a:
          print(r'\f')
      else:
        print(a)
    else:
      print(f'{chr(x)}')
  else:
    print('vazio!')