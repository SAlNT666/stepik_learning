from re import findall


print(len(findall(r'(?m)^.*bee.*bee.*$', s := open(0).read())), 
      len(findall(r'(?m)^.*\bgeek\b.*$', s)), sep='\n')
