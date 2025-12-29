try :
    f = open("data.txt","r")
    print(f.read())
except filenotfoundError:
    print("File not found")
finally:
    print("file operation completed")
    try:
        x = int(input())
        print(10/x)
    except(ValueError,ZeroDivisionError):
        print("Invalid input or division error ")
        try:
            a =10
            b=2
            print(a/b)
        except ZeroDivisionError:
            print("Error")
        else:
            print ("Execution successful")
            try:
                a=int(input())
                b=int(input())
                print(a/b)
            except ZeroDivisionError:
                print("Division by zero error")
            except ValueError:
                print ("Invalid input")