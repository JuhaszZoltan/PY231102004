x:int = int(input('x értéke: '))
y:int = int(input('y értéke: '))
print(f'különbség abs: {abs(x - y)}')

a:int = int(input('a értéke: '))
b:int = int(input('b értéke: '))
c:int = int(input('c értéke: '))
if b+c>a and a+c>b and a+b>c: print('szerkeszthető')
else: print('nem szerkeszthető')

nev:str = input('írd be a neved: ')
for k in nev: print(k)

valami:str = input('írj be valamit: ')
print((len(valami)+2) * '*')
print(f'*{valami}*')
print((len(valami)+2) * '*')