def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
#add a contact
def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        print("Error input")
#change contact name
def change_contact(args, contacts):
    #check if args not null
    if len(args) < 2 or not args[0] or not args[1]:
        return "Name and phone number must not be empty."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
#show phone byname
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
#show all contacts
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
#show all commands
def print_available_commands():
    print("Available commands:")
    print("  hello                        - Greet the bot")
    print("  add <name> <phone>           - Add a new contact")
    print("  change <name> <new phone>    - Change existing contact's phone")
    print("  phone <name>                 - Show the phone number of a contact")
    print("  all                          - Show all contacts")
    print("  show                         - Show all commands")
    print("  close / exit                 - Exit the bot")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print_available_commands()
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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "show":
           print_available_commands()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
