def check():
    #global allow me to change the value on line 6
    global g
    x, y = 0,1
    print("inside the func , g = " + g)
    g = str(11)
    print("after inc. g = "  + g)

g = str(10)
check()
print(g)


def f(): 
    """Testing only
    when we dont need to change the values of gv
    we dont need to specify "global" keyword.
    """

    print( "dd" + s)
s = "I love Paris in the summer!"
f()
