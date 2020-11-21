import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delete():
    for app in apps:
        apps.pop()
        print(app)

root.title("Apps Launcher")

canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

T = tk.Text(root, height=2, width=50, bg="#263D42")
T.pack()
T.insert(tk.END, "Wsh bg, choisis tes apps à lancer")
T.place(x=100, y=20)

openFile = tk.Button(root, text="Open File", padx=10, 
                    pady=3, fg="white", bg="#263D42", command=addApp)
openFile.pack()
openFile.place(x=200, y=555)
runApp = tk.Button(root, text="Run Apps", padx=10, 
                    pady=3, fg="white", bg="#263D42", command=runApps)
runApp.pack()
runApp.place(x=100, y=555)

delete = tk.Button(root, text="Delete", padx=10, 
                    pady=5, fg="white", bg="#263D42", command=delete)
delete.pack()
delete.place(x=450, y=557)
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:    #w = write
    for app in apps:
        f.write(app + ',')
