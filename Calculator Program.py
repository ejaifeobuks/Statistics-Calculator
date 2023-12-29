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
import xml.etree.ElementTree as ET  # Add this line to import ET
from urllib.parse import quote
import mathematical_functions as mp
root=tk.Tk()      

def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/().,":
        mp.add_to_calculation(key,text_result)
    elif key == '\r':
        evaluate_calculation()

def Statistics_panel():
    btn_1.config(text="mean", command=lambda: mp.mean(text_result))
    btn_2.config(text="mode", command=lambda: mp.mode(text_result))
    btn_3.config(text="median", command=lambda:mp.median(text_result))
    btn_4.config(text="range", command=lambda: mp.Range(text_result))
    btn_5.config(text="Standard deviation", command=lambda:mp.Standard_deviation(text_result))
    btn_6.config(text="Variance", command=lambda: mp.Variance(text_result))
    btn_7.config(text="Coefficient of Variance", command=lambda:mp.Coefficient_of_Variation(text_result))
    btn_8.config(text="Z-score", command=lambda: mp.X_values(text_result) )
    btn_9.config(text="Regression", command=lambda: mp.Regression(text_result))
    btn_open.config(text="X-value",command=lambda: mp.X_values(text_result))
    btn_closed.config(text="Y-value",command=lambda: mp.Y_values(text_result))
    
  #The basic interface
def basic_panel():
    btn_1.config(text="1", command=lambda: mp.mp.add_to_calculation(1,text_result))
    btn_2.config(text="2", command=lambda: mp.add_to_calculation(2,text_result))
    btn_3.config(text="3", command=lambda: mp.add_to_calculation(3,text_result))
    btn_4.config(text="4", command=lambda: mp.add_to_calculation(4,text_result))
    btn_5.config(text="5", command=lambda: mp.add_to_calculation(5,text_result))
    btn_6.config(text="6", command=lambda: mp.add_to_calculation(6,text_result))
    btn_7.config(text="7", command=lambda: mp.add_to_calculation(7,text_result))
    btn_8.config(text="8", command=lambda: mp.add_to_calculation(8,text_result))
    btn_9.config(text="9", command=lambda: mp.add_to_calculation(9,text_result))
    btn_open.config(text=")", command=lambda: mp.add_to_calculation(")",text_result))
    btn_closed.config(text="(", command=lambda: mp.add_to_calculation("(",text_result))
    
def graph_panel():
    ...
def scientific_panel():
 
    ...
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
        
    except Exception as e:
        mp.clear_field(text_result)
        text_result.insert(1.0, f"Error: {e}")


