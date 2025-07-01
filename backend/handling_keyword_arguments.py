def create_user(**kwargs):
    print("Creating user with data:", kwargs)

create_user(name="Gokul", email="gokul@example.com")

# ** kwargs allows passing a variable n of keyword arguments(data) to the function.
# This is useful when the number of arguments is not known beforehand or when you want to pass