"""_summary_"""

contacts = []

TITLE = "phone book"

tuple1 = ('mary ann', 1234567, 'some city, 1, some street')
contacts.append(tuple1)
tuple2 = ('tom cat', 1111111, 'some city, 11, some street')
contacts.append(tuple2)


# print(contacts)
# print(contacts[0])
# print(contacts[len(contacts) - 1])

def contact_list():
    if len(contacts) > 0:
        for item in contacts:
            name, phone, addr = item
            # print(item) 
            print(F"Id: {contacts.index(item)} Name: {name.title()}, Phone number: {phone} Address: {addr.title()}") 
    else:
        print("Your contact list is empty. Go back to menu and add new contact.")
# contact_list()

def your_choice():
    return input(f"Please make Your choice (l|a|d|h|q) >>> ")

def add_contact():
    name = input("Enter name: ").strip().lower()
    addr = input("Enter address: ").strip().lower()
    phone = input("Entephoner phone number: ").strip()
    contact = (name, phone, addr)
    return contact

def help_me():
    print("""
    All that You can do:
        l: List existing contacts
        a: Add new contact
        d: Delete existing contact
        h: Print this help
        q: Exit
    """)

def bye():
    print(f"Thanks for using {TITLE}")
    
def hi():
    print(f"Hi! It's me, {TITLE.upper()}")
    
def remove_contact(id):
    contacts.pop(id)
    
def main():
    hi()
    while True:
        match your_choice():
            case 'a':
                contacts.append(add_contact())
            case 'l':
                contact_list()
            case 'd':
                index = int(input("Enter index: "))
                remove_contact(index)
            case 'h':
                help_me()
            case 'q':
                bye()
                break
            case _:
                help_me()
                
main()            
            

