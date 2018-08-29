def bSearch(seq,x,l,r):
    if r-l == 0:
        return(False)
        
    mid = (l+r)//2
    
    if (x==seq[mid]):
        return(True,mid)
    
    if (x < seq[mid]):
        return(bSearch(seq,x,l,mid))
        
    else:
        return(bSearch(seq,x,mid+1,r))
        
        