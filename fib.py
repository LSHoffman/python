fib_list = []
evens_list = []
i = 0


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

n_list = list(range(1,1000))

while F(n_list[i]) < 4000000:
    fib_list.append(F(n_list[i]))
    i += 1
    
for number in fib_list:
    if number % 2 == 0:
        evens_list.append(number)
        
print(sum(evens_list))
        



