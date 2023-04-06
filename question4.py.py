def main():

    def factorial(a):

        if a == 0: return 0
        elif a == 1: return 1
        else: return a*factorial(a-1) 


    print(factorial(0))
    print(factorial(2))
    print(factorial(4))
    print(factorial(6))
    print(factorial(8))
    print(factorial(10))
    print(factorial(12))
    
 

if __name__ == '__main__':

 

    main()
