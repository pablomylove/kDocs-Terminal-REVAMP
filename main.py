import tkinter
import time

root = tkinter.Tk()
root.title("")
root.attributes("-fullscreen", True)
root.config(bg="black")

fileFrame = tkinter.Frame(root, bg="#111111", width=250, height=9999999)
fileFrame.propagate(False)
fileFrame.pack(side="right")

titleFrame = tkinter.Frame(fileFrame, bg="#111111", width=250, height=42)
titleFrame.propagate(False)
titleFrame.pack(side="top")

tkinter.Label(titleFrame, text="Files" , bg="#111111", fg="white", font=("Arial", 23)).place(x=0, y=0)

cmdEntry = tkinter.Entry(root, width=9999999, justify="left", fg="white", bg="black", borderwidth=5)
cmdEntry.pack(side="top")

cmdResultLabels = []

files = []
fileButtons = []

def script(event):
  global cmdEntry, cmdResultLabels
  if "print" in cmdEntry.get():
    args = cmdEntry.get().split(" ", 2)
    try:
      l = tkinter.Label(root, text=args[2], fg=args[1], bg="black", font=("Arial", 9))
    except:
      tkinter.Label(root, text="ERROR: invalid text colour", fg="red", bg="black", font=("Arial", 9))
    cmdResultLabels.append(l)
    l.pack(side="top")
  if "new_file" in cmdEntry.get():
    global files, fileButtons
    args = cmdEntry.get().split(" ", 1)
    files.append(args[1])
    l = tkinter.Label(root, text='file "'+args[1]+'" created in '+time.ctime(), bg="black", fg="white" , font=("Arial", 9))
    cmdResultLabels.append(l)
    l.pack(side="top", pady=1)
    files.append(args[1])
    newFileButton = tkinter.Button(fileFrame, text=args[1], bg="#111111", fg="white", font=(10), width=900000)
    fileButtons.append(newFileButton)
    newFileButton.pack(side="top")
  if "delete_file" in cmdEntry.get():
    args = cmdEntry.get().split(" ", 1)
    try:
      files.remove(args[1])
      for i in fileButtons:
        if i.cget("text") == args[1]:
          i.destroy()
          fileButtons.remove(i)
        else:
              tkinter.Label(root, text="ERROR: file not found", fg="red", bg="black", font=("Arial", 11)).pack(side="top")
    except:
      tkinter.Label(root, text="ERROR: file not found", fg="red", bg="black", font=("Arial", 11)).pack(side="top")
  
  cmdEntry.delete(0, "end")

cmdEntry.bind("<Return>", script)

tkinter.mainloop()
