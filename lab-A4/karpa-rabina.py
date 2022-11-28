# d is the number of characters in the input alphabet
# q - prime number

def rabin_karp_matcher_horizontal(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    result = set()
    for x in range(n - 2):
        p = 0
        t = 0

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[x][i])) % q
        for y in range(n - m + 1):
            if p == t:
                found = True
                for i in range(m):
                    if (lines[x][y + i] != pattern[i]):
                        found = False
                        break
                if found:
                    result.add((x, y))
            if y < n - m:
                t = ((t - h * ord(text[x][y])) * d + ord(text[x][y + m])) % q
    return result


def rabin_karp_matcher_vertical(text, pattern, d, q, result):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q

    final_result = set()

    for x in range(n - 2):
        p = 0
        t = 0
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i][x])) % q
        for y in range(n - m + 1):
            if p == t:
                found = True
                for i in range(m):
                    if (lines[y + i][x] != pattern[i]):
                        found = False
                        break
                if found and (y, x) in result:
                    final_result.add((y, x))
            if y < n - m:
                t = ((t - h * ord(text[y][x])) * d + ord(text[y + m][x])) % q

    return final_result


def rabin_karp_matcher(array, string):
    results_horizontal = rabin_karp_matcher_horizontal(array, string, 256, 101)
    results = rabin_karp_matcher_vertical(array, string, 256, 101, results_horizontal)
    return results


with open('patterns/patterns/1000_pattern.txt') as txt:
    lines = [line for line in txt]

results = rabin_karp_matcher(lines, "ABC")

print("Found " + str(len(results)) + " patterns")
print(results)
