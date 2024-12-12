class Bus:
    def __init__(self) -> None:
        self._speed = 0
        self.max_speed = 120
        self.max_seats = 60
        self._passengers = list()
        self._has_empty_seats = True
        self._places = dict()

    def __str__(self) -> str:
        return f"""
        Speed: {self._speed},
        Max Speed: {self.max_speed},
        Max Seats: {self.max_seats},
        Passenders surnames: {self._passengers},
        Has empty seats: {self._has_empty_seats},
        Places: {self._places}
        """
    
    def __iadd__(self, passenger_surname: str):
        self.boarding_in(passenger_surname)
        return self
    
    def __isub__(self, passenger_surname: str):
        self.boarding_out(passenger_surname)
        return self

    def __contains__(self, passenger_surname: str) -> bool:
        return passenger_surname in self._passengers

    def speed_up(self, value: int) -> None:
        self._speed += value

    def speed_down(self, value: int) -> None:
        self._speed -= value

    def boarding_in(self, *passengers) -> None:
        if not self._has_empty_seats:
            print("The bus is full")
            return
        elif self.max_seats - len(self._passengers) < len(passengers):
            print(f"Not enough empty places. Empty: {self.max_seats - len(self._passengers)}")
            return
        
        for passenger in passengers:
            self._passengers.append(passenger)
            self._places[self.__next_index()] = passenger
        
        self._has_empty_seats = self.max_seats > len(self._passengers)

    def __next_index(self) -> int:
        for i in range(0, self.max_seats):
            if i not in self._places.keys():
                return i

    def boarding_out(self, *passengers) -> None:
        self._passengers = [
            passenger for passenger in self._passengers if passenger not in passengers
        ]
        self._places = {
            key: value for key, value in self._places.items() if value not in passengers
        }
        self._has_empty_seats = self.max_seats > len(self._places)

bus = Bus()
bus.speed_up(40)
print(bus)

bus.speed_down(40)
bus.boarding_in("surn_1", "surn_2", "surn_3", "surn_4")
print(bus)

bus.boarding_out("surn_2", "surn_3")
print(bus)

bus.speed_up(20)
bus.boarding_in("surn_5", "surn_6", "surn_7")
print(bus)

surn = "surn_6"
print(f"Person {surn} in list ? {surn in bus}")
bus -= surn
print(bus)
print(f"Person {surn} in list ? {surn in bus}")

surn = "surn_8"
print(f"Person {surn} in list ? {surn in bus}")
bus += surn
print(bus)
print(f"Person {surn} in list ? {surn in bus}")
