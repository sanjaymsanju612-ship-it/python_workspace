class Batsman:
    def bat(self):
        print("good in batting")

class Bowler:
    def bawl(self):
        print("good in bowling")
    
    
class AllRounder(Batsman,Bowler):
    def field(self):
        print("good in both battimg and bowling")

A= AllRounder()
A.field()
A.bat()
A.bawl()
print(AllRounder.__mro__)