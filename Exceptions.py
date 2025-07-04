def validate_password(password):
    if password == "":
        raise Exception("Password should not be empty.")
    elif len(password) < 8:
        raise Exception("Password length must me be at least 8 characters.")
    elif not any (char.isdigit() for char in password):
        raise Exception("password must contain at least one digit.")
    elif not any (char.isupper() for char in password):
        raise Exception("Password must contain at least on uppercase letter.")
    else:
        print("Password is strong.")

try:
    validate_password("Shashi12")
    validate_password("")
    validate_password("short")
    validate_password("nouppercase1")
except Exception as e:
    print(e)




def book_ride(distance):
    if distance <= 0:
        raise Exception("Distance must be greater than zero.")
    elif distance > 500:
        raise Exception("Distance exceeds our service limit.")
    else:
        print("Ride booked for", distance, "km. Enjoy your journey!")

try:
    book_ride(100)
    book_ride(-5)
    book_ride(600)
except Exception as e:
    print(e)
