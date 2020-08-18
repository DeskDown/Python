class Student():
    """Student class

    Raises:
        ValueError: No Error Raised

    Returns:
        nothing: at all
    """
    
    __idPrefix = 1000
    all_students = {}

    def __init__(self, name, sname):
        Student.__idPrefix += 1
        self. name = name
        self.sname = sname
        self.id = Student.__idPrefix
        Student.all_students[self.id] = self

    
    def __str__(self):
        return self.name + " " + self.sname + " "  + "id: " + str(self.id)
    
    @classmethod
    def remove_student(cls, id):
        if id in cls.all_students.keys():
            del cls.all_students[id]
        else:
            raise ValueError(f"id: {id} Not found")