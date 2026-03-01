class person:
    def __init__(self,name,age,address):
      self.name=name
      self.age=age
      self.address=address
    def display_details(self):   
       print(f"name:{self.name},"
             f"age: {self.age},"
             f"address: {self.address}")
class Student(person):
    def __init__(self, name, age, address, student_id, course, semester):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.course = course
        self.semester = semester

    def display_details(self):
        print("Student Details:")
        super().display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Semester: {self.semester}")
        print("-" * 30)

    def enroll_course(self, new_course):
        self.course = new_course
        print(f"{self.name} has enrolled in {self.course}.\n")
class Faculty(person):
   def __init__(self,name,age,address,faculty_id,department,designation):
      super().__init__(name, age, address)
      self.faculty_id=faculty_id
      self.department=department
      self.designation=designation
   def display_details(self):
      print("faculty details")
      super().display_details()
      print(f"faculty_id: {self.faculty_id}," 
               f"department: {self.department},"
               f"designation: {self.designation}")
   def assign_course(self, course_name):
        print(f"{self.name} has been assigned to teach {course_name}.")
class Staff(person):
   def __init__(self,name,age,address,staff_id,department,designation):
      super().__init__(name,age,address)
      self.staff_id=staff_id
      self.department=department
      self.designation=designation

   def display_details(self):
        print("Staff Details:")
        super().display_details()
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}")
   def assign_task(self, task):
        print(f"{self.name} has been assigned the task: {task}\n")
student1 = Student("John Doe", 20, "123 Main St", "S123", "B.Tech", 3)
faculty1 = Faculty("Jane Smith", 35, "456 Elm St", "F123", "Computer Science", "Professor")
staff1 = Staff("Bob Johnson", 40, "789 Oak St", "ST123", "Administration", "Manager")
student1.display_details()
faculty1.display_details()
staff1.display_details()
student1.enroll_course("M.Tech")
faculty1.assign_course("Data Structures")
staff1.assign_task("Prepare Exam Schedule")
