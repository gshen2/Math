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
        self.rectangle()
        self.circle()

    def rectangle(self):
        # Base
        lbl_base = ttk.Label(self.rect, text='Base =')
        lbl_base.grid(row=0, column=0)
        self.rect_base = tk.StringVar()
        entry_base = ttk.Entry(self.rect, width=7, textvariable=self.rect_base)
        entry_base.grid(row=0, column=1)

        # Height
        lbl_h = ttk.Label(self.rect, text='Height =')
        lbl_h.grid(row=1, column=0)
        self.rect_h = tk.StringVar()
        entry_h = ttk.Entry(self.rect, width=7, textvariable=self.rect_h)
        entry_h.grid(row=1, column=1)

        # Area
        lbl_area = ttk.Label(self.rect, text='Area =')
        lbl_area.grid(row=0, column=2, sticky='E')
        self.rect_area = tk.StringVar()
        entry_area = ttk.Entry(self.rect, width=7, textvariable=self.rect_area, state='disable')
        entry_area.grid(row=0, column=3)

        # Perimeter
        lbl_per = ttk.Label(self.rect, text='Perimeter =')
        lbl_per.grid(row=1, column=2)
        self.rect_per = tk.StringVar()
        entry_per = ttk.Entry(self.rect, width=7, textvariable=self.rect_per, state='disable')
        entry_per.grid(row=1, column=3)

        # Calculate Button
        button = ttk.Button(self.rect, text='Calculate', command=self.calc_rect)
        button.grid(row=2, column=0, columnspan=4, sticky='NSEW', padx=20, pady=10)

    def calc_rect(self):
        self.rect_area.set(Geo_2D.Rectangle(
            float(self.rect_base.get()),
            float(self.rect_h.get())
        ).area())
        self.rect_per.set(Geo_2D.Rectangle(
            float(self.rect_base.get()),
            float(self.rect_h.get())
        ).perimeter())

    def circle(self):
        # Radius
        lbl_r = ttk.Label(self.circ, text='Radius =')
        lbl_r.grid(row=0, column=0)
        self.circ_r = tk.StringVar()
        entry_r = ttk.Entry(self.circ, width=7, textvariable=self.circ_r)
        entry_r.grid(row=0, column=1)

        # Area
        lbl_area = ttk.Label(self.circ, text='Area =')
        lbl_area.grid(row=0, column=2, sticky='E')
        self.circ_area = tk.StringVar()
        entry_area = ttk.Entry(self.circ, width=7, textvariable=self.circ_area, state='disable')
        entry_area.grid(row=0, column=3)

        # Circumference
        lbl_c = ttk.Label(self.circ, text='Circumference =')
        lbl_c.grid(row=1, column=2)
        self.circ_c = tk.StringVar()
        entry_c = ttk.Entry(self.circ, width=7, textvariable=self.circ_c, state='disable')
        entry_c.grid(row=1, column=3)

        button = ttk.Button(self.circ, text='Calculate', command=self.calc_circ)
        button.grid(row=2, column=0, columnspan=4, sticky='NSEW', padx=20, pady=10)

    def calc_circ(self):
        self.circ_area.set(Geo_2D.Circle(float(self.circ_r.get())).area())
        self.circ_c.set(Geo_2D.Circle(float(self.circ_r.get())).circumference())

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
