x=6

if x==5:
  print("x jest równe 5")
else:
  print("x nie jest równe 5")
  print("x jest równe: ", x)

y=False
if y:
  print('prawda')
else:
  print('fałsz')

k=input('Podaj k:')
if bool(k):
  print('k zawiera dane: ',k)
else:
  print('k nie zawiera danych')

'''
  Użytkownik podaje 3 wartości z klawiatury: x, y, z
  wyświetl, któa z tych zmiennych będzie największa
  wykorzystaj instrukcję warunkową
'''

x=input('Podaj wartość: ')
y=input('Podaj wartość: ')
z=input('Podaj wartość: ')

if((x>y and x>z) and (x != y and x != z)):
    print("x jest najwieksze i wynosi", x)
elif((y>x and y>z) and (y != x and y != z)):
    print("y jest najwieksze i wynosi", y)
elif((z>x and z>y) and (z != x and z != y)):
    print("z jest najwieksze i wynosi", z)