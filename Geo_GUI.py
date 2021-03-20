import Geo_2D
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Geometry Calculator')
        self.tabs_2d_3d()

    def tabs_2d_3d(self):
        tabs = ttk.Notebook(self)
        self._2d = ttk.Frame(tabs)
        self._3d = ttk.Frame(tabs)
        tabs.add(self._2d, text='2D')
        tabs.add(self._3d, text='3D')
        tabs.pack(expand=1, fill='both')
        self.tab_2d()
        self.tab_3d()

    def tab_2d(self):
        tabs = ttk.Notebook(self._2d)
        self.sq = ttk.Frame(tabs)
        self.rect = ttk.Frame(tabs)
        self.circ = ttk.Frame(tabs)
        tabs.add(self.sq, text='Square')
        tabs.add(self.rect, text='Rectangle')
        tabs.add(self.circ, text='Circle')
        tabs.pack(expand=1, fill='both')
        self.square()

    def square(self):
        # Base
        lbl_base = ttk.Label(self.sq, text='Base =')
        lbl_base.grid(row=0, column=0)
        self.sq_base = tk.StringVar()
        entry_base = ttk.Entry(self.sq, width=7, textvariable=self.sq_base)
        entry_base.grid(row=0, column=1)
        entry_base.focus()

        # Area
        lbl_area = ttk.Label(self.sq, text='Area =')
        lbl_area.grid(row=0, column=2, sticky='E')
        self.sq_area = tk.StringVar()
        entry_area = ttk.Entry(self.sq, width=7, textvariable=self.sq_area, state='disable')
        entry_area.grid(row=0, column=3)

        # Perimeter
        lbl_per = ttk.Label(self.sq, text='Perimeter =')
        lbl_per.grid(row=1, column=2)
        self.sq_per = tk.StringVar()
        entry_per = ttk.Entry(self.sq, width=7, textvariable=self.sq_per, state='disable')
        entry_per.grid(row=1, column=3)

        # Calculate Button
        button = ttk.Button(self.sq, text='Calculate', command=self.calc_sq)
        button.grid(row=2, column=0, columnspan=4, sticky='NSEW', padx=20, pady=10)

    def calc_sq(self):
        self.sq_area.set(Geo_2D.Square(float(self.sq_base.get())).area())
        self.sq_per.set(Geo_2D.Square(float(self.sq_base.get())).perimeter())

    def tab_3d(self):
        pass


if __name__ == '__main__':
    Window().mainloop()
