class Gen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if Gen.current < self.last:
            num = Gen.current
            Gen.current += 1
            return num


def fib(num):
    current = 0
    l_num = 0
    for x in range(num):
        if x == 0:
            print(f'Fibanacci[{x}] is 0')
        elif x == 1:
            current = x
            print(f'Fibanacci[{x}] is 1')
        else:
            new = l_num + current
            print(f'Fibanacci[{x}] is {new}')
            l_num = current
            current = new 

fib(21)