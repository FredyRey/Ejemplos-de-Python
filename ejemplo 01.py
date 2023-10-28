class User:
    name=None
    email=None
    def send_email(self):
        if self.email is not None:
            print("sendingemail"+self.email)
        else:
            print("error")

    def init(self,name,email): # este es el llamado Constructor 
        self.name=name
        self.email=email
    def str(self):
        return "User: " + self.email

class Student(User):
    id =None
    def init(self,
       name=None,
       email=None,
       id= None,
       score = None
       ):
       super().init(name,email)
       self.id= id
       self.score = score
    def str(self):
        return "Student:"+str(self.id)+","+self.email
    def repr(self):
        return f"Student(name='{self.name}',email='{self.email}', id='{self.id}')"
    {}
