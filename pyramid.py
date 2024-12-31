#Created by Kuroyukihime000


from math import sqrt #Импортим из мат библиотеки коорень


# function 
V =  lambda S1,S2,H : 1/3*H*(S1 + sqrt(S1*S2)+ S2)

# function main 
def main():
    S1 = user_input1 = float(input("Введите площадь верхнего ооснования = "))
    S2 = user_input2 = float(input("Введите площадь нижнего основания = "))
    H = user_input3 = float(input("Введите значение высоты усеченной пирамиды = "))
    res = (print( "Полученый обьём = " ,V (S1,S2,H)))

if __name__ == "__main__":
    main()
