#Joel Chenoweth
#1-26-20
#the project is math fibonnacci sequence
def fib(n):
        """returns the positive integer into the sequence position"""
        if n <= 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
term = 0
term = fib(17)

#print(term)


