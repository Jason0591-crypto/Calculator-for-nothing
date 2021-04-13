import random
import three_d_shape_calculations


def main_calculator():
    while True:
        print("1. Calculate 3D shapes\n2. Calculate 2D shapes")
        choice1 = str(input("Enter the type of process you want to run, or press E to exit"))
        if choice1 == "1":
            three_d_shapes_calculator()
        # elif choice1 == "2":
        #     two_d_shapes_calculator()
        elif choice1 == "e" or "E":
            break
        else:
            print("--ERROR--")


def three_d_shapes_calculator():
    while True:
        def calculate_surface_area():
            while True:
                # Print out the choices
                print("1. Cylinder\n2. Sphere\n3. Cone\n4. ")

                # The choice of the user
                choice3 = str(input("Enter the shape you want to calculate, or press E to go back"))

                # Determine the choice of the user and call the corresponding function
                if choice3 == "1":
                    three_d_shape_calculations.cylinder_surface_area()
                elif choice3 == "2":
                    three_d_shape_calculations.sphere_surface_area()
                elif choice3 == "3":
                    three_d_shape_calculations.cone_surface_area()
                elif choice3 == "E" or "e":
                    break
                else:
                    print("--ERROR--")

        def calculate_volume():
            while True:
                # Print out the choices
                print("1. Cylinder\n2. Sphere\n3. Cone\n4. ")

                # The choice of the user
                choice3 = str(input("Enter the shape you want to calculate, or press E to go back"))

                # Determine the choice of the user and call the corresponding function
                if choice3 == "1":
                    three_d_shape_calculations.cylinder_volume()
                elif choice3 == "2":
                    three_d_shape_calculations.sphere_volume()
                elif choice3 == "3":
                    three_d_shape_calculations.cone_volume()
                elif choice3 == "E" or "e":
                    break
                else:
                    print("--ERROR--")

        print("1. Calculate surface areas\n2. Calculate volumes\n3. ")
        choice2 = str(input("Enter the type of process you want to run, or press E to exit"))

        if choice2 == "1":
            calculate_surface_area()
        elif choice2 == "2":
            calculate_volume()
        elif choice2 == "e" or "E":
            break
        else:
            print("--ERROR--")


# def two_d_shapes_calculator():
#     while True:
#         print("1. Calculate perimeters\n2. Calculate areas")
#         choice2 = str(input("Enter the type of process you want to run, or press E to exit"))
#         break


main_calculator()
