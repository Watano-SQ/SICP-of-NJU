class Link:
    empty = ()
    def __init__(self,value,next=empty):
        self.val = value
        self.next = next
    
    def sum(self):
        res = 0
        temp = self
        while(temp.next != temp.empty):
            res += temp.val
            temp = temp.next
        res += temp.val
        return res
    
    def display(self):
        temp = self
        str = '< '
        while(temp.next != temp.empty):
            if isinstance(temp.val,int): 
                str += f'{temp.val} '
                temp = temp.next
            elif isinstance(temp.val,Link):
                str += temp.val.display()
                temp = temp.next
        str += f'{temp.val} '
        str += '> '
        return str
    
    def func_rec(self,f):
        if self.next is not self.empty:
            if isinstance(self.val,int):
                value = f(self.val)
                return Link(value,self.next.func_rec(f))
            elif isinstance(self.val,Link):
                return Link(self.val.func_rec(f),self.next.func_rec(f))
        else:
            if isinstance(self.val,int):
                value = f(self.val)
                return Link(value,self.empty)
            elif isinstance(self.val,Link):
                return Link(self.val.func_rec(f),self.empty)
    

    def func_loop(self,f):
        if self.next is not self.empty:
            
            pass
        else:
            pass
    
a = Link(1,Link(3,Link(2,Link(4,Link(7)))))
b = Link(a,Link(3))
print(a.sum())
print(a.func_rec(lambda x: 2*x).display())

    
