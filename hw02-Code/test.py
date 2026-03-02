is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
is_positive = lambda x: x > 0
greater_than_three = lambda x: x > 3

def filter_digits(f, n):
    def count_num(n):
        count = 0
        while n != 0:
            count += 1 
            n = n // 10
        return count 
    
    def filter(f,n):
        re = 0
        times = 0
        for i in range(1,count_num(n)+1):
            obj = n % 10
            if f(obj) == 1:
                re = obj*pow(10, times) + re 
                times += 1 
            n = n // 10 
        return re
    return filter(f,n)

print(filter_digits(is_even,14601002))