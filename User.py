
def save_user_profile(name, email, password):
    # Create a dictionary to store user profile
    user_profile = {
        'name': name,
        'email': email,
        'password': password
    }
    return user_profile

# Example usage:
userFirst = input("First Name: ")
userLast = input("Last Name: ")
email = input("E-Mail address: ")
password = input("Password: ")

fullName = userFirst + " " + userLast

profile = save_user_profile(fullName, email, password)
print(profile)


def save_user_information(street,postal,city,state):
    # Create a dictionary for user information
    user_information = {
        'street': street,
        'postal': postal,
        'city': city,
        'state': state,
    }
    return user_information

street = input("Street: ")
postal = input("Postal code: ")
city = input("City: ")
state = input("State: ")

adress = save_user_information(street,postal,city,state)
print(adress)