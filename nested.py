def show():

    s = 'nested'

    def add():

        s = 'function'
        print(s)

    add()
    print(s)

show()
