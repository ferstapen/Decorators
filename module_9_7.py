def is_prime(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        prime = True
        for i in range(2, a):
            if a % i == 0:
                prime = False
                break
        if prime:
            print('Простое')   
        else:
            print('Составное') 
        return a
    return wrapper            

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
