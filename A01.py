import tkinter as tk
from tkinter import messagebox
import time
import sys
# Global variable to track the admin status
admin = True

# Function to perform work after GUI is hidden
def Work():
    while True:
        print('        Welcome to A01 Program!')
        print('What program do you want to use today?(1-10)')
        print('1. BMI')
        print('e. Exit')
        print('d. Description')
        user_input = input('Enter Number: ')
        #Exit function
        if user_input == 'e':
            print('Exiting program', end='', flush=True)
            for _ in range(3):
                time.sleep(0.3)
                print('.', end='', flush=True)
            print()
            print('Done!')
            sys.exit()
            break
        #BMI Program
        elif user_input == '1':
            print('---- Welcome to BMI Program ----')
            weight = int(input("Enter your weight (Kg): "))
            height = float(input("Enter your height (Meter): "))
            bmi = weight / (height ** 2)
            print(f'Your BMI is {bmi:.2f}')
            if bmi < 18.5:
                bmi_result = '!!! Below The Standard !!!'
            elif 18.5 <= bmi < 23:
                bmi_result = '! Normal !'
            elif 23 <= bmi < 25:
                bmi_result = '!! Over Weight !!'
            elif 25 <= bmi < 30:
                bmi_result = '!!! Fat LV.1 !!!'
            else:
                bmi_result = '!!!! Fat LV.2 !!!!'
            print('BMI status: ', bmi_result)
            print()
        elif user_input == 'd':
            print('###### Description ######')
            print('Welcome to A01 Program !' )
            print('This Program Developed in: 17/05/2024')
            print('Developer: Tanakon Panapong' )
            print('Language: Python')
            print('Other: I make this program in my free time to stole my knowlege and share to public')
            print()
            
        else:
            print("Invalid option. Please try again.")
            print()
        

# Function to handle button click
def check_pass():
    global admin
    user = user_entry.get()
    key = key_entry.get()
    if (user == 'admin') and (key == '12345'):
        messagebox.showinfo('Success', 'Welcome!')
        print('Request Accepted')
        root.withdraw()
        Work()
    else:
        messagebox.showinfo('Fail', 'Request Denied')
        print('Request Denied')
        root.withdraw()
        root.destroy()

# Function to hide the GUI
def Hidegui():
    root.withdraw()

# Main script execution
root = tk.Tk()
root.title("A01 Program")

if not admin:
    name_label = tk.Label(root, text="A01", font=("Helvetica", 24))
    name_label.grid(row=0, column=2)

    user_label = tk.Label(root, text="Username:")
    user_label.grid(row=1, column=1)

    user_entry = tk.Entry(root)
    user_entry.grid(row=1, column=2)

    key_label = tk.Label(root, text="Password:")
    key_label.grid(row=2, column=1)

    key_entry = tk.Entry(root, show="*")
    key_entry.grid(row=2, column=2)

    submit_btn = tk.Button(root, text="Login", command=check_pass)
    submit_btn.grid(row=3, columnspan=2)
else:
    Work()
    Hidegui()

root.geometry("400x300+400+200")
root.mainloop()