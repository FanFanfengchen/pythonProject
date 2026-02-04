def fire(n,c=1):
    if not isinstance(n,int) or not isinstance(c,int):
        raise TypeError("bv")
    if n < 1 or c < 1 or c > n:
        raise ValueError("bv")
    for current in range(c,n+1):
        spaces = ' ' * (n-current)
        stars = '*' * (2*current-1)
        print(spaces + stars)
fire(10)


