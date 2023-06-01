from tkinter import *
root = Tk()

root.title("% Calculation")
root.geometry("600x600")

pa_garde3_label = Label()
pa_garde5_label = Label()
pa_garde10_label= Label()

class grade_3():
    
    def __init__(self, lang_arts, maths):
        self.lang_arts = lang_arts
        self.maths = maths

    def percentage(self):
        total_marks = self.lang_arts+ self.maths
        tm = total_marks*100
        grade_3_pa = tm/200
        pa_garde3_label["text"] = grade_3_pa

class grade_5():

    def __init__(self, lang_arts, maths, sst):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst

    def percentage(self):
        total_marks = self.lang_arts+ self.maths+self.sst
        tm = total_marks*100
        grade_5_pa = tm/300
        pa_garde5_label["text"] = grade_5_pa

class grade_10():

    def __init__(self, lang_arts, maths,sst, foriegn_lang):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        self.foriegn_lang = foriegn_lang

    def percentage(self):
        total_marks = self.lang_arts+ self.maths + self.sst + self.foriegn_lang
        tm = total_marks*100
        grade_10_pa = tm/400
        pa_garde10_label["text"] = grade_10_pa

obj_grade_3 = grade_3(40, 50)
grade_3_btn = Button(root, text = "Grade - 3", command = obj_grade_3.percentage)
grade_3_btn.pack(padx = 20, pady = 20)
pa_garde3_label.pack(padx = 20, pady = 20)

obj_grade_5 = grade_5(40, 50, 70)
grade_5_btn = Button(root, text = "Grade - 5", command = obj_grade_5.percentage)
grade_5_btn.pack(padx = 20, pady = 20)
pa_garde5_label.pack(padx = 20, pady = 20)

obj_grade_10 = grade_10(40, 50, 70, 90)
grade_10_btn = Button(root, text = "Grade - 10", command = obj_grade_10.percentage)
grade_10_btn.pack(padx = 20, pady = 20)
pa_garde10_label.pack(padx = 20, pady = 20)

root.mainloop()


