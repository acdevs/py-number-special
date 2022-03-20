def sosod(x: int):
    '''sum of squares of digits'''
    s=0
    while x>0:
       d=x%10
       s+=d**2
       x//=10
    return s


def sod(x: int):
    '''sum of digits'''
    s=0
    while x>0:
       d=x%10
       s+=d
       x//=10
    return s



def automorphic(x: int):
    '''An automorphic number is a number which is present in the last digit(s) of its
square. Example: 25 is an automorphic number as its square is 625 and 25 is
present as the last digits'''
    x2=x**2
    while x>0:
        d=x%10
        if d==x2%10:
            pass
        else:
            return False
            break
        x//=10
        x2//=10
    else:
        return True


def neon(x: int):
    '''A number is said to be a Neon Number if the sum of digits of the square of the number is equal to
thenumber itself. Example 9 is a Neon Number. 9*9=81 and 8+1=9.Hence it is a Neon Number.'''
    x2=x**2
    s=0
    while x2>0:
        d=x2%10
        s+=d
        x2//=10
    if s==x:
        return True
    else:
        return False


def magic(x: int):
    '''A number is said to be a Magic number if the sum of its digits are calculated till a single digit is
obtained by recursively adding the sum of its digits. If the single digit comes to be 1 then the
number is a magic number.'''
    m=sod(x)
    if m==1:
        print(True)
    else:
        try:
            magic(m)     #recusrsion
        except:
            print(False)


def palindrome(n: int):
    '''Reverse of a number is also same as the original number.'''
    x=n
    r=i=0
    while x>0:
        d=x%10
        x//=10
        r=r*10+d
        i+=1
    if n==r:
        
        return True
    else:
        return False

    
def taxicab(n: int):
    '''the nth taxicab number, typically denoted Ta(n) or Taxicab(n), also called
the nth Hardy–Ramanujan number is defined as the smallest number that can be expressed as a
sum of two positive cube numbers in n distinct ways.'''
    return 'coming soon'


def armstrong(x: int,order: int =3 ):
    '''A positive integer is called an Armstrong number of order n if abcd… = a + b + c + d + …  to nth power of digits.
In case of an Armstrong number of 3 digits, the sum of cubes of each digits is equal to the number itself.'''
    n=x
    s=0
    while x>0:
        d=x%10
        x//=10
        s+=d**order
    if n==s:
        return True
    else:
        return False

def fact(n : int):
    '''factorial of a number'''
    f=1
    for i in range(1,n+1):
        f*=i
    return f


def strong(x :int):
    '''If the sum of factorial of the digits in any number is equal the given number then the number is
called as STRONG number.'''
    n=x
    s=0
    while x>0:
        d=x%10
        x//=10
        s+=fact(d)
    if n==s:
        return True
    else:
        return False


def perfect(x :int):
    '''a perfect number is a positive integer that is equal to the sum of its proper
positive divisors, that is, the sum of its positive divisors excluding the number itself'''
    s=0
    for i in range(1,x):
        if x%i == 0:
           s+=i
    if x==s:
        return True
    else:
        return False


def happy(x :int):
    '''A happy number is a number defined: Starting with any positive integer,
    replace the number by the sum of the squares of its digits, and repeat the process until the number
    either equals 1(where it will stay), or it loops endlessly in a cycle which does not include 1. Those
    numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are
    unhappy numbers (or sad numbers). '''
    m=sosod(x)
    if m==1:
        print(True)
    else:
        try:
            happy(m)    #recusrsion
        except:
            print(False)


def anagram(*x: tuple):
    '''Two numbers are said to be anagram if the reverse of the number is equal to the original number .'''
    x=list(x)
    t=[]
    n=len(x)
    for i in range(n):
        t.append([])
        while x[i]>0:
            d=x[i]%10
            if d not in t[i]:
                t[i].append(d)
            x[i]//=10
        t[i].sort()
    for i in range(n-1):
        if t[i] == t[i+1]:
            pass
        else:
            return False
            break
    else:
        return True
    
'''done'''
    
    
    
        
        
    
        
