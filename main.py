#Created by Kuroyukihime000
#--------------------------


import Arcgimed  as arh
import pyramid  as pyr

#Main function
def main():
    user_choise = input("Choose"
                            "the function you want to use: Arcgimed = 1 pyramid = 2 ->")
    if user_choise.lower() == '1':
        ro1= float(input("Введите плотность = "))
        ro2= 1
        m = float(input("Введите массу тела, погруженного в воду = "))
        arh.comparison(ro1)
    elif user_choise.lower() == '2':
        S1 = user_input1 = float(input("Введите площадь верхнего ооснования = "))
        S2 = user_input2 = float(input("Введите площадь нижнего основания = "))
        H = user_input3 = float(input("Введите значение высоты усеченной пирамиды = "))
        print("Обьём вашей усеч пирамиды = ", pyr.V(S1,S2,H))

if __name__ == "__main__":
    main()

