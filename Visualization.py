import pygame
import tkinter as tk

from Simulation import Simulation

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class Visualization:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Planety")
        self.clock = pygame.time.Clock()

    def draw(self, planet_position):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit()
        self.screen.fill((255, 255, 255))

        cords = self.__convert_coords(planet_position)
        pygame.draw.circle(self.screen, (200, 0, 0), (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), self.r1)
        pygame.draw.circle(self.screen, (0, 0, 20), cords, self.r2)
        # self.clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    @staticmethod
    def __convert_coords(abs_coords):
        x = int(SCREEN_WIDTH / 2 + abs_coords[0])
        y = int(SCREEN_HEIGHT / 2 - abs_coords[1])
        return x, y


def run_visualisation():
    v1 = velocity_x.get()
    v2 = velocity_y.get()
    r1 = radiation1.get() or 0
    r2 = radiation2.get() or 0
    sp1 = start_position_x.get()
    sp2 = start_position_y.get()
    ts = time_step.get()
    m1 = mass1.get()
    m2 = mass2.get()

    v = Visualization(int(r1), int(r2))
    s = Simulation((float(eval(sp1)), float(eval(sp2))), (float(eval(v1)), float(eval(v2))), float(eval(ts)),
                   int(m1), int(m2), float(eval(r1)), float(eval(r2)))

    for i in s:
        v.draw(i)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("500x800")
    window.title("Dane")
    text = tk.StringVar()
    label = tk.Label(window, textvariable=text, padx=100, pady=50, font=("Times New Roman", 20))
    text.set("Wprowadź dane symulacji")
    label.pack()  # podpinanie kontrolki pod okno

    vals = {
        "vxtext": tk.StringVar(),
        "vytext": tk.StringVar(),
        "xtext": tk.StringVar(),
        "ytext": tk.StringVar(),
        "ttext": tk.StringVar(),
        "m1text": tk.StringVar(),
        "m2text": tk.StringVar(),
        "r1text": tk.StringVar(),
        "r2text": tk.StringVar()}

    velocity_x_desc = tk.Label(window, text="Prędkość początkowa Vx:").pack()
    velocity_x = tk.Entry(window, textvariable=vals["vxtext"], width=40)
    velocity_x.pack()

    label1 = tk.Label(window, textvariable=vals["vxtext"])
    label1.pack()  # podpinanie kontrolki pod okno

    velocity_y_desc = tk.Label(window, text="Prędkość początkowa Vy:").pack()
    velocity_y = tk.Entry(window, textvariable=vals["vytext"], width=40)
    velocity_y.pack()

    position_x_desc = tk.Label(window, text="Położenie planety nr 2, współrzędna x").pack()
    start_position_x = tk.Entry(window, textvariable=vals["xtext"], width=40)
    start_position_x.pack()

    position_y_desc = tk.Label(window, text="Położenie planety nr 2, współrzędna y").pack()
    start_position_y = tk.Entry(window, textvariable=vals["ytext"], width=40)
    start_position_y.pack()

    time_step_desc = tk.Label(window, text="Krok czasu:").pack()
    time_step = tk.Entry(window, textvariable=vals["ttext"], width=40)
    time_step.pack()

    mass1_desc = tk.Label(window, text="Masa nieruchomej planety").pack()
    mass1 = tk.Entry(window, textvariable=vals["m1text"], width=40)
    mass1.pack()

    mass2_desc = tk.Label(window, text="Masa ruchomej planety").pack()
    mass2 = tk.Entry(window, textvariable=vals["m2text"], width=40)
    mass2.pack()

    radiation1_desc = tk.Label(window, text="Promień nieruchomej planety").pack()
    radiation1 = tk.Entry(window, textvariable=vals["r1text"], width=40)
    radiation1.pack()

    radiation2_desc = tk.Label(window, text="Promień ruchomej planety").pack()
    radiation2 = tk.Entry(window, textvariable=vals["r2text"], width=40)
    radiation2.pack()

    break_label = tk.Label(window, text=" ")
    break_label.pack()

    run = tk.Button(window, text="Run", width=20, command=run_visualisation)
    run.pack()

    tk.mainloop()
