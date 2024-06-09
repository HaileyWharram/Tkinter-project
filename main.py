#Authors: Liza, Hailey, Martha
#Title: Annoying UI
#Course: ICS4U-03
#Date: June 8, 2024

#import Tkinter library and pillow
#note: to run the program, you'll need to install pillow
#type "pip install pillow" in terminal
#when running the program, you have to move the window(click on the edge and move a bit)
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# used for resizing images and buttons together with window
def resize_image(event):
    # update canvas size to match the new window size & adjusting positions
    if 'canvas' in globals() and canvas.winfo_exists():
        canvas.config(width=event.width, height=event.height)
        canvas.coords(bg_image_id, 0, 0)
        canvas.coords(label_window, event.width // 2, event.height // 2)
        canvas.coords(button_window, event.width // 2 - 30, (event.height // 2) + 50)
        canvas.coords(button_window_no, event.width // 2 + 30, (event.height // 2) + 50)
        canvas.coords(fake_day_label_window, event.width // 2 - 50, event.height // 2 - 100)
        canvas.coords(fake_day_window, event.width // 2 + 50, event.height // 2 - 100)
        canvas.coords(fake_month_label_window, event.width // 2 - 50, event.height // 2 - 70)
        canvas.coords(fake_month_window, event.width // 2 + 50, event.height // 2 - 70)
        canvas.coords(fake_year_label_window, event.width // 2 - 50, event.height // 2 - 40)
        canvas.coords(fake_year_window, event.width // 2 + 50, event.height // 2 - 40)

# function for yes button 
def on_yes():
    print("Is this your birthday?")
    #display the message
    messagebox.showinfo("Info", "Are you sure?")

# function for no button   
def on_no():
    print("Are you sure?")
    #display the message
    messagebox.showinfo("Info", "Could not cancel operation")

# function that asks user to enter day, month and year of birth
def get_birthday():
    #handles dialog boxes
    day = simpledialog.askinteger("Input", "Your day of birth:", parent=init, minvalue=1, maxvalue=31)
    month = simpledialog.askstring("Input", "Your month of birth:", parent=init)
    year = simpledialog.askinteger("Input", "Your year of birth:", parent=init, minvalue=1900, maxvalue=2100)
    if day and month and year:
        birthdate = f"{day} / {month} / {year}"
        print(birthdate)
        label.config(text=birthdate)
        
        #call switch to switch to next window
        switch()

def switch():
    init.unbind('<Configure>')
    for widget in init.winfo_children():
        #removes the current window
        widget.destroy()
    new_canvas = tk.Canvas(init, width=400, height=400)
    new_canvas.pack(fill="both", expand=True)
    
    new_bg_image = ImageTk.PhotoImage(Image.open("file.png"))
    new_canvas.create_image(0, 0, image=new_bg_image, anchor="nw")
    
    text = tk.Label(init, text="Processing your birthday...")
    text_window = new_canvas.create_window(325, 180, window=text)
    
    falling_cupcakes(new_canvas, text)
    
    new_canvas.bg_image = new_bg_image

#the following functions are displaying messages of warnings to ennoy user
#they follow after each other       
def fake_message(event):
    messagebox.showinfo("Info", "Data is not inserted. Try another way")
    init.after(5000, delayed_warning)

def delayed_warning():
    messagebox.showwarning("Warning", "Why are you still trying?")
    init.after(5000, another_delayed_warning)

def another_delayed_warning():
    messagebox.showerror("Error", "An error occured")
    init.after(5000, final_warning)

def final_warning():
    messagebox.showinfo("Info", "This is the last warning... or is it?")
    #init.after(5000, fake_message) 

def show_final_window():
    #destroy the old window
    for widget in init.winfo_children():
        widget.destroy()
    #create new window
    final_canvas = tk.Canvas(init, width=400, height=400)
    final_canvas.pack(fill="both", expand=True)
    final_bg_img = ImageTk.PhotoImage(Image.open("file.png"))
    final_canvas.create_image(0, 0, image=final_bg_img, anchor="nw")
        
    final_text = tk.Label(init, text="Done! Thanks for inputting your birthday!", font=("Helvetica", 16))
    final_text_window = final_canvas.create_window(325, 180, window=final_text)
    final_canvas.bg_image = final_bg_img
    
#function to create falling cupcakes animation
#parameters: canvas(object), text_window(object)
def falling_cupcakes(canvas, text_window):
    print("Falling cupcakes initiated")
    #create an empty list of cupcakes that will be filled out
    cupcakes = []
    for i in range(6):
        #create 6 images for cupcakes
        cupcake = canvas.create_image(i * 100, -50, anchor="nw", image=cupcake_img_final)
        #fill them in the list
        cupcakes.append(cupcake)
        print(f"Cupcake {i} created at position {i * 100}, -50")

    #function to animate movements of cupcakes
    #parameters: step(int), loop(int)
    def animate(step=0, loop=0):
        if loop < 5:
            if step < 50:
                for i, cupcake in enumerate(cupcakes):
                    canvas.move(cupcake, 0, 5)
                    print(f"Cupcake {i} moved to {canvas.coords(cupcake)}")
                canvas.update()
                init.after(50, animate, step + 1, loop)
            else:
                for i, cupcake in enumerate(cupcakes):
                    canvas.coords(cupcake, i * 100, -50)
                    print(f"Cupcake {i} reset to {canvas.coords(cupcake)}")
                canvas.update()
                init.after(500, animate, 0, loop + 1)
        else:
            for i, cupcake in enumerate(cupcakes):
                canvas.delete(cupcake)
                print(f"Cupcake {i} deleted")
            #once done, display the final window
            show_final_window()
    animate()

#function for fake entries to trick user
def fake_entry():
    fake_day_label = tk.Label(init, text="Your day of birth:", bg="white")
    fake_month_label = tk.Label(init, text="Your month of birth:", bg="white")
    fake_year_label = tk.Label(init, text="Your year of birth:", bg="white")
    fake_day = tk.Entry(init, state="readonly", width=5, justify="center")
    fake_month = tk.Entry(init, state="readonly", width=10, justify="center")
    fake_year = tk.Entry(init, state="readonly", width=5, justify="center")

    # 0 is represented as a default value, asking in what format to enter data
    fake_day.insert(0, "DD")
    fake_month.insert(0, "MM")
    fake_year.insert(0, "YYYY")

    #bind the click event to the fake entries
    fake_day.bind("<Button-1>", fake_message)
    fake_month.bind("<Button-1>", fake_message)
    fake_year.bind("<Button-1>", fake_message)

    #use global to interpret fake day, month and year on the window
    global fake_day_label_window, fake_day_window
    global fake_month_label_window, fake_month_window
    global fake_year_label_window, fake_year_window

    fake_day_label_window = canvas.create_window(325 - 100, 100, window=fake_day_label)
    fake_day_window = canvas.create_window(325 - 50, 150, window=fake_day)
    fake_month_label_window = canvas.create_window(325 - 100, 130, window=fake_month_label)
    fake_month_window = canvas.create_window(325, 150, window=fake_month)
    fake_year_label_window = canvas.create_window(325 - 100, 160, window=fake_year_label)
    fake_year_window = canvas.create_window(325 + 50, 150, window=fake_year)

init = tk.Tk()
init.title("Birthdate")
# initialize the window
init.geometry("650x360")

# load images using Pillow
bg_image_pil = Image.open("file.png")
cupcake_img_pil = Image.open("cupcake(1).png")

# convert Pillow images to PhotoImage for Tkinter
bg_image = ImageTk.PhotoImage(bg_image_pil)
cupcake_img = cupcake_img_pil.resize((200, 200))
cupcake_img_final = ImageTk.PhotoImage(cupcake_img)

# create canvas
canvas = tk.Canvas(init, width=650, height=360)
canvas.pack(fill="both", expand=True)

# add images to canvas
bg_image_id = canvas.create_image(0, 0, image=bg_image, anchor="nw")
label = tk.Label(init, text="test text for now", width=650, height=360, image=bg_image)
label_window = canvas.create_window(650, 360, window=label)
yes_button = tk.Button(init, text="Confirm", command=on_yes)
no_button = tk.Button(init, text="Cancel", command=on_no)
button_window = canvas.create_window(325, 240, window=yes_button)
button_window_no = canvas.create_window(325, 280, window=no_button)

# call the fake entry function
fake_entry()

# meant to call the function to resize the image with window
init.bind('<Configure>', resize_image)

menu = tk.Menu(init)
init.config(menu=menu)
# call the function get_birthday for label
menu.add_command(label="Your Birthday!", command=get_birthday)

# run the main event loop
init.mainloop()