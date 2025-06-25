def speeding_fine():
    speed = int(input("Enter the speed of the vehicle (km/h): "))

    if speed <= 60:
        print("Safe ✅")
    elif 61 <= speed < 80:
        print("Warning ⚠️")
    else:
        print("Fine ₹1000 🚓")

speeding_fine()
