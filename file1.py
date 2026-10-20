class Batsman:
    def bat(self):
        print("good in bat")
        
class Bowler:
    def bowl(self):
        print("good in bowling")

class Allorownder(Batsman,Bowler):
    def both(self):
        print("good in both bat and bowl")
    
a1 = Allorownder()
a1.both()
a1.bat()
        