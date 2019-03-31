from typing import Tuple
import numpy as np
from BoomException import BoomException


class Simulation:
    gravitational_constant = 6.67408 * 10 ** -11

    # ... możliwe że kolejne takie pola będą potrzeben, np na przyspieszenie. Są to listy dwulementowe bo masz Vx, Vy

    def __init__(self,
                 start_position=np.array((10, 10)),
                 start_velocity=np.array((0, 0)),
                 time_step=1 / 60,
                 mass1=100000000000,  # masa nieruchomego ciała
                 mass2=100000000000,
                 radiance2=1,
                 radiance1=10):
        self.curr_position = start_position
        self.curr_velocity = start_velocity
        self.time_step = time_step
        self.mass1 = mass1
        self.mass2 = mass2
        self.radiance2 = radiance2
        self.radiance1 = radiance1

    # odleglosc srodkow planet R
    def __distance_between_centres(self):
        return np.hypot(self.curr_position[0], self.curr_position[1])

    # sila grawitacji
    def __gravitation_force(self):
        return self.gravitational_constant * self.mass1 * self.mass2 / self.__distance_between_centres() ** 2

    # przyspieszenie grawitacyjne
    def __gravitional_acceleration(self):
        return self.gravitational_constant * self.mass1 / self.__distance_between_centres() ** 2

    # zwrot_wektora
    def __vector_return(self):
        return np.abs(self.curr_position)/self.curr_position

    # rozłożenie wektora przyspieszenia
    def __vector_magnitude_and_direction_to_components(self):
        return np.abs(self.curr_position) * self.__gravitional_acceleration() / self.__distance_between_centres() * self.__vector_return()

    # przyrost prędkości w trakcie kroku czasu
    def __velocity_growth(self):
        return self.__vector_magnitude_and_direction_to_components() * self.time_step

    # wypadkowa prędkości
    def __resultant_of_velocity(self):
        return self.__vector_magnitude_and_direction_to_components() + self.curr_velocity

    # policz zmianę pozycji w czasie tego time-stepu
    def __calculate_position_offset(self):
        return self.__resultant_of_velocity() * self.time_step

    # zwracaj położenie planety w kolejnej klatce symulacji, tj po minięciu time-stepu
    def __next__(self):
        self.curr_position = self.curr_position + self.__calculate_position_offset()
        if self.__distance_between_centres() < self.radiance1 + self.radiance2: raise BoomException('Boom!')
        return self.curr_position

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Simulation()
    for i in s:
        print(i)