def Ask():
    try:
       file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
       if file_path:
           with open(file_path, 'r') as file:
               file_content = file.read()
               encoded_url=quote(file_content, encoding='utf-8')
               Request_url='http://api.wolframalpha.com/v2/query?appid=9YPG4R-X5Q4V5624E&input='+encoded_url+'&podstate=Result__Step-by-step%20solution&format=image'
               print(Request_url)
               response=requests.get(Request_url)
               if response.status_code == 200:
                # Parse the XML response
                roots = ET.fromstring(response.text)

                # Loop through subpods in the response
                for subpod in roots.findall(".//subpod"):
                    img_url = subpod.find(".//img").get("src")
                    
                    # Fetch image content from the URL
                    img_response = requests.get(img_url)

                    if img_response.status_code == 200:
                        # Use BytesIO to handle image content
                        img_content = BytesIO(img_response.content)

                        # Open the image using PIL
                        img = Image.open(img_content)

                        # Specify the desired file path to save the image
                        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

                        if save_path:
                            # Save the image to the specified path
                            img.save(save_path)
                            print(f"Image saved to: {save_path}")
                        else:
                            print("Saving canceled.")
                    else:
                        print(f"Error fetching image: {img_response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
           

root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

def calculator_resizer(event=None):
        root.update_idletasks()
        window_width=root.winfo_width()
        window_height=root.winfo_height()
        button_height =int(0.1*window_height)
        button_width=int(0.2*window_width)
        text_result_height=int(0.5*window_height)
        text_result_width=window_width
        font_size=int(min(window_width/30, window_height/30))
        widget_properties= {"font": ("Arial", font_size), "height": button_height, "width":button_width}
        text_result_properties={"font": ("Arial", font_size),"height":text_result_height,"width":text_result_width}
        for btn in buttons:
            btn.configure(**widget_properties)
        text_result.configure(**text_result_properties) 
# Configure rows and columns to expand with the window
root.grid_rowconfigure(0,weight=5)
for i in range(1,6):  # Assuming 7 rows in your layout
    root.grid_rowconfigure(i,weight=1)
for i in range(0,5):  # Assuming 7 columns in your layout
    root.grid_columnconfigure(i, weight=1)

btn_1=tk.Button(root, text="1", command=lambda: mp.mp.add_to_calculation(1,text_result),width=5, font=  ("Arial",14))
btn_1.grid(row=1,column=0)
btn_2=tk.Button(root, text="2", command=lambda: mp.add_to_calculation(2,text_result),width=5, font=  ("Arial",14))
btn_2.grid(row=1,column=1)
btn_3=tk.Button(root, text="3", command=lambda: mp.add_to_calculation(3,text_result),width=5, font=  ("Arial",14))
btn_3.grid(row=1,column=2)
btn_4=tk.Button(root, text="4", command=lambda: mp.add_to_calculation(4,text_result),width=5, font=  ("Arial",14))
btn_4.grid(row=2,column=0)
btn_5=tk.Button(root, text="5", command=lambda: mp.add_to_calculation(5,text_result),width=5, font=  ("Arial",14))
btn_5.grid(row=2,column=1)
btn_6=tk.Button(root, text="6", command=lambda: mp.add_to_calculation(6,text_result),width=5, font=  ("Arial",14))
btn_6.grid(row=2,column=2)
btn_7=tk.Button(root, text="7", command=lambda: mp.add_to_calculation(7,text_result),width=5, font=  ("Arial",14))
btn_7.grid(row=3,column=0)
btn_8=tk.Button(root, text="8", command=lambda: mp.add_to_calculation(8,text_result),width=5, font=  ("Arial",14))
btn_8.grid(row=3,column=1)
btn_9=tk.Button(root, text="9", command=lambda: mp.add_to_calculation(9,text_result),width=5, font=  ("Arial",14))
btn_9.grid(row=3,column=2)

btn_0=tk.Button(root, text="0", command=lambda: mp.add_to_calculation(0,text_result),width=5, font=  ("Arial",14))
btn_0.grid(row=4,column=1)
btn_plus=tk.Button(root, text="+", command=lambda: mp.add_to_calculation("+",text_result),width=5, font=  ("Arial",14))
btn_plus.grid(row=1,column=3)
btn_minus=tk.Button(root, text="-", command=lambda: mp.add_to_calculation("-",text_result),width=5, font=  ("Arial",14))
btn_minus.grid(row=2,column=3)
btn_div=tk.Button(root, text="/", command=lambda: mp.add_to_calculation("/",text_result),width=5, font=  ("Arial",14))
btn_div.grid(row=4,column=3)
btn_mul=tk.Button(root, text="*", command=lambda: mp.add_to_calculation("*",text_result),width=5, font=  ("Arial",14))
btn_mul.grid(row=3,column=3)
btn_open=tk.Button(root, text="(", command=lambda: mp.add_to_calculation("(",text_result),width=5, font=  ("Arial",14))
btn_open.grid(row=4,column=0,)
btn_closed=tk.Button(root, text=")", command=lambda: mp.add_to_calculation(")",text_result),width=5, font=  ("Arial",14))
btn_closed.grid(row=4,column=2)
btn_clear=tk.Button(root, text="C", command=lambda: mp.clear_field(text_result),width=11, font=  ("Arial",14))
btn_clear.grid(row=5,column=0,columnspan=2,sticky="nsew")
btn_equals=tk.Button(root, text="=", command=evaluate_calculation,width=11, font=  ("Arial",14))
btn_equals.grid(row=5,column=2)
btn_ask=tk.Button(root, text="Ask an AI" , command=lambda: Ask(),width=11, font=  ("Arial",14))
btn_ask.grid(row=5,column=4)
btn_seperate=tk.Button(root, text=",",command=lambda: mp.add_to_calculation(",",text_result),width=11, font=  ("Arial",14))
btn_seperate.grid(row=5,column=3)
btn_statistics=tk.Button(root, text="Statistics", command=lambda: Statistics_panel(), width=11, font=  ("Arial",14))
btn_statistics.grid(row=1,column=4)
btn_basic=tk.Button(root, text="Basic", command=lambda: basic_panel(), width=11, font=  ("Arial",14))
btn_basic.grid(row=2,column=4)
btn_scientific=tk.Button(root, text="scientific", command=lambda: scientific_panel(), width=11, font=  ("Arial",14))
btn_scientific.grid(row=3,column=4)
btn_graphs=tk.Button(root, text="Graphs", command=lambda: graph_panel(), width=11, font=  ("Arial",14))
btn_graphs.grid(row=4,column=4)
buttons=[btn_0,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_clear,btn_closed,btn_equals,btn_minus,btn_open,btn_div,btn_mul,btn_plus,btn_statistics,btn_basic,btn_scientific,btn_graphs,btn_ask,btn_seperate]
root.bind("<Configure>", calculator_resizer)
btn_graphs.bind("<Button-1>",lambda event:graph_panel())
btn_scientific.bind("<Button-1>",lambda event:scientific_panel())
btn_basic.bind("<Button-1>",lambda event:basic_panel())

root.bind("<Key>", on_key)
calculator_resizer()
root.mainloop()