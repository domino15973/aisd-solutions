import sys
import time


def Hanoi(sour, dest, buff):
    iter = 0
    if (not len(sour) % 2):
        while (True):
            try:
                if (len(sour) and (not len(buff) or sour[-1] < buff[-1])):
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())

                iter += 1

                print(list(sour), list(buff), list(dest))

                if ((not len(dest) or sour[-1] < dest[-1])):
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())

                iter += 1

                print(list(sour), list(buff), list(dest))

                if (dest[-1] < buff[-1]):
                    buff.append(dest.pop())
                else:
                    dest.append(buff.pop())

                iter += 1

                print(list(sour), list(buff), list(dest))
            except IndexError:
                break

    else:
        while (True):
            try:
                if (not len(dest) or sour[-1] < dest[-1]):
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())

                iter += 1

                print(list(sour), list(buff), list(dest))

                if (len(sour) and (not len(buff) or sour[-1] < buff[-1])):
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())

                iter += 1

                print(list(sour), list(buff), list(dest))

                if (buff[-1] < dest[-1]):
                    dest.append(buff.pop())
                else:
                    buff.append(dest.pop())
                iter += 1

                print(list(sour), list(buff), list(dest))
            except IndexError:
                break

    return iter


def main():
    n = int(input('Enter the number of disk: '))
    if n <= 1:
        print('Number of disk must be greater than 1!')
        sys.exit()

    sour = []
    dest = []
    buff = []

    for i in range(n):
        sour.append(n - i)

    t1 = time.time()
    print(list(sour), list(buff), list(dest))
    step = Hanoi(sour, dest, buff)
    t2 = time.time()
    t = t2-t1

    print("Number of moves performed: " + str(step))
    print("Total program time is: " + str(t))


main()
