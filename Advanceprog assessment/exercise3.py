import tkinter as tk
from tkinter import ttk

# Load student data from the file
def load_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 6:
                student_no, name, coursework1, coursework2, coursework3, exam_score = parts
                students.append({
                    'student_no': student_no,
                    'name': name,
                    'coursework1': int(coursework1),
                    'coursework2': int(coursework2),
                    'coursework3': int(coursework3),
                    'exam_score': int(exam_score)
                })
    return students

# Calculate grades for each student
def calculate_grades(students):
    for student in students:
        total_coursemark = student['coursework1'] + student['coursework2'] + student['coursework3']
        student['total_coursemark'] = total_coursemark
        total_score = total_coursemark + student['exam_score']
        student['total_percentage'] = (total_score / 160) * 100

        if student['total_percentage'] >= 70:
            student['grade'] = 'A'
        elif student['total_percentage'] >= 60:
            student['grade'] = 'B'
        elif student['total_percentage'] >= 50:
            student['grade'] = 'C'
        elif student['total_percentage'] >= 40:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'

# Calculate summary information (number of students and average percentage)
def calculate_summary(students):
    num_students = len(students)
    average_percentage = (
        sum(student['total_percentage'] for student in students) / num_students 
        if num_students > 0 else 0
    )
    return num_students, average_percentage

# Update the table based on the selected view
def update_table(view):
    for row in table.get_children():
        table.delete(row)

    if view == "All Students":
        filtered_students = students
    elif view == "High Score":
        filtered_students = sorted(students, key=lambda x: x['total_percentage'], reverse=True)[:1]
    elif view == "Low Score":
        filtered_students = sorted(students, key=lambda x: x['total_percentage'])[:1]
    else:
        filtered_students = [student for student in students if student['name'] == view]

    # Insert rows into the table
    for index, student in enumerate(filtered_students):
        table.insert('', 'end', values=(
            student['name'],
            student['student_no'],
            student['total_coursemark'],
            student['exam_score'],
            f"{student['total_percentage']:.2f}%",
            student['grade']
        ), tags=('odd' if index % 2 else 'even'))

    num_students, avg_percentage = calculate_summary(filtered_students)
    summary_label.config(
        text=f"Number of Students: {num_students} | Average Percentage: {avg_percentage:.2f}%"
    )

# Load student data before initializing the GUI
students = load_student_data('studentMarks.txt')
calculate_grades(students)

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Student Manager")
root.geometry("1000x600")
root.resizable(False, False)

# Title frame
title_frame = tk.Frame(root, bg='lightblue', pady=10)
title_frame.pack(fill='x')

title_label = tk.Label(title_frame, text="Student Manager", font=('Helvetica', 18, 'bold'), bg='lightblue')
title_label.pack()

# Control frame
control_frame = tk.Frame(root, pady=10)
control_frame.pack(fill='x', padx=20)

view_label = tk.Label(control_frame, text="View: ", font=('Helvetica', 12))
view_label.pack(side='left', padx=5)

view_options = ["All Students", "High Score", "Low Score"] + [student['name'] for student in students]
view_dropdown = ttk.Combobox(
    control_frame, values=view_options, state="readonly", font=('Helvetica', 12), width=30
)
view_dropdown.set(view_options[0])
view_dropdown.pack(side='left', padx=5)

view_button = tk.Button(
    control_frame, text="Show", command=lambda: update_table(view_dropdown.get()),
    font=('Helvetica', 12), width=10
)
view_button.pack(side='left', padx=5)

# Table frame
table_frame = tk.Frame(root, pady=10)
table_frame.pack(fill='both', expand=True, padx=20)

columns = ('Name', 'Number', 'Total Coursework', 'Exam Mark', 'Overall Percentage', 'Grade')
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150)
table.pack(fill='both', expand=True)

# Add alternating row colors
table.tag_configure('odd', background='lightgrey')
table.tag_configure('even', background='white')

# Summary frame
summary_frame = tk.Frame(root, bg='lightgrey', pady=10)
summary_frame.pack(fill='x')

summary_label = tk.Label(summary_frame, text="", font=('Helvetica', 12), bg='lightgrey')
summary_label.pack()

# Load initial data into the table
update_table("All Students")

# Run the Tkinter event loop
root.mainloop()
