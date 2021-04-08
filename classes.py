class student:

    def __init__(self,name,major,gpa,isOnProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation

    def Honors(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False