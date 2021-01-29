import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from quicksort import QuickSort
import re

root = tk.Tk()
root.geometry("450x300")

input_file = ""
output_file = ""
arr = []

qs = QuickSort()

def get_input_file():
    global input_file
    input_file = askopenfilename()
    retext = input_file
    retext = retext.split("/")
    n = len(retext)
    input_file_text.insert('end', retext[n-1])

def get_output_file():
    global output_file
    file = [('Text Document', '*.txt')]
    output_file = asksaveasfilename(filetypes = file, defaultextension = file)
    retext = output_file
    retext = retext.split("/")
    n = len(retext)
    output_file_text.insert('end', retext[n-1])


def get_input_text():
    f = open(input_file, "r")
    read = f.read()
    out = re.split(' |, |\*|\n',read)
    for x in out:
        arr.append(x)

def sort_save():
    if ".txt" in input_file:
        get_input_text()
        arr_lenght = len(arr)
        qs.quickSort(arr, 0, arr_lenght-1)
    else:
        status_text.config(text = "Enter a valid input file")
        return
    if ".txt" in output_file:
        f = open(output_file, "w")
        for i in range(arr_lenght):
            f.write('%s\n' % arr[i])
            print(arr[i])
        f.close()
        status_text.config(text = "Done!")
    else:
        status_text.config(text = "Enter a valid output file")

info = tk.Label(root, text = "Sort a .txt file seperated by space or ,")
info.grid(row=0,column=0)

input_button = tk.Button(root, text ="Input.txt", command = get_input_file,  width=10, height=2)
input_file_text = tk.Text(root, height = 3, width = 32)
input_button.grid(row=1,column=1)
input_file_text.grid(row=1,column=0, pady = (20, 20))

output_file_text = tk.Text(root, height = 3, width = 32)
output_button = tk.Button(root, text ="Output.txt", command = get_output_file,  width=10, height=2)
output_file_text.grid(row=2,column=0, padx = (25,25))
output_button.grid(row=2,column=1)

sort_button = tk.Button(root, text ="Sort", command = sort_save,  width=10, height=2)
sort_button.grid(row=3,column=1, pady = (20, 20))

status_text = tk.Label(root, text = "")
status_text.grid(row=3,column=0)

root.mainloop()
