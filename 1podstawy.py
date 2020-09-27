print("test")
print(8)

x=10.234
print(x)
print("{:.2f}".format(x))

#potegowanie
pow=2**10
print(pow)

'''
pobieranie danych
'''


name1=input("Podaj imie: ")
surname1=input("Podaj swoje nazwisko: ")
wiek1=input("Podaj wiek: ")

print("Twoje imie: " + name1 + ", nazwisko " + surname1 + " " + str(wiek1))


print("\nPodaj swoj wiek: ",end="")
age=input()


surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)

lastLetter1=surname[len(surname) -1]
lastLetter2=surname[-1]
print(lastLetter1)
print(lastLetter2)


x="5"
print(type(x))

y=4
print(type(y))
y=y/2
print(type(y))


surname="Kowalski"
print()
print(surname[0])#K
print(surname[0:3])#Kow
print(surname[-2])#k
print(surname[-2:])#ki
print(surname[:-2])#Kowals
print(surname[:-2:2])#Kwl do 2 od końca, co 2 znak