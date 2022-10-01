# cgpa calculator

import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.geometry("1500x1500")
main_window.title("CGPA CALCULATOR")
main_window.configure(bg="black")

gradeofcourse = []
unitofcourse = []

gradeofcourse2 = []
unitofcourse2 = []

def proceedfinal_1():

    courses_value2 = int(question2_entry.get())

    global value

    for value in range(20, courses_value2 + 20):
        course_2_label = tk.Label(text="Grade Input: ", font=("Arial BLACK", 15), bg="black")
        course_2_label.grid(row=value, column=0)

        course2_entry = tk.Entry(font=("Arial", 20), width=5)
        course2_entry.grid(row=value, column=1)
        gradeofcourse2.append(course2_entry)

        unit_2_label = tk.Label(text="Unit Input: ", font=("Arial BLACK", 15), bg="black")
        unit_2_label.grid(row=value, column=2)

        unit_2_entry = tk.Entry(font=("Arial", 20), width=5)
        unit_2_entry.grid(row=value, column=3)
        unitofcourse2.append(unit_2_entry)
    def proceedfinal_2():
        global gpa2
        scores2 = []
        unitnum2 = []
        for scoreentry2 in gradeofcourse2:
            score2 = scoreentry2.get()
            scores2.append(score2)
        for realunit2 in unitofcourse2:
            unit2 = int(realunit2.get())
            unitnum2.append(unit2)

        actul_grades2 = []
        for value in scores2:
            if value == "A":
                actul_grades2.append(5)
            elif value == "B":
                actul_grades2.append(4)
            elif value == "C":
                actul_grades2.append(3)
            elif value == "D":
                actul_grades2.append(2)
            elif value == "F":
                actul_grades2.append(0)

        units_mul_score2 = []
        for index in range(len(actul_grades2)):
            multiply2 = actul_grades2[index] * unitnum2[index]
            units_mul_score2.append(multiply2)
            Tscore2 = units_mul_score2
            Tunit2 = unitnum2
            gpa2 = sum(Tscore2) / sum(Tunit2)
        messagebox.showinfo("CALCULATOR", "YOUR SECOND SEMESTER GPA IS " + str(gpa2))
        messagebox.showinfo("CALCULATOR", "YOUR TOTAL CGPA IS " + str((gpa1+gpa2)/2))

    second_semesterbutton = tk.Button(text="PROCEED", font=("Ariel", 20), command=proceedfinal_2)
    second_semesterbutton.grid(row=value + 20, column=3)







def proceed_1():
    courses_value = int(question1_entry.get())
    global value
    for value in range(3, courses_value + 3):
        course_1_label = tk.Label(text="Grade Input: ", font=("Arial BLACK", 15), bg="black")
        course_1_label.grid(row=value, column=0)

        course1_entry = tk.Entry(font=("Arial", 20), width=5)
        course1_entry.grid(row=value, column=1)
        gradeofcourse.append(course1_entry)

        unit_1_label = tk.Label(text="Unit Input: ", font=("Arial BLACK", 15), bg="black")
        unit_1_label.grid(row=value, column=2)

        unit_1_entry = tk.Entry(font=("Arial", 20), width=5)
        unit_1_entry.grid(row=value, column=3)
        unitofcourse.append(unit_1_entry)

    def proceed_2():
        global gpa1
        scores = []
        unitnum = []
        for scoreentry in gradeofcourse:
            score = scoreentry.get()
            scores.append(score)
        for realunit in unitofcourse:
            unit = int(realunit.get())
            unitnum.append(unit)

        actul_grades = []
        for value in scores:
            if value == "A":
                actul_grades.append(5)
            elif value == "B":
                actul_grades.append(4)
            elif value == "C":
                actul_grades.append(3)
            elif value == "D":
                actul_grades.append(2)
            elif value == "F":
                actul_grades.append(0)

        units_mul_score = []
        for index in range(len(actul_grades)):
            multiply = actul_grades[index] * unitnum[index]
            units_mul_score.append(multiply)
            Tscore = units_mul_score
            Tunit = unitnum
            gpa1 = sum(Tscore) / sum(Tunit)
        messagebox.showinfo("CALCULATOR", "YOUR FIRST SEMESTER GPA IS " + str(gpa1))


    first_semesterbutton = tk.Button(text="PROCEED", font=("Ariel", 20), command=proceed_2)
    first_semesterbutton.grid(row=value + 3, column=3)




    header2_label = tk.Label(text="2ND SEMESTER GPA ", font=("Arial BLACK", 20), bg="black")
    header2_label.grid(row=value + 4, column=0, pady=15)

    question2_label = tk.Label(text="How many courses did you offer this semester: ", font=("Arial BLACK", 15),
                               bg="black")
    question2_label.grid(row=value + 5, column=0, padx=5)

    global question2_entry
    question2_entry = tk.Entry(font=("Arial", 20), width=10)
    question2_entry.grid(row=value + 5, column=1, padx=10)

    proceedfinal_button = tk.Button(text="PROCEED", font=("Arial Black", 15,), command=proceedfinal_1)
    proceedfinal_button.grid(row=value + 6, column=3)


header1_label = tk.Label(text="1ST SEMESTER GPA ", font=("Arial BLACK", 20), bg="black")
header1_label.grid(row=0, column=0, pady=15)

question1_label = tk.Label(text="How many courses did you offer this semester: ", font=("Arial BLACK", 15),
                           bg="black", )
question1_label.grid(row=1, column=0, padx=5)

question1_entry = tk.Entry(font=("Arial", 20), width=10)
question1_entry.grid(row=1, column=1, padx=10)

proceed1_button = tk.Button(text="PROCEED", font=("Arial Black", 15,), command=proceed_1)
proceed1_button.grid(row=1, column=3)

main_window.mainloop()