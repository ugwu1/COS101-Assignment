def physic_and_maths_operation_option():
    print("a. distance")
    print("b. potential energy")
    print("c. surface tension")
    print("d. finial velocity")
    print("e. area")
    print("f. end")

physic_and_maths_operation_option()
option = input("enter an option a to f  ")
if option == "a":

    speeds = int(input("enter the speed of the distance(M/S) "))
    time = int(input("enter the time taken(S) "))
    distance = speeds * time
    print(f"distance = {distance} M")

elif option == "b":
    mass = int(input("enter the mass of the PE(Kg)"))
    height = int(input("enter the height of the PE(M)"))
    potential_energy = mass * height * 10
    print(f"potential energy = {potential_energy} joule")

elif option == "c":
    force = int(input("enter the force(N)"))
    length = int(input("enter the length(M)"))
    surface_tension = force * length
    print(f"surface tension {surface_tension} N/m")

elif option == "d":
    initial_velocity = int(input("enter the initial velocity(m/s)"))
    acceleration = int(input("enter the acceleration(m/s^2) "))
    time = int(input("enter the time taken(S) "))
    final_velocity = initial_velocity * acceleration * time
    print(f"final velocity {final_velocity} m/s" )

elif option == "e":
    base = int(input("enter the base "))
    height = int(input("enter the height "))
    area = base * height
    print(area)

elif option =="f":
    name = "thank you for using henry's code "
    matric = "matric no bhu|24|04|05|0126"
    end = name + matric
    print(end)

else :
    print("the option type is invalid pls choose an option a to f")