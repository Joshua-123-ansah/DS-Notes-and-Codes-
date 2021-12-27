#THE CONCEPT OF MEMIOZATION
def memoFib(n,memo={}):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        if n in memo:
            return memo[n]
        else: 
            result=memoFib(n-1,memo)+memoFib(n-2,memo)
            memo[n]=result
            return result
        
print(memoFib(50))