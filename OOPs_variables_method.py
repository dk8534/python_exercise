# In python OOPs 3 variables :
# 1. Instance variables (object level variable)
# 2. Static/class variables (class level variable)
# 3. local variable (general generic variable)

class Test:
    collageName = 'V.S.S.INTER COLLAGE' #class variable
    # instance method:
    def __init__(self,name,rollno):
        self.name = name #instance variable
        self.rollno = rollno #instance variable
    # class method: 
    def getinfo(cls):
        print('collage name',cls.collageName)
    #static method:
    @staticmethod #as per class method process    
    def getinfo2():
        x = 10 #x is localvariable
        for i in range(x): # i is localvariable
            print(i)

x=Test('darshan',123)
x.getinfo()
x.getinfo2()

# In python OOPs 3 methods:
# 1. Instance method(if atleast instance variable present inside method know as instance method)
# 2. class method(if not any instanece variable present but present atleast static or class variable inside method know as class method)
# 3. static method(if not any instance variable and not any class or static variable present inside method known as static method.)

# to accress or creation of class method:

class Test:
    collageName = 'V.S.S.INTER COLLAGE' #class variable
    # instance method:
    def __init__(self,name,rollno):
        self.name = name #instance variable
        self.rollno = rollno #instance variable
    # class method:
    @classmethod #to convert or access class variables or method to class method we need to use before classmethod decorator outside the method.
    def getinfo(cls):
        print('collage name',cls.collageName)
    #static method:    
    def getinfo2(self):
        x = 10 #x is localvariable
        for i in range(10): # i is localvariable
            print(i)

x=Test('dk',123)
x.getinfo()
