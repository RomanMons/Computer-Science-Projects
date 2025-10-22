def function(n,a):
    i = 1
    h = 1
    while i < n:
        i = i+1
        h = a*h+1
    return h

print(function(6,2))
