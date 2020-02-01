def maior_primo(x):
    div = 2
    e_primo = True
    primo_k = 0
    primo_a = 0
    final = 0
    while primo_k < x:
       if e_primo == True and primo_k != 1:
         final = primo_a
       div = 2
       primo_k = primo_k + 1
       primo_a = primo_k
       e_primo = True
       while div < primo_k and e_primo:
          if primo_k % div == 0:
            e_primo = False
          div = div + 1
    if e_primo == True:
       return primo_k
    else:
       return final
