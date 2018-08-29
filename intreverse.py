def intreverse(n):
   
    sum,temp =0,0
    
    while n != 0:
        temp = n%10
        sum = sum*10 + temp
        n = n //10
    return(sum)
    