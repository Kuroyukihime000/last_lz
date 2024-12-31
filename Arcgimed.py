# Created by Kuroyukihime000
#------------------------

#Functions 
def comparison(ro1):
    if ro1>1:
        print("неплавучий")
    elif ro1 == 1:
        print("неплавучий")
    else:
        print("Плавучий") 

#Funtcion main
def main ():
    ro1= float(input("Введите плотность = "))
    m = float(input("Введите массу тела, погруженного в воду = "))
    comparison(ro1)

if __name__ == '__main__':
    main()