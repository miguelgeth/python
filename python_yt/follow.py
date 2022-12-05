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

# operation = days_to_units2(30,24,"Hours")
# print(operation)


# using an input another way,  this is from the course, but i prefer mine 
# def days_to_units2(num_of_days,time,name):
#     return f"{num_of_days} days are {num_of_days * time} {name}"


# user_input = int(input("Hey user, neter a number of days and I will covert it to hours\n"))
# calculated_value = days_to_units2(user_input,24,"Hours")
# print(calculated_value)


#while,try

def days_to_units2(num_of_days,time,name):
    try:
        if num_of_days:
            return "un numbero"
    return f"{num_of_days} days are {num_of_days * time} {name}"


user_input = int(input("Hey user, neter a number of days and I will covert it to hours\n"))
calculated_value = days_to_units2(user_input,24,"Hours")
print(calculated_value)


# def days(num):
#     if num > 0:
#         return("hola")
#     else:
#         return("nada")
# operation = days(1)
# print(operation)











#using try and expect
def days_to_units2(num_of_days,time,name):
    try:
        if num_of_days != int:#le podemos quitar != int porque el error me salta igual solo lo puse para que quede mas chido y ser mas especifico
            num_of_days = int(input("give us a number and we will convert it to hours: "))
            return f"{num_of_days} days are: {num_of_days * time} {name}"
    except ValueError:
        print("type a number not other value")

    operation = days_to_units2(30,24,"Hours")
    print(operation)