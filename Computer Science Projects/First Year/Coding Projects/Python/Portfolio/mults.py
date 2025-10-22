def count_multiples(n,numlist):
    i = 0
    j = 0
    mult = len(numlist)
    while i < mult:
        a = numlist[i]
        if a%n == 0:
            j+=1
        i+=1
    return j
if __name__ == "__main__":
    test = count_multiples(2, [25, 5, 1, 10, 3, 7])
    print(test)
