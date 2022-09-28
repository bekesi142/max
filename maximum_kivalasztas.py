'''Random lista generálás'''
import random
lista=[]
for i in range(6):
    lista.append(random.randint(1,10))
print('lista:',lista)

'''Maximumkiválasztásos rendezés'''

def kivalasztasos_rendezes(tomb):
   for i, elem_i in enumerate(tomb):
      max_index = i
      max_ertek = elem_i
      for j, elem_j in enumerate(tomb[i+1:],i+1):
         if elem_j > max_ertek:
            max_index = j
            max_ertek = elem_j
      tomb[i] = max_ertek
      tomb[max_index] = elem_i
      print(tomb)
kivalasztasos_rendezes(lista)
