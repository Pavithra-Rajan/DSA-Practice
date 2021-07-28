from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    ls=Counter(ar)
    ret=0
    for i in ls.values():
        if i>1:
            ret+=i//2
    return ret
