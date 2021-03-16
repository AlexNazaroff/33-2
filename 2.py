from my_module import *


p = 100
def pab():
  r = 10
  h = 20
  print(p,r,h)
pab()


podscet_monet_i_ih_ves(100,2.5,1)
podscet_monet_i_ih_ves(200,5,2)



a1 = 100
b1 = 200
print('Площадь прямоугольника %s на %s равна %s' % (a1,b1,ploshad_axb(a1,b1)))

for i in range (0,3):
  print('Insert a:')
  a = int(input())
  print('Insert b:')
  b = int(input())
  print('Площадь прямоугольника %s на %s равна %s' % (a,b,ploshad_axb(a,b)))