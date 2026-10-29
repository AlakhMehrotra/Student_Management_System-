import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

## pymysql, mysql.connector , sqlite3

win = tk.Tk()

win.geometry("1600x900")
win.title("Student Management System")

win.config(bg = 'pink')

title_label = tk.Label(win, text = "Student Management System" , font=("Arial" , 30 ,"bold") , border=12 , relief=tk.GROOVE)
title_label.pack(side=tk.TOP , fill = tk.X)

detail_frame = tk.LabelFrame(win , text="Enter Details" , font=("Arial" , 20 , "bold") , bg = "navyblue" , foreground= "yellow" , border = 12 , relief=tk.GROOVE)
detail_frame.place(x = 20,y=120,height=700,width=500)

Data_Frame = tk.Frame(win , bd=12, bg='navyblue', relief=tk.GROOVE)
Data_Frame.place(x=550,y=120,height=700,width=900)

#============ Variables =======================#
rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
college = tk.StringVar()
contact = tk.StringVar()
fathers_name = tk.StringVar()
address = tk.StringVar()
cgpa = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
search_var = tk.StringVar()      # holds the "Search By" choice


#==============================================#
#=========== Database =============#
# The database file is created automatically next to this script on first run.
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.db")

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    con = get_connection()
    con.execute("""
        CREATE TABLE IF NOT EXISTS students (
            rollno       TEXT PRIMARY KEY,
            name         TEXT,
            class_name   TEXT,
            college      TEXT,
            contact      TEXT,
            fathers_name TEXT,
            address      TEXT,
            cgpa         TEXT,
            gender       TEXT,
            dob          TEXT
        )
    """)
    con.commit()
    con.close()

# Maps the "Search By" dropdown text to the database column
SEARCH_COLUMNS = {
    'Roll no.'    : 'rollno',
    'Address'     : 'address',
    'Name'        : 'name',
    'Father Name' : 'fathers_name',
    'Gender'      : 'gender',
    'D.O.B'       : 'dob',
    'C.G.P.A'     : 'cgpa',
    'Class'       : 'class_name',
    'College'     : 'college',
    'Contact No.' : 'contact',
}

#=========== Entry =============#
rollno_lbl = tk.Label(detail_frame, text="Roll no" , font=("Arial",20) , bg="navyblue",fg = "pink")
rollno_lbl.grid(row=0,column=0,padx=2,pady=4)

rollno_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=4)

name_lbl = tk.Label(detail_frame, text="Name" , font=("Arial",20) , bg="navyblue",fg = "pink")
name_lbl.grid(row=1,column=0,padx=2,pady=4)

name_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=4)

class_lbl = tk.Label(detail_frame, text="Class" , font=("Arial",20) , bg="navyblue",fg = "pink")
class_lbl.grid(row=2,column=0,padx=2,pady=4)

class_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=4)

college_lbl = tk.Label(detail_frame, text="College" , font=("Arial",20) , bg="navyblue",fg = "pink")
college_lbl.grid(row=3,column=0,padx=2,pady=4)

college_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=college)
college_ent.grid(row=3,column=1,padx=2,pady=4)

contact_lbl = tk.Label(detail_frame, text="Contact" , font=("Arial",20) , bg="navyblue",fg = "pink")
contact_lbl.grid(row=4,column=0,padx=2,pady=4)

contact_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=4)

Fathers_lbl = tk.Label(detail_frame, text="Fathers Name" , font=("Arial",20) , bg="navyblue",fg = "pink")
Fathers_lbl.grid(row=5,column=0,padx=2,pady=4)

Fathers_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=fathers_name)
Fathers_ent.grid(row=5,column=1,padx=2,pady=4)

address_lbl = tk.Label(detail_frame, text="Address" , font=("Arial",20) , bg="navyblue",fg = "pink")
address_lbl.grid(row=6,column=0,padx=2,pady=4)

address_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=4)

Cgpa_lbl = tk.Label(detail_frame, text="CGPA" , font=("Arial",20) , bg="navyblue",fg = "pink")
Cgpa_lbl.grid(row=7,column=0,padx=2,pady=4)

Cgpa_ent = tk.Entry(detail_frame,bd = 7 , font=("Arial", 18), textvariable=cgpa)
Cgpa_ent.grid(row=7,column=1,padx=2,pady=4)

gender_lbl = tk.Label(detail_frame, text="Gender" , font=("Arial",20) , bg="navyblue",fg = "pink")
gender_lbl.grid(row=8,column=0,padx=2,pady=4)

gender_ent = ttk.Combobox(detail_frame , font=("Arial",18), state="readonly" , textvariable=gender)
gender_ent['values'] = ('Male' , 'Female' , 'Others')
gender_ent.grid(row=8 , column =1 , padx = 2 , pady= 4) 

