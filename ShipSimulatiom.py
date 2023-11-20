# Richard Boamah
# Lab 6 Data Structure - Python

import random
from tabulate import tabulate
from faker import Faker
import time

class Passenger:
    def __init__(self, name, pass_color):
        self.name = name
        self.pass_color = pass_color

class Room:
    def __init__(self, deck, room_number):
        self.deck = deck
        self.room_number = room_number

# Initialize the cruise ship simulation
class CruiseShipSimulation:
    def __init__(self):
        self.passenger_line = []  # FIFO Queue for passenger line
        self.rooms_by_deck = {
            'A': [Room('A', i) for i in range(1, 21)],
            'B': [Room('B', i) for i in range(1, 101)],
            'C': [Room('C', i) for i in range(1, 201)],
            'D': [Room('D', i) for i in range(1, 501)]
        }
        self.room_assignments = []  # LIFO Stack for room assignments

# Generate a random list of passengers with names and pass colors
    def generate_passenger_line(self, num_passengers):
        fake = Faker()
        pass_colors = ['GREEN', 'BLUE', 'ORANGE', 'RED (Staff)']

        for _ in range(num_passengers):
            name = fake.name()
            pass_color = random.choice(pass_colors)
            self.passenger_line.append(Passenger(name, pass_color))

# Process passengers in the line and assign rooms
    def process_passengers(self):
        while self.passenger_line:
            passenger = self.passenger_line.pop(0)  # FIFO
            self.process_passenger(passenger)

# Determine the deck based on pass color
    def process_passenger(self, passenger):
        pass_color = passenger.pass_color

        if pass_color == 'GREEN':
            deck = 'A'
        elif pass_color == 'BLUE':
            deck = 'B'
        elif pass_color == 'ORANGE':
            deck = 'C'
        else:
            deck = 'D'

# Get an available room on the specified deck
        room = self.get_available_room(deck)
        if room:             # Assign the room and print the simulation step
            self.room_assignments.insert(0, (passenger.name, pass_color, room.deck, room.room_number))
            self.print_simulation_step(passenger, room)
            time.sleep(0.5) 

# Get an available room on the specified deck
    def get_available_room(self, deck):
        if not self.rooms_by_deck[deck]:
            return None

        # Ensure unique room assignment on the same deck
        room = random.choice(self.rooms_by_deck[deck])
        self.rooms_by_deck[deck] = [r for r in self.rooms_by_deck[deck] if r.room_number != room.room_number]
        return room

    def print_simulation_step(self, passenger, room):
        print(f"{passenger.name} ({passenger.pass_color}) checking in and assigned to Room {room.room_number} on Deck {room.deck}")

    def verify_availability(self):
        for room_list in self.rooms_by_deck.values():
            if any(room_list):
                print(f"Warning: Not all rooms have been assigned on Deck {room_list[0].deck}")

# Print the simulation step
    def print_room_manifest(self):
        table_headers = ['Passenger Name', 'Pass Color', 'Deck', 'Room Number']
        print(tabulate(self.room_assignments, headers=table_headers, tablefmt='grid'))

if __name__ == "__main__":
    cruise_ship = CruiseShipSimulation()
    cruise_ship.generate_passenger_line(820)
    cruise_ship.process_passengers()
    cruise_ship.verify_availability()
    cruise_ship.print_room_manifest()
