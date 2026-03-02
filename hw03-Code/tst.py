
def pingpong(n):
    def contain_six(n):
        if n == 0:
            return 0
        if (n%10 != 6):
            return contain_six(n//10)
        else:
            return True
    def return_num(i,current_term,total_sum):
        if i > n:
            return total_sum
        next_term = -current_term if contain_six(i) or (i%6)==0 else current_term
        return return_num(i+1,next_term,total_sum+current_term)
    return return_num(1,1,0)


print(pingpong(100))