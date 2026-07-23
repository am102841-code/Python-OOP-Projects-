class Student:
    def __init__(self):
        # name and grade, function add grade, function averagen graade.
        # also print out each grade percent with the ltter grade for it at the end
        # more ideas, gpa calcualtor, differnt types of schools, private and public, shcool cost calucalot for public/ private,
      # chedck if the typed grades are less than zero, mroe than 100, or not an integer 
        self.name = input("What is your name? \n < ")
        self.grade = None
        self.grade_amount = 3
        self.grades = []
        self.letters = []
        self.average_int = 0
        self.final_grades = None
        self.gpa_int = 0  
        self.gpa_average = 0
        self.schedule = None 
        self.cost = 0 
        self.school_type = None 
        self.average_letter = None

    def add_grades(self):
        looping = True
        while looping:
            if self.grade_amount == 0:
                print("All three grades inputed!")
                break
            else:
                grade = input("Input a grade \n < ")
                #if type(grade) != int: 
                  #grade = input("Please type an integer \n < ")
          
                self.grades.append(int(grade))
                self.grade_amount -= 1

    def average(self):
        total = 0
        for x in self.grades:
            total = int(x) + total
        self.average_int = total / len(self.grades)
        self.average_int = round(self.average_int, 2)
        if self.average_int <= 60:
            self.average_letter = "F"
        elif self.average_int >= 60 and self.average_int <= 69:
            self.average_letter = "D"
        elif self.average_int >= 70 and self.average_int <= 79: 
            self.average_letter = "C" 
        elif self.average_int >= 80 and self.average_int <= 89: 
            self.average_letter = "B"
        elif self.average_int <= 100 and self.average_int >= 90: 
            self.average_letter = "A"
        # print(f"Average: {self.average_int}")

    def letter_grades(self):
        self.letters = []
        
        for x in self.grades: # three letter grades in total
            if x <= 60:
                self.letters.append("F")
            elif x >= 60 and x <= 69:
                self.letters.append("D")
            elif x >= 70 and x <= 79: 
              self.letters.append("C") 
            elif x >= 80 and x <= 89: 
              self.letters.append("B")
            elif x <= 100 and x >= 90: 
              self.letters.append("A")

        self.final_grades = {
            self.grades[0]: self.letters[0],
            self.grades[1]: self.letters[1],
            self.grades[2]: self.letters[2],
        }

    def gpa(self): 
        # A = 4 ; B = 3 ; C = 2; D = 1; F = 0 
        # find all values of the letter grades, then divide by 3 to find the average
        for x in self.letters: 
          if x == "A":
            self.gpa_int += 4 
          if x == "B": 
            self.gpa_int += 3 
          if x == "C": 
            self.gpa_int += 2 
          if x == "D": 
            self.gpa_int += 1 
          if x == "F": 
            self.gpa_int += 0 

        self.gpa_average = self.gpa_int/3
        self.gpa_average = round(self.gpa_average, 2)

    #def cost(self): 
      #pass
      

student1 = Student()
student1.add_grades()
student1.average()
student1.letter_grades()
student1.gpa()

print(
    f"Student: {student1.name} \nAverage: {student1.average_int} | {student1.average_letter}"
)

print(f"Grades: \n {student1.grades[0]} | {student1.letters[0]} \n {student1.grades[1]} | {student1.letters[1]} \n {student1.grades[2]} | {student1.letters[2]} \nGPA: {student1.gpa_average}")
