import numpy as np
from BoomException import BoomException


class Simulation:
    gravitational_constant = 6.67408 * 10 ** -11

    def __init__(self,
                 start_position,
                 start_velocity,
                 time_step,
                 mass1,  # masa nieruchomego ciała
                 mass2,
                 radiance1,
                 radiance2):
        self.curr_position = np.array(start_position)
        self.curr_velocity = np.array(start_velocity)
        self.time_step = time_step
        self.mass1 = mass1
        self.mass2 = mass2
        self.radiance1 = radiance1
        self.radiance2 = radiance2

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
    def __vector_direction(self):
        return -np.abs(self.curr_position) / self.curr_position

    # rozłożenie wektora przyspieszenia
    def __vector_magnitude_and_direction_to_components(self):
        return np.abs(self.curr_position) * self.__gravitional_acceleration() / self.__distance_between_centres() * self.__vector_direction()

    # przyrost prędkości w trakcie kroku czasu
    def __velocity_growth(self):
        return self.__vector_magnitude_and_direction_to_components() * self.time_step

    # average velocity growth
    def __avg_velocity(self):
        return self.curr_velocity + 0.5 * self.__velocity_growth()

    # nowa prędkość
    def __update_velocity(self):
        self.curr_velocity += self.__velocity_growth()

    # policz zmianę pozycji w czasie tego time-stepu
    def __calculate_position_offset(self):
        return self.__avg_velocity() * self.time_step

    # zwracaj położenie planety w kolejnej klatce symulacji, tj po minięciu time-stepu
    def __next__(self):
        self.curr_position = self.curr_position + self.__calculate_position_offset()
        self.__update_velocity()
        if self.__distance_between_centres() < self.radiance1 + self.radiance2: raise BoomException('Boom!')
        return self.curr_position

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Simulation((10, 10), (10, 10), 1, 1000, 100, 10, 10)
    print(s._Simulation__distance_between_centres())
    print(s._Simulation__gravitation_force())
    print(s._Simulation__gravitional_acceleration())
    print(s._Simulation__vector_direction())
