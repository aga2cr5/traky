# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Class to describe a car object
#​‌‌‌​​​​‌‌​‌‌‌​ A car has the following attributes: max_tank, tank, consumption, mileage and id

class Car:

    def __init__(self, consumption, name = "unregistered vehicle"):
        self.max_tank = 40
        self.tank = self.max_tank # tank is full when delivered from factory
        self.consumption = consumption
        self.mileage = 0.0
        self.id = name

    #​‌‌‌​​​​‌‌​‌‌‌​ Return mileage
    def get_mileage(self):
        return self.mileage

    #​‌‌‌​​​​‌‌​‌‌‌​ Return tank
    def get_tank_level(self):
        return self.tank

    #​‌‌‌​​​​‌‌​‌‌‌​ Drive the wanted distance
    def drive(self, distance):
        max_distance = self.tank / self.consumption * 100
        if max_distance < distance:
            self.mileage += max_distance
            self.tank = 0
            return max_distance
        else:
            self.mileage += distance
            self.tank -= distance * self.consumption / 100
            return distance

    #​‌‌‌​​​​‌‌​‌‌‌​ Refuels the car
    def refuel(self, amount):
        self.tank += min(amount, self.max_tank - self.tank)
        return self.tank




#​‌‌‌​​​​‌‌​‌‌‌​ Class to describe a car track
#​‌‌‌​​​​‌‌​‌‌‌​ A car track has the following attributes: name, distance, cars and nof_cars
#​‌‌‌​​​​‌‌​‌‌‌​ Fill in the missing methods

class CarTrack:

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance    # distance of the car track
        self.cars = []              # cars driving on the track
        self.nof_cars = 0

    #​‌‌‌​​​​‌‌​‌‌‌​ Returns the distance of the car track
    def get_distance(self):
        return self.distance

    #​‌‌‌​​​​‌‌​‌‌‌​ Returns the list containing the cars in the car track
    def get_cars(self):
        return self.cars

    #​‌‌‌​​​​‌‌​‌‌‌​ Returns the number of cars in the car track
    def get_nof_cars(self):
        return self.nof_cars


    def add_car(self, car):
        """ Add a car to the car track and return the number of cars in the track """
        self.cars.append(car)
        self.nof_cars += 1
        return self.nof_cars


    def count_avg_consumption(self):
        """ Count and return the average consumption of the race cars """
        kulutus = 0
        for car in self.cars:
            kulutus += car.consumption
        kesk_kulutus = kulutus / self.nof_cars
        return kesk_kulutus



    def get_winner(self):
        """ Return the car with the biggest mileage """
        """ Use of built-in functions such as max() is prohibited """
        best = 0
        winner = None
        for car in self.cars:
            if Car.get_mileage(car) > best:
                best = Car.get_mileage(car)
                winner = car
        return winner



    def count_rounds(self, car):
        """ Count how many rounds a car drove, round down to the nearest integer """
        rounds = int(Car.get_mileage(car) / self.distance)
        return rounds


def main():
    track = CarTrack("Monaco", 30)
    print(track.get_distance())

    car_1 = Car(10.6, "ZZZ-123")
    car_2 = Car(8.1, "ABC-245")
    car_3 = Car(13.8, "FOO-634")
    car_4 = Car(14.2, "JKL-375")

    cars = [car_1, car_2, car_3, car_4]
    for car in cars:
        track.add_car(car)

    car_1.drive(479)
    car_2.drive(472)
    car_3.drive(531)
    car_4.drive(317)

    """HALUTUT TIEDOT"""
    for car in cars:
        print(car.get_mileage())

    winner = track.get_winner()
    print(winner)
    print(track.count_rounds(winner))
    print(track.count_avg_consumption())

if __name__ == "__main__":
    main()
