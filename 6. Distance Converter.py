from tkinter import Label, Button, Entry, messagebox, Tk, END


def convert():
    try:
        if len(mileEntry.get()) == 0 and len(kmEntry.get()) == 0:
            messagebox.showwarning("Input Error", "Check your input. Both fields can't be empty")
        elif len(mileEntry.get()) == 0:
            mileEntry.insert(END, float(kmEntry.get())*0.621371)
        elif len(kmEntry.get()) == 0:
            kmEntry.insert(END, float(mileEntry.get())*1.60934)
        else:
            messagebox.showwarning("Input Error", "Check your input. Both fields can't be filled")
    except ValueError:
        messagebox.showerror("Value Error", "You must enter a number only")

if __name__ == "__main__":
    window = Tk()
    window.geometry("250x175")
    window.title("Distance Converter")

    kmLabel = Label(window, text="Kilometer")
    kmLabel.place(x=20, y=25)

    kmEntry = Entry(window)
    kmEntry.place(x=100, y=25)

    mileLabel = Label(window, text="Miles")
    mileLabel.place(x=20, y=75)

    mileEntry = Entry(window)
    mileEntry.place(x=100, y=75)

    convertBtn = Button(window, text="Convert", command=convert)
    convertBtn.place(x=100, y=125)

    window.mainloop()