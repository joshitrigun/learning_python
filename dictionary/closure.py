def Closure():
    msg = 'Hello'
    def display():
        print("*" * 10)
        print(msg)
        print("*" * 10)
    return display

Closure()()
