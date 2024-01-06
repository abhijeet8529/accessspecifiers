def boxprint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("sysmol should be atleast single str")
    if width <= 2:
        raise Exception("width must be greater than 2")
    if height <= 2 :
        raise Exception("height must be greater than 2")

        
    print(symbol * width)
    for i in range(height- 2):
        print(symbol+ (' '* (width -2 )) + symbol)  
    print(symbol * width)
        
for s , w ,h in (('+', 4, 4), ('O', 20, 5), ('~', 13, 3), ('ZZ', 3, 3)):
    try:
        boxprint(s,w,h)
    except Exception as err:
        print('an exception happend : ' +str(err))