def greet(who_to_greet):
    greeting = "Hello, " + who_to_greet
    return greeting

if __name__ == "__main__":
    nameToGreet = input("Enter the name to be greeted: ")
    print (greet(nameToGreet))