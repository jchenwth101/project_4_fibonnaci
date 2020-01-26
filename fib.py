#this is my header.  there are many like it but this one is mine.  Joel Chenoweth
#the year of our lord 2020, the month of January, day 26
#the project is math fibonnacci sequence called without recursion
def fib(n):
        """returns the positive integer into the sequence position"""
        if n <= 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
term = 0
term = fib(17)

#print(term)


