"""_summary_"""

contacts = []

TITLE = "phone book"

contact = {
    'first_name': 'john',
    'last_name': 'doe',
    'mobile': '1234567'
}

contacts.append(contact)

# for key in contact:
#     print(key)
    
for key in contact:
    print(contact[key])
# print(contacts)
# print(dir(contacts))
# print(contact)
# print(type(contact))
# print(id(contact))
# print(dir(contact))
# print(contacts[0])
# print(contacts[len(contacts) - 1])

def contact_list():
    if len(contacts) > 0:
        for item in contacts:
            for k,v in item.items():
                print(k, ' => ', v) 
    else:
        print("Your contact list is empty. Go back to menu and add new contact.")


# contact_list()

def your_choice():
    return input(f"Please make Your choice (l|a|u|d|h|q) >>> ")

def add_contact():
    contact = {}
    first_name = input("Enter firstr name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    mobile = input("Enter phoner phone number: ").strip()
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['mobile'] = mobile
    return contact

def help_me():
    print("""
    All that You can do:
        l: List existing contacts
        a: Add new contact
        u: Edit existing contact
        d: Delete existing contact
        h: Print this help
        q: Exit
    """)

def bye():
    print(f"Thanks for using {TITLE}")
    
def hi():
    print(f"Hi! It's me, {TITLE.upper()}")
    
def remove_contact(contact):
    index = contacts.index(contact)
    confirm = input("Are You sure You want delete this contact? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        return contacts.pop(index)
    return
    
def lookup_contact(name):
    first_name = ''
    last_name = ''
    
    words = name.split()
    
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        
    for d in contacts:
        if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
            return d
        elif d['first_name'] == words[0].lower() or d['last_name'] == words[0].lower():
            return d

def update_contact(contact):
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']
    old_mobile = contact['mobile']
    first_name = input(f"Enter first name: ({old_first_name}) >>> ").strip().lower() or old_first_name
    last_name = input(f"Enter last name: ({old_last_name}) >>> ").strip().lower() or old_last_name
    mobile = input(f"Enter phone number: ({old_mobile}) >>> ").strip() or old_mobile
    
    return {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'mobile': mobile}

def main():
    hi()
    while True:
        match your_choice():
            case 'a':
                contacts.append(add_contact())
            case 'l':
                contact_list()
            case 'u':
                name = input("What You looking for? ")
                contact = lookup_contact(name)
                contact.update(update_contact(contact))
            case 'd':
                name = input("What You looking for? ")
                contact = lookup_contact(name)
                contact = remove_contact(contact)
                if contact:
                    print("Contact removed successfuly.")
            case 'h':
                help_me()
            case 'q':
                bye()
                break
            case _:
                help_me()
                
main()            
            

