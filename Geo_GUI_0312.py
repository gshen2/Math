import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Geometry Calculator')
        self.geometry('500x500')
        self.shape_select()

    def shape_select(self):
        shape_2D = tk.StringVar()
        shape_2D_chosen = ttk.Combobox(width=10, textvariable=shape_2D, state='readonly')
        shape_2D_chosen['values'] = ('Circle', 'Rectangle', 'Square')
        shape_2D_chosen.grid(row=0, column=1, columnspan=2)
        shape_2D_chosen.current(0)

    def widgets(self):
        label_shape = ttk.Label(self, text='Shape:')
        label_shape.grid(column=0, row=0, padx=10, pady=10)

        label_input = ttk.Label(self, text='Input:')
        label_input.grid(row=1, column=0, padx=10, pady=10)

        label_base = ttk.Label(self, text='Base = ')
        label_base.grid(row=1, column=1, padx=10, pady=10)
        base = tk.StringVar()
        base_box = ttk.Entry(width=10, textvariable=base)
        base_box.grid(row=1, column=2, padx=10, pady=10)

        label_height = ttk.Label(self, text='Height = ')
        label_height.grid(row=2, column=1, padx=10, pady=10)
        height = tk.StringVar()
        height = ttk.Entry(width=10, textvariable=height)
        height.grid(row=2, column=2, padx=10, pady=10)

        label_radius = ttk.Label(self, text='Radius = ')
        label_radius.grid(row=3, column=1, padx=10, pady=10)
        radius = tk.StringVar()
        radius_box = ttk.Entry(width=10, textvariable=radius)
        radius_box.grid(row=3, column=2, padx=10, pady=10)

        label_output = ttk.Label(self, text='Output:')
        label_output.grid(row=4, column=0, padx=10, pady=10)

        label_perimeter = ttk.Label(self, text='Perimeter')
        label_perimeter.grid(row=4, column=1, padx=10, pady=10)
        perimeter = tk.StringVar()
        perimeter_box = ttk.Entry(width=10, textvariable=perimeter, state='disabled')
        perimeter_box.grid(row=4, column=2, padx=10, pady=10)

        label_area = ttk.Label(self, text='Area')
        label_area.grid(row=5, column=1, padx=10, pady=10)
        area = tk.StringVar()
        area_box = ttk.Entry(width=10, textvariable=area, state='disabled')
        area_box.grid(row=5, column=2, padx=10, pady=10)

        label_circumference = ttk.Label(self, text='Perimeter')
        label_circumference.grid(row=6, column=1, padx=10, pady=10)
        circumference = tk.StringVar()
        circumference_box = ttk.Entry(width=10, textvariable=circumference, state='disabled')
        circumference_box.grid(row=6, column=2, padx=10, pady=10)


if __name__ == '__main__':
    Window().mainloop()
