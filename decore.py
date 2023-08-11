def hello(func):
    def bm(name):
        if name=="sunny":
            print('Hello Sunny bad morning ')
        else:
            func(name)
    return bm
    


@hello 
def wish(name):
    print("Hello",name,"good morning")


wish("suny")