dob_lbl = tk.Label(detail_frame, text="D.O.B" , font=("Arial",20) , bg="navyblue",fg = "pink")
dob_lbl.grid(row=9,column=0,padx=2,pady=4)

dob_ent = DateEntry(detail_frame , date_pattern="dd-mm-yyyy",width=18 , font=("Arial",20) , bg="navyblue",fg = "pink")
dob_ent.grid(row=9,column=1,padx=2,pady=4)


#============ Functions =======================#

def get_form_data():
    """Read all form fields and return them as a tuple (same order as the DB columns)."""
    return (
        rollno.get().strip(),
        name.get().strip(),
        class_var.get().strip(),
        college.get().strip(),
        contact.get().strip(),
        fathers_name.get().strip(),
        address.get().strip(),
        cgpa.get().strip(),
        gender.get().strip(),
        dob_ent.get().strip(),
    )

def validate(data):
    """Return True if the form data is acceptable, otherwise show a message and return False."""
    roll, nm, cls, col, cont, fname, addr, cg, gen, birth = data

    if not roll or not nm:
        messagebox.showerror("Error", "Roll no and Name are required.")
        return False

    if cont and (not cont.isdigit() or len(cont) != 10):
        messagebox.showerror("Error", "Contact must be a 10 digit number.")
        return False

    if cg:
        try:
            value = float(cg)
        except ValueError:
            messagebox.showerror("Error", "CGPA must be a number.")
            return False
        if not (0 <= value <= 10):
            messagebox.showerror("Error", "CGPA must be between 0 and 10.")
            return False

    return True

def clear_form():
    rollno.set("")
    name.set("")
    class_var.set("")
    college.set("")
    contact.set("")
    fathers_name.set("")
    address.set("")
    cgpa.set("")
    gender.set("")
    dob_ent.set_date(datetime.today())
    rollno_ent.config(state="normal")
    rollno_ent.focus_set()

def fill_table(rows):
    """Clear the table and show the given rows."""
    student_table.delete(*student_table.get_children())
    for row in rows:
        # iid = roll no, so the exact text (e.g. leading zeros) is never altered
        student_table.insert("", tk.END, iid=row[0], values=row)

def fetch_all():
    con = get_connection()
    rows = con.execute("SELECT * FROM students ORDER BY rollno").fetchall()
    con.close()
    fill_table(rows)

def add_student():
    data = get_form_data()
    if not validate(data):
        return
    try:
        con = get_connection()
        con.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?)", data)
        con.commit()
        con.close()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"Roll no '{data[0]}' already exists.")
        return
    fetch_all()
    clear_form()
    messagebox.showinfo("Success", "Student added successfully.")

def update_student():
    data = get_form_data()
    if not validate(data):
        return
    con = get_connection()
    cur = con.execute("""
        UPDATE students
        SET name=?, class_name=?, college=?, contact=?, fathers_name=?,
            address=?, cgpa=?, gender=?, dob=?
        WHERE rollno=?
    """, data[1:] + (data[0],))
    con.commit()
    con.close()
    if cur.rowcount == 0:
        messagebox.showerror("Error", "No student found with this Roll no. Select a row from the table first.")
        return
    fetch_all()
    clear_form()
    messagebox.showinfo("Success", "Student updated successfully.")

def delete_student():
    roll = rollno.get().strip()
    if not roll:
        messagebox.showerror("Error", "Select a student from the table first.")
        return
    if not messagebox.askyesno("Confirm", f"Delete student with Roll no '{roll}'?"):
        return
    con = get_connection()
    cur = con.execute("DELETE FROM students WHERE rollno=?", (roll,))
    con.commit()
    con.close()
    if cur.rowcount == 0:
        messagebox.showerror("Error", "No student found with this Roll no.")
        return
    fetch_all()
    clear_form()
    messagebox.showinfo("Success", "Student deleted successfully.")

def reset_form():
    clear_form()
    student_table.selection_remove(student_table.selection())

def search_student():
    choice = search_var.get()
    text = particular_entry.get().strip()
    if not choice:
        messagebox.showerror("Error", "Please choose a 'Search By' option.")
        return
    if not text:
        messagebox.showerror("Error", "Please enter a value to search.")
        return
    column = SEARCH_COLUMNS[choice]
    con = get_connection()
    rows = con.execute(f"SELECT * FROM students WHERE {column} LIKE ? ORDER BY rollno", (f"%{text}%",)).fetchall()
    con.close()
    fill_table(rows)
    if not rows:
        messagebox.showinfo("Search", "No matching records found.")

def show_all():
    particular_entry.delete(0, tk.END)
    search_byent.set("")
    fetch_all()

