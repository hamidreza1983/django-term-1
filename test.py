
def star(func):
    def wrraper():
        print ("*********")
        func()
        print ("*********")
    return wrraper


@star
def test1():
    print ("this is first number")

@star
def test2():
    print ("this is second number")


@star
def test3():
    print ("this is third number")



test1()
test2()
test3()