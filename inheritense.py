class Doctor():
    def __init__(self):
        print("this is a class doctor")

    def bmi(weight, height):
        bmi = weight/(height* height)
        print("Your bmi is " + str(bmi))

    def heart_rate(heart_rate):
        if(heart_rate>60 and heart_rate<100):
            print("great you heart rate is normal.")

        else:
            print("Your heart rate does not look normals please a doctor write away.")


class Patient(Doctor):
    def __init__(self, height, weight, name, heart_rate , age):
        self.patient_height = height
        self.patient_weight = weight
        self.patient_name = name
        self.patient_heart_rate = heart_rate
        self.patient_age = age

    def health_check(self):
        print("name" + self.patient_name)
        print("age" + str(self.patient_age))
        print("heart rate" + str(self.patient_heart_rate))
        print("height" + str(self.patient_height))
        print("weight" + str(self.patient_weight))
        Doctor.bmi(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rate)

patient1 = Patient(165, 90, "jessica", 129, 34)
patient1.health_check()
patient2 = Patient(198, 56, "ram", 98,12 )
patient2.health_check()