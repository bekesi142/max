'''Random lista generálás'''
import random
lista=[]
for i in range(6):
    lista.append(random.randint(1,10))
print('lista:',lista)

'''Maximumkiválasztásos rendezés'''

def kivalasztasos_rendezes(tomb):
   for i, item_at_i in enumerate(tomb):
      min_index = i
      min_value = item_at_i
      for j, item_at_j in enumerate(tomb[i+1:],i+1):
         if item_at_j < min_value:
            min_index = j
            min_value = item_at_j
      tomb[i] = min_value
      tomb[min_index] = item_at_i
      print(tomb)
kivalasztasos_rendezes(lista)
