from operator import add, mul, mod
def lambda_curry2(func):
    def curried_func(k):
        def add_k(x):
            return func(x,k) #反了
        return add_k
    return curried_func

def count_cond(condition):
    def traverse(n):
        sum = 0
        for i in range(1,n+1):
            sum += condition(n,i)
        return sum
    return (lambda n:traverse(n))
    

trigger(n):   n = 0 ? 0 : 1
sum(n,f):  f0 + f1 +f2 +... +fn 
product(n,f):  f0 * f1 * f2 * ... * fn 
product_of_trigger:  if have root? 0 : 1 

minimal_root:  
    num_of_root = num_of_(f_i=0) = n - num_of_(trigger(f_i=1)) = n - sum(n,trigger(f(i)))
    if num_of_root == 0 that is  product_of_trigger == 1 : return n + product_of_trigger + t*num_of_root # ok
    elif num_of_root != 0 that is product_of_trigger == 0 : return minimal_root == n + product_of_trigger - t*num_of_root(whose product_of_trigger == 1 and who + 1 product_of_trigger == 0)

    how to t?
t(whose product_of_trigger == 1 and who + 1 product_of_trigger == 0)

# 取反！！！
trigger(n):   n = 0 ? 0 : 1
sum(n,f):  f0 + f1 +f2 +... +fn 
product(n,f):  f0 * f1 * f2 * ... * fn 
product_of_trigger:  if have root? 0 : 1 

minimal_root:  
    num_of_root = num_of_(f_i=0) = n - num_of_(trigger(f_i=1)) = n - sum(n,trigger(f(i)))
    if num_of_root == 0 that is  product_of_trigger == 1 : return n + product_of_trigger + t*num_of_root # ok
    elif num_of_root != 0 that is product_of_trigger == 0 : return minimal_root == n + product_of_trigger - t*num_of_root(whose product_of_trigger == 1 and who + 1 product_of_trigger == 0)

    how to t?
t(whose product_of_trigger == 1 and who + 1 product_of_trigger == 0)

# 取反！！！