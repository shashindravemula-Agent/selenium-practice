from OOPS import Calculator

class Childimpl(Calculator):

    def completeData(self):
        return self.getdata()

obj = Childimpl()
print(obj.completeData())


