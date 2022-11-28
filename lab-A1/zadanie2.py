import random
import time


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


def main():
    times = []
    tc1 = time.time()
    for _ in range(10):
        myList = []
        for i in range(10000):
            x = random.randint(0, 1000)
            myList.append(x)
        t1 = time.time()
        mergeSort(myList)
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
