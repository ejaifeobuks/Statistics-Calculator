# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:07:02 2023

@author: OgheneobukomeEjaife
"""
import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image
from io import BytesIO
import xml.etree.ElementTree as ET
from urllib.parse import quote
import mathematical_functions as mp

root = tk.Tk()

def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/().,":
        mp.add_to_calculation(key, text_result)
    elif key == '\r':
        evaluate_calculation()

def update_buttons(config):
    for btn, cfg in zip(button_list, config):
        btn.config(text=cfg["text"], command=lambda c=cfg["command"]: c(text_result))

def statistics_panel():
    update_buttons(statistics_panel_config)
    btn_open.config(text="X-values", command=lambda: mp.input_values("X", text_result))
    btn_closed.config(text="Y-values", command=lambda: mp.input_values("Y", text_result))
    btn_open.grid()
    btn_closed.grid()

def basic_panel():
    update_buttons(basic_panel_config)
    btn_open.config(text="(", command=lambda: mp.add_to_calculation("(", text_result))
    btn_closed.config(text=")", command=lambda: mp.add_to_calculation(")", text_result))
    btn_open.grid()
    btn_closed.grid()

def graph_panel():
    # Implement the graph panel functionality
    pass

def scientific_panel():
    # Implement the scientific panel functionality
    pass

def evaluate_calculation():
    try:
        expression = mp.stat_calculator.expression
        result = str(eval(expression))
        mp.stat_calculator.clear_expression()
        mp.add_to_calculation(result, text_result)
    except Exception as e:
        mp.clear_field(text_result)
        text_result.insert("1.0", f"Error: {e}")

def Ask():
    try:
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                encoded_url = quote(file_content, encoding='utf-8')
                Request_url = 'http://api.wolframalpha.com/v2/query?appid=YOUR_APP_ID&input=' + encoded_url + '&podstate=Result__Step-by-step%20solution&format=image'
                print(Request_url)
                response = requests.get(Request_url)
                if response.status_code == 200:
                    roots = ET.fromstring(response.text)
                    for subpod in roots.findall(".//subpod"):
                        img_url = subpod.find(".//img").get("src")
                        img_response = requests.get(img_url)
                        if img_response.status_code == 200:
                            img_content = BytesIO(img_response.content)
                            img = Image.open(img_content)
                            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
                            if save_path:
                                img.save(save_path)
                                print(f"Image saved to: {save_path}")
                            else:
                                print("Saving canceled.")
                        else:
                            print(f"Error fetching image: {img_response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Create button placeholders
button_list = []

# Create a grid of buttons (3 columns x 3 rows for the main panel)
for row in range(1, 4):
    for col in range(0, 3):
        btn = tk.Button(root, width=5, font=("Arial", 14))
        btn.grid(row=row, column=col)
        button_list.append(btn)

# Additional buttons
btn_open = tk.Button(root, width=5, font=("Arial", 14))
btn_open.grid(row=4, column=0)
btn_closed = tk.Button(root, width=5, font=("Arial", 14))
btn_closed.grid(row=4, column=2)

# Define panel configurations
basic_panel_config = [
    {"text": "1", "command": lambda tr: mp.add_to_calculation("1", tr)},
    {"text": "2", "command": lambda tr: mp.add_to_calculation("2", tr)},
    {"text": "3", "command": lambda tr: mp.add_to_calculation("3", tr)},
    {"text": "4", "command": lambda tr: mp.add_to_calculation("4", tr)},
    {"text": "5", "command": lambda tr: mp.add_to_calculation("5", tr)},
    {"text": "6", "command": lambda tr: mp.add_to_calculation("6", tr)},
    {"text": "7", "command": lambda tr: mp.add_to_calculation("7", tr)},
    {"text": "8", "command": lambda tr: mp.add_to_calculation("8", tr)},
    {"text": "9", "command": lambda tr: mp.add_to_calculation("9", tr)},
]

statistics_panel_config = [
    {"text": "Mean", "command": mp.mean},
    {"text": "Mode", "command": mp.mode},
    {"text": "Median", "command": mp.median},
    {"text": "Range", "command": mp.data_range},
    {"text": "Std Dev", "command": mp.standard_deviation},
    {"text": "Variance", "command": mp.variance},
    {"text": "Coef Var", "command": mp.coefficient_of_variation},
    {"text": "Regression", "command": lambda tr: mp.regression(tr)},
    {"text": "Values", "command": mp.get_values},
]

# Initialize with basic panel
basic_panel()

# Continue setting up other buttons
btn_0 = tk.Button(root, text="0", command=lambda: mp.add_to_calculation("0", text_result), width=5, font=("Arial", 14))
btn_0.grid(row=4, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: mp.add_to_calculation("+", text_result), width=5, font=("Arial", 14))
btn_plus.grid(row=1, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: mp.add_to_calculation("-", text_result), width=5, font=("Arial", 14))
btn_minus.grid(row=2, column=3)
btn_mul = tk.Button(root, text="*", command=lambda: mp.add_to_calculation("*", text_result), width=5, font=("Arial", 14))
btn_mul.grid(row=3, column=3)
btn_div = tk.Button(root, text="/", command=lambda: mp.add_to_calculation("/", text_result), width=5, font=("Arial", 14))
btn_div.grid(row=4, column=3)

btn_clear = tk.Button(root, text="C", command=lambda: mp.clear_field(text_result), width=11, font=("Arial", 14))
btn_clear.grid(row=5, column=0, columnspan=2, sticky="nsew")
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=5, column=2)
btn_separate = tk.Button(root, text=",", command=lambda: mp.add_to_calculation(",", text_result), width=11, font=("Arial", 14))
btn_separate.grid(row=5, column=3)
btn_ask = tk.Button(root, text="Ask an AI", command=Ask, width=11, font=("Arial", 14))
btn_ask.grid(row=5, column=4)

btn_statistics = tk.Button(root, text="Statistics", command=statistics_panel, width=11, font=("Arial", 14))
btn_statistics.grid(row=1, column=4)
btn_basic = tk.Button(root, text="Basic", command=basic_panel, width=11, font=("Arial", 14))
btn_basic.grid(row=2, column=4)
btn_scientific = tk.Button(root, text="Scientific", command=scientific_panel, width=11, font=("Arial", 14))
btn_scientific.grid(row=3, column=4)
btn_graphs = tk.Button(root, text="Graphs", command=graph_panel, width=11, font=("Arial", 14))
btn_graphs.grid(row=4, column=4)

buttons = button_list + [btn_0, btn_clear, btn_closed, btn_equals, btn_minus, btn_open, btn_div, btn_mul, btn_plus, btn_statistics, btn_basic, btn_scientific, btn_graphs, btn_ask, btn_separate]


def calculator_resizer(event=None):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_height = int(0.1 * window_height)
    button_width = int(0.2 * window_width)
    text_result_height=int(0.5*window_height)
    text_result_width=window_width
    font_size = int(min(window_width / 30, window_height / 30))
    text_result_properties={"font": ("Arial", font_size),"height":text_result_height,"width":text_result_width}
    widget_properties = {"font": ("Arial", font_size), "height": button_height, "width": button_width}
    for btn in buttons:
        btn.configure(**widget_properties)
    text_result.configure(**text_result_properties) 
# Configure rows and columns to expand with the window
root.grid_rowconfigure(0, weight=5)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(0, 5):
    root.grid_columnconfigure(i, weight=1)

root.bind("<Configure>", calculator_resizer)
btn_graphs.bind("<Button-1>",lambda event:graph_panel())
btn_scientific.bind("<Button-1>",lambda event:scientific_panel())
btn_basic.bind("<Button-1>",lambda event:basic_panel())

root.bind("<Key>", on_key)
calculator_resizer()
root.mainloop()
