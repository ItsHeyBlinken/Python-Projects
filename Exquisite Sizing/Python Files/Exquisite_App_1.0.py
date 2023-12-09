



import tkinter as tk

def calculate_size():
    bust = float(bust_entry.get())
    waist = float(waist_entry.get())
    hips = float(hips_entry.get())

    gsi_label.config(text="Gown size is")

    if bust <= 28.3 and waist <= 20.5 and hips <= 31.5:
        result_label.config(text="Elissar 0.")
    elif bust <= 29.9 and waist <= 22 and hips <= 33.1:
        result_label.config(text="Elissar 2.")
    elif bust <= 31.5 and waist <= 23.6 and hips <= 34.6: 
        result_label.config(text='Elissar 4. \n')
        result_label.config(text='Zakaa 0. \n')
    elif bust <= 32 and waist <= 23.5 and hips <= 35.5:
        result_label.config(text='Eddy K 0. \n')
    elif bust <= 32.5 and waist <= 24.5 and hips <= 35.5: 
        result_label.config(text='Zakaa 2. \n')
    elif bust <= 33 and waist <= 24.5 and hips <= 36.5:
        result_label.config(text='Eddy K 2. \n')
        result_label.config(text='Randy Fenoli 00. \n')
    elif bust <= 33.5 and waist <= 25.5 and hips <= 36.2: 
        result_label.config(text='Elissar 6. \n')
        result_label.config(text='Zakaa 4. \n')
    elif bust <= 34 and waist <= 25.5 and hips <= 37.5:
        result_label.config(text='Eddy K 4. \n')
        result_label.config(text='Randy Fenoli 0. \n')
    elif bust <= 34.5 and waist <= 26.5 and hips <= 37:
        result_label.config(text='Zakaa 6. \n') 
    elif bust <= 34.6 and waist <= 26.8 and hips <= 37.8: 
        result_label.config(text='Elissar 8. \n')        
    elif bust <= 35 and waist <= 26.5 and hips <= 38.5: 
        result_label.config(text='Eddy K 6. \n')
        result_label.config(text='Randy Fenoli 2. \n')
    elif bust <= 36 and waist <= 27.5 and hips <= 39:
        result_label.config(text='Randy Fenoli 4. \n')
    elif bust <= 36 and waist <= 28 and hips <= 38.5:
        result_label.config(text='Zakaa 8. \n')
    elif bust <= 36.2 and waist <= 28.3 and hips <= 39.4: 
        result_label.config(text='Elissar 10. \n')
    elif bust <= 36.5 and waist <= 28 and hips <= 40:
        result_label.config(text='Eddy K 8. \n')
    elif bust <= 37.5 and waist <= 29.5 and hips <= 40:
        result_label.config(text='Zakaa 10. \n')
    elif bust <= 37.8 and waist <= 29.9 and hips <= 40.9: 
        result_label.config(text='Elissar 12. \n')
    elif bust <= 38 and waist <= 30 and hips <= 41.5:
        result_label.config(text='Eddy K 10. \n')
        result_label.config(text='Randy Fenoli 6')
    elif bust <= 39 and waist <= 30.5 and hips <= 42:
        result_label.config(text='Randy Fenoli 8. \n')
    elif bust <= 39 and waist <= 31 and hips <= 41.5:
        result_label.config(text='Zakaa 12. \n')
    elif bust <= 39.4 and waist <= 31.5 and hips <= 42.5: 
        result_label.config(text='Elissar 14. \n')
    elif bust <= 39.5 and waist <= 31.5 and hips <= 43:
        result_label.config(text='Eddy K 12. \n')
    elif bust <= 40.5 and waist <= 32 and hips <= 43.5:
        result_label.config(text='Randy Fenoli 10. \n')
    elif bust <= 40.9 and waist <= 33.1 and hips <= 44.1:
        result_label.config(text='Elissar 16. \n')
    elif bust <= 41 and waist <= 33 and hips <= 44.5:
        result_label.config(text='Eddy K 14. \n')
    elif bust <= 41 and waist <= 33 and hips <= 43.5:
        result_label.config(text='Zakaa 14. \n')
    elif bust <= 42 and waist <= 33.5 and hips <= 43.5:
        result_label.config(text='Randy Fenoli 12. \n')
    elif bust <= 42.5 and waist <= 35.5 and hips <= 46:
        result_label.config(text='Eddy K 16. \n')
    elif bust <= 42.5 and waist <= 34.6 and hips <= 45.7:
        result_label.config(text='Elissar 18. \n')
    elif bust <= 43 and waist <= 35 and hips <= 45.5:
        result_label.config(text='Zakaa 16. \n')
    elif bust <= 44 and waist <= 36 and hips <= 48:
        result_label.config(text='Eddy K Curvy 16W. \n')
    elif bust <= 44.1 and waist <= 36.2 and hips <= 47.2:
        result_label.config(text='Elissar 20. \n')
    elif bust <= 44.5 and waist <= 36.5 and hips <= 47.5:
        result_label.config(text='Eddy K 18. \n')
    elif bust <= 45 and waist <= 37.5 and hips <= 48.5:
        result_label.config(text='Randy Fenoli 14. \n')
    elif bust <= 45 and waist <= 37 and hips <= 47.5:
        result_label.config(text='Zakaa 18. \n')
    elif bust <= 45.7 and waist <= 37.8 and hips <= 48.8:
        result_label.config(text='Elissar 22. \n')
    elif bust <= 46 and waist <= 38 and hips <= 50:
        result_label.config(text='Eddy K Curvy 18W. \n')
    elif bust <= 46.5 and waist <= 38.5 and hips <= 49.5:
        result_label.config(text='Eddy K 20. \n')
    elif bust <= 47 and waist <= 39.5 and hips <= 50.5:
        result_label.config(text='Randy Fenoli 16. \n')
    elif bust <= 47.2 and waist <= 39.4 and hips <= 50.4:
        result_label.config(text='Elissar 24. \n')
    elif bust <= 48 and waist <= 40 and hips <= 52:
        result_label.config(text='Eddy K Curvy 20W. \n')
    elif bust <= 48 and waist <= 40 and hips <= 50.5:
        result_label.config(text='Zakaa 20. \n')
    elif bust <= 48.5 and waist <= 41 and hips <= 51.5:
        result_label.config(text='Eddy K 22. \n')
    elif bust <= 48.8 and waist <= 40.9 and hips <= 52:
        result_label.config(text='Elissar 26. \n')
    elif bust <= 49 and waist <= 41.5 and hips <= 52.5:
        result_label.config(text='Randy Fenoli 18. \n')
    elif bust <= 50 and waist <= 42.5 and hips <= 54.5:
        result_label.config(text='Eddy K Curvy 22W. \n')
    elif bust <= 50.4 and waist <= 42.5 and hips <= 53.5:
        result_label.config(text='Elissar 28. \n')
    elif bust <= 50.5 and waist <= 44 and hips <= 53.5:
        result_label.config(text='Eddy K 24. \n')
    elif bust <= 51 and waist <= 44 and hips <= 55:
        result_label.config(text='Randy Fenoli 20. \n')
    elif bust <= 51 and waist <= 43 and hips <= 53.5:
        result_label.config(text='Zakaa 22. \n')
    elif bust <= 52 and waist <= 45 and hips <= 57:
        result_label.config(text='Eddy K Curvy 24W. \n')
    elif bust <= 53 and waist <= 46.5 and hips <= 57.5:
        result_label.config(text='Randy Fenoli 22. \n')
    elif bust <= 53.5 and waist <= 47 and hips <= 56.5:
        result_label.config(text='Eddy K 26. \n')
    elif bust <= 54 and waist <= 47.5 and hips <= 59:
        result_label.config(text='Eddy K Curvy 26W. \n')
    elif bust <= 54 and waist <= 46 and hips <= 56.5:
        result_label.config(text='Zakaa 24. \n')
    elif bust <= 55 and waist <= 49 and hips <= 60:
        result_label.config(text='Randy Fenoli 24. \n')
    elif bust <= 56 and waist <= 50 and hips <= 61:
        result_label.config(text='Eddy K Curvy 28W. \n')
    elif bust <= 56.5 and waist <= 50 and hips <= 59.5:
        result_label.config(text='Eddy K 28. \n')
    elif bust <= 57 and waist <= 51.5 and hips <= 62.5:
        result_label.config(text='Randy Fenoli 26. \n')
    elif bust <= 57 and waist <= 49 and hips <= 59.5:
        result_label.config(text='Zakaa 26. \n')
    elif bust <= 58 and waist <= 52.5 and hips <= 64:
        result_label.config(text='Eddy K Curvy 30W. \n')
    elif bust <= 60 and waist <= 55 and hips <= 66:
        result_label.config(text='Eddy K Curvy 32W. \n')
    elif bust <= 60 and waist <= 53.5 and hips <= 65.5:
        result_label.config(text='Randy Fenoli 28. \n')
    elif bust <= 60 and waist <= 52 and hips <= 62.6:
        result_label.config(text='Zakaa 28. \n')
    elif bust <= 62 and waist <= 55.5 and hips <= 67.5:
        result_label.config(text='Randy Fenoli 30. \n')
    else:
        result_label.config(text="Custom Sizing Needed")

# Create the main window
window = tk.Tk()
window.title("Exquisite Bride Sizing Program")

# Set the window size (width x height)
window.geometry("250x250")  # You can adjust the width and height as needed

# Create and place labels and entry fields for measurements
bust_label = tk.Label(window, text="Bust measurement:")
bust_label.pack()
bust_entry = tk.Entry(window)
bust_entry.pack()

waist_label = tk.Label(window, text="Waist measurement:")
waist_label.pack()
waist_entry = tk.Entry(window)
waist_entry.pack()

hips_label = tk.Label(window, text="Hips measurement:")
hips_label.pack()
hips_entry = tk.Entry(window)
hips_entry.pack()

calculate_button = tk.Button(window, text="Calculate Size", command=calculate_size)
calculate_button.pack()

gsi_label = tk.Label(window, text="")
gsi_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
