# class Player():
#     def play(self):
#         print("player of cricket")
        
# class Batsman(Player):
#     def bat(self):
#         print("good in batting")

# class Bowler(Player):
#     def bawl(self):
#         print("good in bowling")
    
    
# class AllRounder(Batsman,Bowler):
#     def field(self):
#         print("good in both battimg and bowling")

# a1=AllRounder()
# a1.field()
# a1.bawl()
# a1.bat()

# b1=Bowler()
# b1.bawl()
# b1.play()

class Employee:
    def work(self):
        print("fullstack developer")

class Frontend(Employee):
    def page(self):
        print("create web pages")
    
class Backend(Employee):
    def sql(self):
        print("add database")

class Fullstackdeveloper(Frontend,Backend):
    def develop(self):
        print("able to create both frontend and backend")


e1=Fullstackdeveloper()
e1.develop()
e1.sql()
e1.page()