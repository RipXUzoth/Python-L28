class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def show_details(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Seating Capacity: {self.capacity}")


class Bus(Vehicle):
    def __init__(self, name, capacity, fare_per_person):
        super().__init__(name, capacity)
        self.fare_per_person = fare_per_person

    def calculate_total_fare(self, passengers):
        if passengers > self.capacity:
            print("Error: Number of passengers exceeds capacity!")
            return None
        total_fare = passengers * self.fare_per_person
        return total_fare


# Example usage
bus1 = Bus("City Express", 40, 25)  # fare per person = 25
bus1.show_details()
passenger_count = 30
total_fee = bus1.calculate_total_fare(passenger_count)

if total_fee is not None:
    print(f"Total fare for {passenger_count} passengers: ₹{total_fee}")
