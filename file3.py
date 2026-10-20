class Minister:
    def attend_mewting(self):
        print("attend the meeting")

class EducationMinister(Minister):
    def education_reform(self):
        print("belongs to education dept")

class FinanceMinister(Minister):
    def budget_speech(self):
        print("belongs to finance condition")

class HealtMinister(Minister):
    def inspect_govtfacilities(self):
        print("belongs to health dept")
        

h1 = HealtMinister()
h1.inspect_govtfacilities()
h1.attend_mewting()







