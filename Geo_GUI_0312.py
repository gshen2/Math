import Geo_2D
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Geometry Calculator')
        self.resizable(False, False)
        self.tabs_2d_3d()

    def tabs_2d_3d(self):
        tabControl = ttk.Notebook(self)
        self._2d = ttk.Frame(tabControl)
        self._3d = ttk.Frame(tabControl)
        tabControl.add(self._2d, text='2D Shapes')
        tabControl.add(self._3d, text='3D Objects')
        tabControl.pack(expand=1, fill='both')
        self.tabs_2d()
        self.tabs_3d()

    def tabs_2d(self):
        tabControl = ttk.Notebook(self._2d)
        self.square = ttk.Frame(tabControl)
        self.rectangle = ttk.Frame(tabControl)
        self.circle = ttk.Frame(tabControl)
        self.triangleSSS = ttk.Frame(tabControl)
        tabControl.add(self.square, text='Square')
        tabControl.add(self.rectangle, text='Rectangle')
        tabControl.add(self.circle, text='Circle')
        tabControl.add(self.triangleSSS, text='Triangle_SSS')
        tabControl.pack(expand=1, fill='both')
        self.shapes_2d()

    def tabs_3d(self):
        tabControl = ttk.Notebook(self._3d)
        self.cube = ttk.Frame(tabControl)
        self.cuboid = ttk.Frame(tabControl)
        self.sphere = ttk.Frame(tabControl)
        tabControl.add(self.cube, text='Cube')
        tabControl.add(self.cuboid, text='Cuboid')
        tabControl.add(self.sphere, text='Sphere')
        tabControl.pack(expand=1)
        self.shapes_3d()

    def shapes_2d(self):
        self.sq()
        self.rect()
        self.circ()
        self.tri_SSS()

    def tri_SSS(self):
        lbl_tri_s1 = ttk.Label(self.triangleSSS, text='Side 1 = ')
        lbl_tri_s1.grid(row=0, column=0)
        self.tri_s1 = tk.StringVar()
        entry_tri_s1 = ttk.Entry(self.triangleSSS, width=10, textvariable=self.tri_s1)
        entry_tri_s1.grid(row=0, column=1)

        lbl_tri_s2 = ttk.Label(self.triangleSSS, text='Side 2 = ')
        lbl_tri_s2.grid(row=1, column=0)
        self.tri_s2 = tk.StringVar()
        entry_tri_s2 = ttk.Entry(self.triangleSSS, width=10, textvariable=self.tri_s2)
        entry_tri_s2.grid(row=1, column=1)

        lbl_tri_s3 = ttk.Label(self.triangleSSS, text='Side 3 = ')
        lbl_tri_s3.grid(row=2, column=0)
        self.tri_s3 = tk.StringVar()
        entry_tri_s3 = ttk.Entry(self.triangleSSS, width=10, textvariable=self.tri_s3)
        entry_tri_s3.grid(row=2, column=1)

        button = ttk.Button(self.triangleSSS, text='Calculate', command=self.calc_tri_SSS)
        button.grid(row=3, column=0, columnspan=4, sticky='NSEW', padx=20, pady=20)

        lbl_tri_SSS_area = ttk.Label(self.triangleSSS, text='area = ')
        lbl_tri_SSS_area.grid(row=0, column=2)
        self.tri_SSS_area = tk.StringVar()
        entry_tri_SSS_area = ttk.Entry(self.triangleSSS, width=10, textvariable=self.tri_SSS_area, state='disable')
        entry_tri_SSS_area.grid(row=0, column=3)

        lbl_tri_SSS_peri = ttk.Label(self.triangleSSS, text='perimeter = ')
        lbl_tri_SSS_peri.grid(row=1, column=2)
        self.tri_SSS_peri = tk.StringVar()
        entry_tri_SSS_peri = ttk.Entry(self.triangleSSS, width=10, textvariable=self.tri_SSS_peri, state='disable')
        entry_tri_SSS_peri.grid(row=1, column=3)

    def calc_tri_SSS(self):
        self.tri_SSS_area.set(Geo_2D.Triangle_SSS(side_1=float(self.tri_s1.get()), side_2=float(self.tri_s2.get()), side_3=float(self.tri_s3.get())).area())
        self.tri_SSS_peri.set(Geo_2D.Triangle_SSS(side_1=float(self.tri_s1.get()), side_2=float(self.tri_s2.get()), side_3=float(self.tri_s3.get())).perimeter())

    def sq(self):
        lbl_sq_base = ttk.Label(self.square, text='base = ')
        lbl_sq_base.grid(row=0, column=0)
        self.sq_base = tk.StringVar()
        entry_sq_base = ttk.Entry(self.square, width=10, textvariable=self.sq_base)
        entry_sq_base.grid(row=0, column=1)
        entry_sq_base.focus()

        button = ttk.Button(self.square, text='Calculate', command=self.calc_sq)
        button.grid(row=3, column=0, columnspan=4, sticky='NSEW', padx=20, pady=20)

        lbl_sq_area = ttk.Label(self.square, text='area = ')
        lbl_sq_area.grid(row=0, column=2)
        self.sq_area = tk.StringVar()
        entry_sq_area = ttk.Entry(self.square, width=10, textvariable=self.sq_area, state='disable')
        entry_sq_area.grid(row=0, column=3)

        lbl_sq_peri = ttk.Label(self.square, text='perimeter = ')
        lbl_sq_peri.grid(row=1, column=2)
        self.sq_peri = tk.StringVar()
        entry_sq_peri = ttk.Entry(self.square, width=10, textvariable=self.sq_peri, state='disable')
        entry_sq_peri.grid(row=1, column=3)

    def calc_sq(self):
        self.sq_area.set(Geo_2D.Square(float(self.sq_base.get())).area())
        self.sq_peri.set(Geo_2D.Square(float(self.sq_base.get())).perimeter())

    def rect(self):
        lbl_rect_base = ttk.Label(self.rectangle, text='base = ')
        lbl_rect_base.grid(row=0, column=0)
        self.rect_base = tk.StringVar()
        entry_rect_base = ttk.Entry(self.rectangle, textvariable=self.rect_base)
        entry_rect_base.grid(row=0, column=1)

        lbl_rect_h = ttk.Label(self.rectangle, text='height = ')
        lbl_rect_h.grid(row=1, column=0)
        self.rect_h = tk.StringVar()
        entry_rect_h = ttk.Entry(self.rectangle, textvariable=self.rect_h)
        entry_rect_h.grid(row=1, column=1)

        button = ttk.Button(self.rectangle, text='Calculate', command=self.calc_rect)
        button.grid(row=3, column=0, columnspan=2)

        lbl_rect_area = ttk.Label(self.rectangle, text='area = ')
        lbl_rect_area.grid(row=4, column=0)
        self.rect_area = tk.StringVar()
        entry_rect_area = ttk.Entry(self.rectangle, textvariable=self.rect_area, state='disable')
        entry_rect_area.grid(row=4, column=1)

        lbl_rect_peri = ttk.Label(self.rectangle, text='perimeter = ')
        lbl_rect_peri.grid(row=5, column=0)
        self.rect_peri = tk.StringVar()
        entry_rect_peri = ttk.Entry(self.rectangle, textvariable=self.rect_peri, state='disable')
        entry_rect_peri.grid(row=5, column=1)

    def calc_rect(self):
        self.rect_area.set(Geo_2D.Rectangle(
            base=float(self.rect_base.get()),
            height=float(self.rect_h.get())
        ).area())
        self.rect_peri.set(Geo_2D.Rectangle(
            base=float(self.rect_base.get()),
            height=float(self.rect_h.get())
        ).perimeter())

    def circ(self):
        lbl_r = ttk.Label(self.circle, text='radius = ')
        lbl_r.grid(row=0, column=0)
        self.r = tk.StringVar()
        entry_r = ttk.Entry(self.circle, textvariable=self.r)
        entry_r.grid(row=0, column=1)

        button = ttk.Button(self.circle, text='Calculate', command=self.calc_circ)
        button.grid(row=3, column=0, columnspan=2)

        lbl_circ_area = ttk.Label(self.circle, text='area = ')
        lbl_circ_area.grid(row=4, column=0)
        self.circ_area = tk.StringVar()
        entry_circ_area = ttk.Entry(self.circle, textvariable=self.circ_area, state='disable')
        entry_circ_area.grid(row=4, column=1)

        lbl_circ_circum = ttk.Label(self.circle, text='perimeter = ')
        lbl_circ_circum.grid(row=5, column=0)
        self.circ_circum = tk.StringVar()
        entry_circ_circum = ttk.Entry(self.circle, textvariable=self.circ_circum, state='disable')
        entry_circ_circum.grid(row=5, column=1)

    def calc_circ(self):
        self.circ_area.set(round(Geo_2D.Circle(float(self.r.get())).area(), 3))
        self.circ_circum.set(round(Geo_2D.Circle(float(self.r.get())).circumference(), 3))

    def shapes_3d(self):
        pass

    def calculate(self):
        pass


if __name__ == '__main__':
    Window().mainloop()
