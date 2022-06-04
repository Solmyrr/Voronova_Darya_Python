

def itarator_with_yield(n, sum):
    sum = 0
    for num in range(n + 1):
       if num % 2 != 0 and num**2 < 200:
            sum += num
            yield (num, sum)

                # sum1 += num
                # print(sum1)


example = itarator_with_yield(40, sum)