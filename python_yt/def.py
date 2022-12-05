# calculations_to_unit = 24
# name_of_unit = "Hours"

# def days_to_units():
#     return f"20 days are: {20 * calculations_to_unit} {name_of_unit}" # si le damos un return tenemso que print la function y con un return dentro del bloque de codigo no me deja meter ningun print
#     # print(f"20 days are: {20 * calculations_to_unit} {name_of_unit}")# como aca ya esta print solo, entonces call the function
#     # print("all good!")
# print(days_to_units())
# print("All good!")




# # quitamos las variables y le pusimos parametros
# def days_to_units2(num_of_days,time,name):
#     return f"{num_of_days} days are: {num_of_days * time} {name}"

# operation = days_to_units2(20,24,"Hours")
# print(operation)


# using an input one way, in follow we have another way
# def days_to_units2(time,name):
#     num_of_days = int(input("give us a number and we will convert it to hours: "))
#     return f"{num_of_days} days are: {num_of_days * time} {name}"


# operation = days_to_units2(24,"Hours")
# print(operation)

# #using try and expect, prefer my way
def days_to_units2(num_of_days,time,name):
    while True:
        try:
            if num_of_days != int:#le podemos quitar != int porque el error me salta igual solo lo puse para que quede mas chido y ser mas especifico
                num_of_days = int(input("give us a number and we will convert it to hours: "))
                return f"{num_of_days} days are: {num_of_days * time} {name}"
        except ValueError:
            print("type a number not other value")

operation = days_to_units2(30,24,"Hours")
print(operation)








def has_lucky_number():
    for num in range(10):
        if num % 7 == 0:
            return True
        else:
            return False

print(has_lucky_number())
