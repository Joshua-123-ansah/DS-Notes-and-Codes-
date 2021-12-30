#WHENEVER YOU ARE DOING A RECURSIVE PROBLEMM THERE ARE TWO THINGS YOU WOULD HAVE TO CONSIDER.
#THAT IS THE BASE BASE CASE AND THE RECURRESSION 

#BELOW IS A SIMPLE EXAMPLE OF A RECUSRSIVE PROBLEM. THAT Given n, calculate the total number of 1 to n.


def total(n):
    #In this case this is our base case
    output =0
    if n==1:
        return 1
    output += total(n-1)+n
    return output
print(total(500))