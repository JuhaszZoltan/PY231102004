from module import *

# valami:str = input('írj be egy szót: ')
# print(keretez(valami))

# szavak:list[str] = ['cica', 'kutya', 'nokedli', 'korbács']
# for szo in szavak: print(keretez(szo) + '\n')

a:int = int(input('a oldal hossza (cm): '))
b:int = int(input('b oldal hossza (cm): '))
c:int = int(input('c oldal hossza (cm): '))
if szerkesztheto_e(a, b, c):
    print('szerkeszthető')
else: print('nem szerkeszthető')