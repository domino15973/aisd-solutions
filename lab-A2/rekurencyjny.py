import sys
import time

step = 0


def Hanoi(n, sour, dest, buff):
    global step
    step += 1

    if n == 1:
        dest.append(sour.pop())
        print(list(sour), list(buff), list(dest))
    else:
        Hanoi(n-1, sour, buff, dest)
        dest.append(sour.pop())
        print(list(sour), list(buff), list(dest))
        Hanoi(n-1, buff, dest, sour)


def main():
    n = int(input('Enter the number of disk: '))
    if n <= 1:
        print('Number of disk must be greater than 1!')
        sys.exit()

    sour = ["sour"]
    dest = ['dest']
    buff = ['buff']

    for i in range(n):
        sour.append(n - i)

    t1 = time.time()
    print(list(sour), list(buff), list(dest))
    Hanoi(n, sour, dest, buff)
    t2 = time.time()
    t = t2-t1

    print("Number of moves performed: " + str(step))
    print("Total program time is: " + str(t))


main()
