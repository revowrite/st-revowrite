import tkinter as tk
import csv

def generate_csv_file():
    society_data = {
        'Name of Society': name_entry.get(),
        'Address': address_entry.get(),
        'State': state_entry.get(),
        'District': district_entry.get(),
        'Date of Registration': registration_entry.get(),
        'Area of Operation': operation_entry.get(),
        'Sector Type': sector_entry.get()
    }
    
    fieldnames = ['Name of Society', 'Address', 'State', 'District', 'Date of Registration', 'Area of Operation', 'Sector Type']

    with open('society_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(society_data)
    
    # Optional: Show a confirmation message
    messagebox.showinfo("CSV File Generated", "Society data has been saved to society_data.csv")

# Create the main window
window = tk.Tk()
window.title("Society Form")

# Create the form labels
name_label = tk.Label(window, text="Name of Society")
address_label = tk.Label(window, text="Address")
state_label = tk.Label(window, text="State")
district_label = tk.Label(window, text="District")
registration_label = tk.Label(window, text="Date of Registration")
operation_label = tk.Label(window, text="Area of Operation")
sector_label = tk.Label(window, text="Sector Type")

# Create the form entry fields
name_entry = tk.Entry(window)
address_entry = tk.Entry(window)
state_entry = tk.Entry(window)
district_entry = tk.Entry(window)
registration_entry = tk.Entry(window)
operation_entry = tk.Entry(window)
sector_entry = tk.Entry(window)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=generate_csv_file)

# Arrange the form elements using grid layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
address_entry.grid(row=1, column=1)
state_label.grid(row=2, column=0)
state_entry.grid(row=2, column=1)
district_label.grid(row=3, column=0)
district_entry.grid(row=3, column=1)
registration_label.grid(row=4, column=0)
registration_entry.grid(row=4, column=1)
operation_label.grid(row=5, column=0)
operation_entry.grid(row=5, column=1)
sector_label.grid(row=6, column=0)
sector_entry.grid(row=6, column=1)
submit_button.grid(row=7, column=1)

# Start the GUI event loop
window.mainloop()
