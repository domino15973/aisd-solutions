import random
import time


def insertionsort(myList):
    for i in range(len(myList)):
        x = myList[i]
        j = i - 1
        while j >= 0 and myList[j] > x:
            myList[j+1] = myList[j]
            j = j - 1
        myList[j+1] = x


def main():
    times = []
    tc1 = time.time()
    for _ in range(10):
        myList = []
        for i in range(10000):
            x = random.randint(0, 1000)
            myList.append(x)
        t1 = time.time()
        insertionsort(myList)
        print(myList)
        t2 = time.time()
        t = t2 - t1
        times.append(t)
    tc2 = time.time()
    tc = tc2 - tc1
    print('Total time: ', tc)
    print('Slowest time: ', max(times))
    print('Fastest time: ', min(times))
    print('Average time: ', tc / 10)
    print('All times: ', times)


main()