def on_row_select(event):
    """When a table row is clicked, load that student into the form."""
    selected = student_table.selection()
    if not selected:
        return
    roll = selected[0]
    con = get_connection()
    row = con.execute("SELECT * FROM students WHERE rollno=?", (roll,)).fetchone()
    con.close()
    if row is None:
        return
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    college.set(row[3])
    contact.set(row[4])
    fathers_name.set(row[5])
    address.set(row[6])
    cgpa.set(row[7])
    gender.set(row[8])
    try:
        dob_ent.set_date(datetime.strptime(row[9], "%d-%m-%Y"))
    except (ValueError, TypeError):
        dob_ent.set_date(datetime.today())


#============BUTTON FRAME=======================#

Button_Frame = tk.Frame(detail_frame ,  bg = "navyblue" , border = 10 , relief="groove" )
Button_Frame.place(x = 25 , y = 555 , height=100 , width=420)

add_button = tk.Button(Button_Frame , text="Add" ,bg = "navyblue" , bd=5 , font=('Arial' , 13) , width=18 , height=1 , command=add_student )
add_button.grid(row=0 , column= 0 , padx= 2 , pady= 2)

reset_button = tk.Button(Button_Frame , text="Reset" ,bg = "navyblue", bd=5 , font=('Arial' , 13) , width=18 , height=1 , command=reset_form )
reset_button.grid(row=0 , column= 1 , padx= 3 , pady= 2 )

update_button = tk.Button(Button_Frame , text="Update" ,bg = "navyblue", bd=5 , font=('Arial' , 13) , width=18 , height = 1 , command=update_student )
update_button.grid(row=1 , column= 0 , padx= 2 , pady= 2 )

delete_button = tk.Button(Button_Frame , text="Delete" ,bg = "navyblue", bd=5 , font=('Arial' , 13) , width=18 , height = 1 , command=delete_student )
delete_button.grid(row=1 , column= 1 , padx= 3 , pady= 2 )

#================================================#

#================================#



#===============Data Shown===============#
search_frame = tk.Frame(Data_Frame , bd = 10 , bg='navyblue' , relief=tk.GROOVE)
search_frame.pack(side=tk.TOP , fill=tk.X)

search_by = tk.Label(search_frame , text="Search By" , font=('Arial', 15) , bg='navyblue' , fg = 'pink')
search_by.grid(row=0 , column= 0  , padx=2 , pady=2 )

search_byent = ttk.Combobox(search_frame, font=('Arial',15) , textvariable=search_var , state='readonly' )
search_byent['values'] = ('Roll no.' , 'Address' , 'Name' , 'Father Name' , 'Gender','D.O.B' , 'C.G.P.A' , 'Class' , 'College' , 'Contact No.')
search_byent.grid(row=0 , column= 1  , padx=2 , pady=2 )


particular_entry = tk.Entry(search_frame , font=('Arial',15) , bg='darkslategray')
particular_entry.grid(row=0 , column= 2 , padx=10 , pady=2)

search_btn = tk.Button(search_frame , text="Search" , border=2 , background='navyblue' , command=search_student )
search_btn.grid(row= 0 ,column=3 , padx=2 , pady=2 )

showall_btn = tk.Button(search_frame , text="Show All" , border=2 , background='navyblue' , command=show_all )
showall_btn.grid(row= 0 ,column=4, padx=2 , pady=2 )

#========================================================#


#======================DataBase Frame=========================#
main_frame = tk.Frame(Data_Frame , bd=10 , bg = "navyblue" , relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH , expand=True)

y_scroll = tk.Scrollbar(main_frame , orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame , orient= tk.HORIZONTAL) 

'''  "Roll No","Name","Class","College","Contact","Fathers Name ","Address","CGPA","Gender","D.O.B" '''

student_table = ttk.Treeview(main_frame , columns=("Roll No.","Name","Class","College","Contact","Fathers Name","Address","CGPA","Gender","D.O.B") , yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.column("Roll No." , width=100)
student_table.column("Name" , width=100)
student_table.column("Class" , width= 100)
student_table.column("College" ,width=100)
student_table.column("Contact" , width=100)
student_table.column("Fathers Name" , width=100 )
student_table.column("Address" , width=150)
student_table.column("CGPA" , width=100)
student_table.column("Gender" , width=100)
student_table.column("D.O.B" , width=100)

# Column headings (text only, no layout change)
for col_name in ("Roll No.","Name","Class","College","Contact","Fathers Name","Address","CGPA","Gender","D.O.B"):
    student_table.heading(col_name , text=col_name)

student_table['show'] = 'headings'

student_table.pack(fill=tk.BOTH,expand=True)

student_table.bind("<<TreeviewSelect>>", on_row_select)
#=============================================================#

# Create the table if needed and load existing records on start
init_db()
fetch_all()

win.mainloop()
