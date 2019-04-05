import tkinter as tk
from threading import Thread, Lock

import numpy as np

from Simulation import Simulation
from Visualization import Visualization


class Interface:
    def __init__(self):
        self.init_TkWindow()
        self.run = Lock()
        self.v = Visualization()
        self.update_planet(None)
        tk.mainloop()

    def update_planet(self, _):
        x = eval(self.vals["xtext"].get())
        y = eval(self.vals["ytext"].get())
        pos = np.array((x, y))
        vx = eval(self.vals["vxtext"].get())
        vy = eval(self.vals["vytext"].get())
        vel = np.array((vx, vy)) * 10
        r1 = eval(self.vals["r1text"].get())
        r2 = eval(self.vals["r2text"].get())
        rad = np.array((r1, r2))
        self.v.draw(pos, vel + pos, rad)

    def init_TkWindow(self):
        self.window = tk.Tk()
        self.window.geometry("500x800")
        self.window.title("Dane")
        text = tk.StringVar()
        label = tk.Label(self.window, textvariable=text, padx=100, pady=50, font=("Times New Roman", 20))
        text.set("Wprowadź dane symulacji")
        label.pack()  # podpinanie kontrolki pod okno

        self.vals = {
            "vxtext": tk.StringVar(value="20"),
            "vytext": tk.StringVar(value="10"),
            "xtext": tk.StringVar(value="50"),
            "ytext": tk.StringVar(value="50"),
            "ttext": tk.StringVar(value="1/60"),
            "m1text": tk.StringVar(value="10**10"),
            "m2text": tk.StringVar(value="100"),
            "r1text": tk.StringVar(value="20"),
            "r2text": tk.StringVar(value="10")}


        tk.Label(self.window, text="Położenie planety, współrzędna x").pack()
        start_position_x = tk.Entry(self.window, textvariable=self.vals["xtext"], width=40)
        start_position_x.pack()
        tk.Label(self.window, text="Położenie planety, współrzędna y").pack()
        start_position_y = tk.Entry(self.window, textvariable=self.vals["ytext"], width=40)
        start_position_y.pack()

        tk.Label(self.window, text="Prędkość początkowa Vx:").pack()
        velocity_x = tk.Entry(self.window, textvariable=self.vals["vxtext"], width=40)
        velocity_x.pack()
        tk.Label(self.window, text="Prędkość początkowa Vy:").pack()
        velocity_y = tk.Entry(self.window, textvariable=self.vals["vytext"], width=40)
        velocity_y.pack()

        tk.Label(self.window, text="Krok czasu:").pack()
        time_step = tk.Entry(self.window, textvariable=self.vals["ttext"], width=40)
        time_step.pack()
        tk.Label(self.window, text="Masa nieruchomej planety").pack()
        mass1 = tk.Entry(self.window, textvariable=self.vals["m1text"], width=40)
        mass1.pack()
        tk.Label(self.window, text="Masa ruchomej planety").pack()
        mass2 = tk.Entry(self.window, textvariable=self.vals["m2text"], width=40)
        mass2.pack()
        tk.Label(self.window, text="Promień nieruchomej planety").pack()
        radiation1 = tk.Entry(self.window, textvariable=self.vals["r1text"], width=40)
        radiation1.pack()
        tk.Label(self.window, text="Promień ruchomej planety").pack()
        radiation2 = tk.Entry(self.window, textvariable=self.vals["r2text"], width=40)
        radiation2.pack()
        break_label = tk.Label(self.window, text=" ")
        break_label.pack()

        start_position_x.focus_set()
        run = tk.Button(self.window, text="Run", width=20, command=self.start_simulation)
        run.pack()

        reset = tk.Button(self.window, text = "Reset", width=20, command=self.start_simulation)
        reset.pack()

        self.window.bind('<KeyRelease>', self.update_planet)

    def __start_simulation(self):
        v1 = eval(self.vals["vxtext"].get()) or 0
        v2 = eval(self.vals["vytext"].get()) or 0
        r1 = eval(self.vals["r1text"].get()) or 0
        r2 = eval(self.vals["r2text"].get()) or 0
        sp1 = eval(self.vals["xtext"].get()) or 0
        sp2 = eval(self.vals["ytext"].get()) or 0
        ts = eval(self.vals["ttext"].get()) or 0
        m1 = eval(self.vals["m1text"].get()) or 0
        m2 = eval(self.vals["m2text"].get()) or 0

        s = Simulation((float((sp1)), float((sp2))), (float((v1)), float((v2))), float((ts)),
                       int(m1), int(m2), float((r1)), float((r2)))

        self.v = Visualization()
        for i in s:
            self.v.draw(i, rad=(r1, r2))

    def start_simulation(self):
        self.t=Thread(target=self.__start_simulation)
        self.t.start()

    def restart_simulation(self):
        self.start_simulation()


if __name__ == "__main__":
    i = Interface()
