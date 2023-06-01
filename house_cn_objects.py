class citizen:
    def __init__(self, name, age, dob, id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id_number = id_number

    def add_citizen(self):
        print("name : " + self.citizen_name)
        print("age : "+ str(self.citizen_age))
        print("dob : "+ self.citizen_dob)
        print("citizen id : " + self.citizen_id_number)
        print("citizen added")


citizen_1 = citizen("sophia",10, "6 august 2012", "8485")
citizen_1.add_citizen()
citizen_2 = citizen("harry", 95, "6  november 1927", "5657")
citizen_2.add_citizen()