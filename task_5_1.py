

def itarator_without_yield(n):
     gen1 = (num for num in range(n + 1) if num % 2 != 0)
     while True:
         print(next(gen1))



prob = itarator_without_yield(25)



