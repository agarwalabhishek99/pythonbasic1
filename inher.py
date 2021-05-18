class System:
    def systemMethod(self):
        print("system method")

class User(System):
    def userMethod(self):
        print("User Method")

class Info(User):
    def infoMethod(self):
        print("info method")

i = Info()
i.systemMethod()
i.userMethod()
i.infoMethod()