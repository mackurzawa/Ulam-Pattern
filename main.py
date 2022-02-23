import sys
from math import ceil
from numpy import array, set_printoptions, inf
import pygame


def isPrime(num):
    return (0, 0, 0) if num in primes else (255, 255, 255)

max_number = 169
side = ceil(max_number**.5)//2*2+1
side = 201

primes = [i+1 for i in range(side**2)]
del primes[0]

i = 0
while i < len(primes):
    cur_prime = primes[i]
    while cur_prime <= side**2:
        cur_prime += primes[i]
        if cur_prime in primes:
            primes.remove(cur_prime)
    i += 1

        



cur_x = side//2
cur_y = side//2
cur_num = 1

li = [[0 for _ in range(side)] for _ in range(side)]
li[cur_x][cur_y] = 1
cur_num += 1

for i in range(side//2):
    for j in range(2*i+1):
        cur_y += 1
        li[cur_x][cur_y] = cur_num
        cur_num += 1
    for j in range(2*i+1):
        cur_x -= 1
        li[cur_x][cur_y] = cur_num
        cur_num += 1
    for j in range(2*i+2):
        cur_y -= 1
        li[cur_x][cur_y] = cur_num
        cur_num += 1
    for j in range(2*i+2):
        cur_x += 1
        li[cur_x][cur_y] = cur_num
        cur_num += 1

for i in range(side-1):
    cur_y += 1
    li[cur_x][cur_y] = cur_num
    cur_num += 1

s_width = 1200
s_width = s_width//side*side
screen = pygame.display.set_mode((s_width, s_width))
pygame.display.set_caption(f'Ulam Pattern with array {side}x{side}')



screen.fill((255, 255, 255))
square_side = s_width/side

for i in range(side):
    for j in range(side):
        print(li[j][i])
        pygame.draw.rect(screen, isPrime(li[j][i]), pygame.Rect(int(i*square_side), int(j*square_side), int(square_side), int(square_side)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

set_printoptions(linewidth=inf, threshold=sys.maxsize)
print(array(li))
input()




