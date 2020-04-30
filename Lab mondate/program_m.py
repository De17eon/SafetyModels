import json


class StateProgram:
    def __init__(self):
        self.active_user = None


def load_json():
    try:
        data = json.load(open('users.json'))
    except:
        data = []
    return data


def write_json(obj):
    data = load_json()
    data.append(obj)
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def p_create_user():
    print('Enter the login of user')
    current_login = input()
    print("Enter the password")
    current_password = input()
    print("Enter Access Level (Mandatnaya model')")
    current_access = input()

    new_user = {
        'login': current_login,
        'password': current_password,
        'access': current_access,
    }

    write_json(new_user)


def login_user(program):
    is_exist = False
    print("Enter Login")
    current_login = input()
    current_user = None

    users = load_json()
    for user in users:
        if user['login'] == current_login:
            is_exist = True
            current_user = user
            break

    if not is_exist:
        print("User isn't exist")
    else:
        print("Enter password")
        current_password = input()

        if current_password != current_user['password']:
            print("Wrong password!")
        else:
            print("You are logged in.")
            program.active_user = current_user


def p_read():
    data = json.load(open('string.json'))
    print(data['string'])


def p_add_to_end():
    data = json.load(open('string.json'))
    string = data['string']
    text = input()
    string += text
    with open('string.json', 'w') as file:
        json.dump({'string': string}, file, indent=2, ensure_ascii=False)


def p_delete():
    with open('string.json', 'w') as file:
        json.dump({'string': ''}, file, indent=2, ensure_ascii=False)


def p_replace():
    text = input()
    with open('string.json', 'w') as file:
        json.dump({'string': text}, file, indent=2, ensure_ascii=False)


def p_change_success_user(program):
    is_exist = False
    print("Enter Login")
    current_login = input()
    current_user = None
    users = load_json()
    for user in users:
        if user['login'] == current_login:
            is_exist = True
            current_user = user
            users.remove(user)
            break

    if not is_exist:
        print("A user with this login does not exist.")
    else:
        print("Enter new access level")
        new_access = input()

        if current_user == program.active_user:
            program.active_user['access'] = new_access
        current_user['access'] = new_access
        users.append(current_user)
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    program = StateProgram()
    login_user(program)

    if program.active_user is not None:
        access = program.active_user['access']
        is_infinity_cycle = True
        while is_infinity_cycle:
            command = input()

            if command == "read":
                if access == 'a' or access == 'b' or access == 'c':
                    p_read()
                else:
                    print("No access!")

            elif command == "add":
                if access == 'a' or access == 'b':
                    p_add_to_end()
                else:
                    print("No access!")

            elif command == "del":
                if access == 'a' or access == 'b':
                    p_delete()
                else:
                    print("No access!")

            elif command == "replace":
                if access == 'a' or access == 'b':
                    p_replace()
                else:
                    print("No access!")

            elif command == "cu":
                if access == 'a':
                    p_create_user()
                else:
                    print("No access!")

            elif command == "csu":
                if access == 'a':
                    p_change_success_user(program)
                    access = program.active_user['access']
                else:
                    print("No access!")

            elif command == "end":
                is_infinity_cycle = False

            else:
                print("Invalid instruction")

