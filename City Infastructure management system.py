# Task 1: Vehicle Registration System
# - Problem Statement: 
# Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner
        
    def update_owner(self,new_owner):
        self.owner = new_owner
        print(f"New owner has been updated: {new_owner}")


def main():
    vehicle1 = Vehicle(1, "sudan", "james")
    vehicle1.update_owner("sam")

main()