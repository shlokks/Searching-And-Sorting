def matched(s):
   c=0
   for i in range(len(s)):
       if s[i]=="(":
           c=c+1
       if s[i]==")" :
           if c==0:
               return (False)
           else:
               c=c-1
   if c==0:
       return(True)
   else:
       return(False)