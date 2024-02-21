import tkinter as tk

# Conversion functions
def cm_to_feet():
    cm = float(entry_cm.get())
    feet = cm / 30.48
    label_result.config(text=f"{cm} centimeters is equal to {feet:.2f} feet.")

def feet_to_inches():
    feet = float(entry_feet.get())
    inches = feet * 12
    label_result.config(text=f"{feet} feet is equal to {inches:.2f} inches.")

def sqft_to_sqmtrs():
    sqft = float(entry_sqft.get())
    sqmtrs = sqft / 10.764
    label_result.config(text=f"{sqft} square feet is equal to {sqmtrs:.2f} square meters.")

def sqft_to_hectare_acres():
    sqft = float(entry_sqft_area.get())
    hectares = sqft / 107639.104
    acres = sqft / 43560
    label_result.config(text=f"{sqft} square feet is equal to {hectares:.6f} hectares or {acres:.6f} acres.")

# Create a new Tkinter window
window = tk.Tk()
window.title("Unit Conversion")

# Centimeter to Feet
label_cm = tk.Label(window, text="Centimeters to Feet:")
label_cm.grid(row=0, column=0, padx=15, pady=15, sticky="w")
entry_cm = tk.Entry(window)
entry_cm.grid(row=0, column=1, padx=15, pady=15)
button_cm = tk.Button(window, text="Convert", command=cm_to_feet)
button_cm.grid(row=0, column=2, padx=15, pady=15)
#label_result_cm_feet = tk.Label(window, text="")
#label_result_cm_feet.grid(row=0, column=3, padx=15, pady=15, sticky="w")

# Feet to Inches
label_feet = tk.Label(window, text="Feet to Inches:")
label_feet.grid(row=1, column=0, padx=15, pady=15, sticky="w")
entry_feet = tk.Entry(window)
entry_feet.grid(row=1, column=1, padx=15, pady=15)
button_feet = tk.Button(window, text="Convert", command=feet_to_inches)
button_feet.grid(row=1, column=2, padx=15, pady=15)
#label_result_feet_inches = tk.Label(window, text="")
#label_result_feet_inches.grid(row=1, column=3, padx=15, pady=15, sticky="w")

# Square Feet to Square Meters
label_sqft = tk.Label(window, text="Square Feet to Square Meters:")
label_sqft.grid(row=2, column=0, padx=15, pady=15, sticky="w")
entry_sqft = tk.Entry(window)
entry_sqft.grid(row=2, column=1, padx=15, pady=15)
button_sqft = tk.Button(window, text="Convert", command=sqft_to_sqmtrs)
button_sqft.grid(row=2, column=2, padx=15, pady=15)
#label_result_sqft_sqmtrs = tk.Label(window, text="")
#label_result_sqft_sqmtrs.grid(row=2, column=3, padx=15, pady=15, sticky="w")

# Square Feet to Hectare / Acres
label_sqft_area = tk.Label(window, text="Square Feet to Hectares/Acres:")
label_sqft_area.grid(row=3, column=0, padx=15, pady=15, sticky="w")
entry_sqft_area = tk.Entry(window)
entry_sqft_area.grid(row=3, column=1, padx=15, pady=15)
button_sqft_area = tk.Button(window, text="Convert", command=sqft_to_hectare_acres)
button_sqft_area.grid(row=3, column=2, padx=15, pady=15)
#label_result_sqft_area = tk.Label(window, text="")
#label_result_sqft_area.grid(row=3, column=3, padx=15, pady=15, sticky="w")

# Run the Tkinter event loop
label_result = tk.Label(window, text="")
label_result .grid(row=4, columnspan=3, padx=15, pady=15)
window.mainloop()