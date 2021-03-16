import my_module
import sys
print('Please? insert Your Name: ')

i1 = sys.stdin.readline()
print('Yoar insert %s' % i1)

print('Please? insert Your age: ')

i1 = sys.stdin.readline()
print('Yoar insert age %s' % i1)

p = 100
def pab():
  r = 10
  h = 20
  print(p,r,h)
pab()

my_module.podscet_monet_i_ih_ves(100,2.5,1)
my_module.podscet_monet_i_ih_ves(200,5,2)

a1 = 100
b1 = 200
print('Площадь прямоугольника %s на %s равна %s' % (a1,b1,my_module.ploshad_axb(a1,b1)))

for i in range (0,3):
  print('Insert a:')
  a = int(input())
  print('Insert b:')
  b = int(input())
  print('Площадь прямоугольника %s на %s равна %s' % (a,b,my_module.ploshad_axb(a,b)))
