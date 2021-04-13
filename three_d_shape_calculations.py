import math

# Calculator for the surface area of a cylinder
def cylinder_surface_area():
    height = float(input("Enter the height"))
    radius = float(input("Enter the radius"))
    unit = float(input("Enter the unit"))

    # Calculate the area of the base of the cylinder
    base = radius ** 2 * math.pi
    # Calculate the area of the side of the cylinder
    side = radius * 2 * height * math.pi
    # Calculate the total surface area of the cylinder's bases and side
    total_surface_area = base * 2 + side

    # Print out the result
    print("The total surface area of the cylinder is:    ", total_surface_area, unit)


# Calculator for the volume of a cylinder
def cylinder_volume():
    height = float(input("Enter the height"))
    radius = float(input("Enter the height"))
    unit = float(input("Enter the height"))

    # Calculate the area of the base of the cylinder
    base = radius ** 2 * math.pi
    # Calculate the total volume of the cylinder using its base and height
    total_volume = base * height

    # Print out the result
    print("The total volume of the cylinder is:    ", total_volume, unit)


# Calculator for the surface area of a sphere
def sphere_surface_area():
    radius = float(input("Enter the radius"))
    unit = input("Enter the unit")

    # Calculate the surface area of the sphere using the currently known radius
    total_surface_area = 4 * math.pi * radius

    # Print out the result
    print("The total surface area of the sphere is:   ", total_surface_area, unit)


# Calculator for the volume of a sphere
def sphere_volume():
    radius = float(input("Enter the radius"))
    unit = input("Enter the unit")

    # Calculate the surface area of the sphere using the currently known radius
    total_volume = (4 / 3) * math.pi * radius

    # Print out the result
    print("The total volume of the sphere is:   ", total_volume, unit)


# Calculator for the volume of a sphere
def cone_surface_area():
    slant_height = float(input("Enter the slant height"))
    radius = float(input("Enter the radius"))
    unit = input("Enter the unit")

    # Calculate the base of the cone
    base = (radius ** 2) * math.pi
    # Calculate the surface area of the cone using the currently known base and height
    total_surface_area = base + (radius * math.pi * slant_height)

    # Print out the result
    print("The total volume of the cone is:   ", total_surface_area, unit)


# Calculator for the volume of a sphere
def cone_volume():
    height = float(input("Enter the height"))
    radius = float(input("Enter the radius"))
    unit = input("Enter the unit")

    # Calculate the base of the cone
    base = (radius ** 2) * math.pi
    # Calculate the surface area of the cone using the currently known base and height
    total_surface_area = (1/3) * base * height

    # Print out the result
    print("The total volume of the cone is:   ", total_surface_area, unit)
