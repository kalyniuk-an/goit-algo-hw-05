def input_error(func):
    def inner(*args, **contacts):
        try:
            return func(*args, **contacts)
        except ValueError:
            return "Error: Give me name and phone please"
        except KeyError:
            return f"Contact '{KeyError.args[0]}' not found"
        except IndexError:
            return f"Contact '{IndexError.args[0]}' not found"
    return inner

def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return (f"{name}'s contact number has been changed to {phone}")
    else:
        return (f"contact {name} dosent exist")

@input_error
def find_phone(args, contacts):
    
    for name, phone in contacts.items():
      if name.lower() == args[0].lower():
        return (f"The phone number for {name}: {phone}")
    
    # return (f"Contact {args[0]} not found.")
    raise KeyError(args[0])

def show_all(contacts):
    if not contacts:
        return "Your contact list is empty."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()