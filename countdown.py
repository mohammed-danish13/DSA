def countdown(n,limit):
    if n>limit:
        return
    
    print(n)
    countdown(n+1,limit)
    
countdown(1,10)