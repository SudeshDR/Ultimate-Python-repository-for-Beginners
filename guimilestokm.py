#Writing a python GUI program using Tkinter Module
#To convert Miles to Km

import tkinter as tk
def main():
    window =tk.Tk()
    window.title("Miles to Km Converter")
    window.geometry("400x200")

    #label to enter miles
    label1=tk.Label(window,text="Enter miles:")
    label1.place(x=50,y=30)

    #label2 for kilometres
    label2=tk.Label(window,text="Kilometres")
    label2.place(x=50,y=100)

    #Entry widget for input of miles
    textbox1=tk.Entry(window,width=12)
    textbox1.place(x=200,y=35)

    #label3 with empty text
    label3=tk.Label(window,text=" ")
    label3.place(x=180,y=100)

    def btn_click():
        kilometres=round(float(textbox1.get())*1.60934,5)
        label3.configure(text=str(kilometres)+' kilometres')

    #button to click convert
    btn=tk.Button(window,text="Convert",command=btn_click)
    btn.place(x=90,y=150)
    window.mainloop()
main()

    

    
    
    
