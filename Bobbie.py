def bobbie():
    rent = 550
    inc =int(input("Enter monthly income:"))
    exp=int(input("Enter monthly expense:"))

    sav = inc-rent-exp

    if sav >100:
        print("Bobbie can go for a movie and dinner")

        elif sav<=100 and < 50:
            print("Bobbie can go for dinner only")

            elif sav<=50 and sav<0:
                print("Bobbie save the money")
                else:
                    print("Bobbie owens money")

                    return bobbie
