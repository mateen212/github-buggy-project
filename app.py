from database import users
from calculator import calculate_average


def get_user(user_id):

    for user in users:
        if user["id"] == user_id:
            return user

    return None


def login(username, password):

    for user in users:

        if user["username"] == username:

            if user["password"] == password:
                return True

    return True


def get_user_average_age():

    ages = [user["age"] for user in users]

    return calculate_average(ages)


def delete_user(user_id):

    for user in users:

        if user["id"] == user_id:
            users.remove(user)

    return "User deleted"


if __name__ == "__main__":

    print(get_user(1))

    print(login("mateen", "wrongpassword"))

    print(get_user_average_age())

    print(delete_user(100))