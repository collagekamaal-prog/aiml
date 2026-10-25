def get_sensor_data():
    temp = int(input("Enter temprature : "))
    light = bool(int(input("is there light in the room : (1=yes, 0=no) ")))
    motion = bool(int(input("is there motion : (1=yes, 0=no) ")))
    smoke = bool(int(input("smoke detected : (1=yes, 0=no) ")))
    occup = bool(int(input("is the room occupied : (1=yes, 0=no) ")))

    return temp, motion, smoke, occup, light


def smart_home_agent():

    while True:
        
        temp, motion, smoke, occup, light = get_sensor_data()

        if temp > 30 :
            print("temp over 30 --- *AC TURNED ON*\n")
        else:
            print("temp below 30 --- *AC TURNED OFF*\n")


    
        if motion and not light:
            print("motion and darkness detected --- *light TURNED ON*\n")
        elif motion and light:
            print("no darkness is detected --- *light TURNED OFF*\n")
        elif (not motion) and light:
            print("neither the motion nor the darkness is detected --- *light TURNED OFF*\n")
        else :
            print("darkness is detected --- *light TURNED on*\n")


        if smoke :
            print("smoke detected --- *FIRE ALARM TURNED ON*\n")
        else:
            print("smoke not detected --- *FIRE ALARM TURNED OFF*\n")


        if occup :
            print("room occupied --- *door unlocked*\n")
        else:
            print("room not occupied --- *door locked*\n")



smart_home_agent()
