import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Name Entry App")
    window.geometry("300x200") 

    label = tk.Label(window, text="Enter Your Name:", font=("Arial", 12))
    label.pack(pady=10)

    name_entry = tk.Entry(window, width=30)
    name_entry.pack(pady=5)

    def submit_Name():
        name = name_entry.get()  
        print("User entered:", name)
        
    submit_button = tk.Button(window, text="Submit", command=submit_Name)
    submit_button.pack(pady=10)  

    window.mainloop()

if __name__ == "__main__":
    main()