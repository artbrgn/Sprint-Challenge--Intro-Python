# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    pass


class FlightVehicle(Vehicle):
    pass
# Vehicle is the parent class


class Starship(FlightVehicle):
    pass
# FlightVehicle is the parent class


class Airplane(FlightVehicle):
    pass
# FlightVehicle is the parent class


class GroundVehicle(Vehicle):
    pass
# Vehicle is the parent class


class Car(GroundVehicle):
    pass
# GroundVehicle is the parent class


class Motorcycle(GroundVehicle):
    pass
# GroundVehicle is the parent class
