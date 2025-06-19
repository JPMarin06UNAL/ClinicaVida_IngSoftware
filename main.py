## The libraries necessary for the code are imported
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

def space_filled(text):
    return text.strip() != ""

def its_phone_number(entry):
    if not space_filled(entry):
        return False
    if not entry.isdigit():
        return False
    return len(entry) == 10

def show_selection_listbox():
    selected_index = listbox.curselection()  # Tuple of selected indices
    if selected_index:
        selected_item = listbox.get(selected_index[0])
        messagebox.showinfo("Selección", f"Seleccionaste: {selected_item}")
    else:
        messagebox.showinfo("Selección", "No seleccionaste nada.")





## Functions neccesary for the software according to the process diagram
## 1.Modify the doctors
## 2.Aply changes to the conditions of the schedule according to the requirementes of doctors
## 3.Verify conditions so the software can generate the shift schedule
## 4.Export shift schedule to a excel file




def main():
    root = tk.Tk()
    root.title("Gestor de Turnos")
    root.geometry("500x500") 

    ## 1.Modify the doctors
    # Create listbox
    global listbox
    listbox = tk.Listbox(root, height=6, selectmode="browse")  
    doctors_list = ["J","J","J","J","J","J","J","J","J","A","J","J","J","J","J"] # This needs to be imported from data
    for opcion in doctors_list:
        listbox.insert(tk.END, opcion)
    listbox.pack(pady=10)

    # Button to show the selected doctor
    tk.Button(root, text="Mostrar selección", command=show_selection_listbox).pack(pady=10)



    ## 2.Aply changes to the conditions of the schedule according to the requirementes of doctors

    calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.pack(pady=20)

    def show_date():
        selected_date = calendar.get_date()
        messagebox.showinfo("Fecha seleccionada", f"Seleccionaste: {selected_date}")

    boton = tk.Button(root, text="Obtener fecha", command=show_date)
    boton.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

    