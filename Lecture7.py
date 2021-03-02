"""
Lec 7 while loop
"""

i = 5
while i >=0:
    
    try:
        print(1/(i-3))
    except:
        pass
    i = i-1
    if i == 3:
        pass
    
    print(i)
    
#try:
#    print(1/0)
#except ZeroDivisionError:
#   print('zero division error')
    
#except:
#    print('other errors')