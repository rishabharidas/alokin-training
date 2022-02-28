import json,operator

phone_choice_quotes = """
Phone Details:
1. Insert Personal Number Only 
2. Insert Personal & office Number\n"""
email_choice_quotes = """
Email Details: 
1. Insert Personal email only 
2. Insert Personal & office email\n"""

def write_contacts(passed_contacts):
    """function for writing contacts to file."""
    write_file_data = open("day_2/contacts.json","w")
    write_file_data.write(json.dumps(passed_contacts))
    write_file_data.close()

def read_contacts():
    """function for reading contacts from file."""
    file_data = open("day_2/contacts.json","r")
    loaded_contacts = list(json.loads(file_data.readline()))
    file_data.close()
    return loaded_contacts

def contact_creation():
    """function for contact creation."""
    try:
        contacts = read_contacts()
    except json.JSONDecodeError:
        contacts = []    
    print(contacts)
    numbers = []
    number = {}
    contact = {}
    emails = []
    email = {}
    contact_name = input("Enter Name: ")
    contact["name"] = contact_name
    numbers_choice = int(input(phone_choice_quotes))  #user choice for numbers
    if numbers_choice == 1: # choice for personal number only
        """insert one number to user contact"""
        number["type"] = "personal"
        number["personalNumber"] = input("Enter Personal Number: ")
        numbers.append(number)
    elif numbers_choice == 2: # choice for both home and personal
        """insert two number to user contact"""
        number["type"] = "personal"
        number["personalNumber"] = input("Enter Personal Number: ")
        numbers.append(number)
        number["type"] = "office"
        number["officeNumber"] = input("Enter Office Number: ")
        numbers.append(number)
    contact["phoneNumbers"] = numbers

    email_value = int(input(email_choice_quotes)) #user choice for emails
    if email_value == 1: # choice for personal email only
        email["type"] = "personal"
        email["personalEmailValue"] = input("Enter Personal email: ")
        emails.append(email)
    elif email_value == 2: # choice for office & personal emails
        email["type"] = "personal"
        email["personalEmailValue"] = input("Enter Personal email: ")
        email.append(emails)
        email["type"] = "office"
        email["officeEnailValue"] = input("Enter Office email: ")
        emails.append(email)
    contact["mailIds"] = emails

    contact["notes"] = input("Enter notes: ") #contact notes section

    work_details = {} # Contact Job section
    work_details["companyName"] = input("Enter company name: ")
    work_details["jobTitle"] = input("Enter Job title: ")
    contact["job"] = work_details 

    contacts.append(contact) # insert contact to contacts
    write_contacts(contacts) # write contacts to file

def list_all_contacts():
    """function to list all contacts."""
    try:
        print(sorted(read_contacts(), key=lambda k : k['name'])) # loads contacts
    except json.JSONDecodeError:
        print("Nothing to show")

def search_contact():
    """function to search for a contact."""
    contacts = read_contacts() # loads contacts from json
    print(
        "Search by\n",
        "----------------\n",
        "1. Name\n",
        "2. Number\n") # search choice list
    search_choice = int(input()) # search choice
    if search_choice == 1:
        search_name = input("Enter name to search: ") 
        for contact in contacts: # loop to iterate through contacts
            if contact["name"] == search_name: # check for same name
                print(contact,"\n")
            else:
                print("no contact found\n")
    elif search_choice == 2:
        searching_number = input("Enter number to Serach: ")
        for contact in contacts: # loop to iterate through contacts
            for number in contact["phoneNumbers"]: # loop for itering numbers
                if number["personalNumber"] == searching_number \
                    or number["officeNumber"] == searching_number:
                    print(contact,"\n")

def edit_contact():
    """function for editing a contact."""
    loaded_contacts = read_contacts()
    print(loaded_contacts)
    print(
        "Search by\n",
        "------------------\n",
        "1. Name",
        "2. Number\n" ) # search choice list
    search_choice = int(input()) # search choice
    if search_choice == 1: # Search with Name
        search_name = input("Enter name to search: ") 
        for contact in loaded_contacts: # loop to iterate through contacts
            if contact["name"] == search_name: # check for same name
                print(
                    "Edit on Contact\n",
                    "--------------------\n",
                    "1. Name\n",
                    "2. Number\n",
                    "3. Email\n",
                    "4. Job Details\n") # edit choice list
                edit_choice = int(input()) # search choice
                if edit_choice == 1: # edit choice on name
                    contact["name"] = input("Enter new Name:")
                    write_contacts(loaded_contacts) # calling write function

                elif edit_choice == 2: # edit choice on number
                    print(
                        "Edit On Number section\n",
                        "-------------------------\n",
                        "1. Home\n",
                        "2. Office\n") # edit choice list
                    number_edit_choice = int(input("Enetr choice: "))
                    if number_edit_choice == 1:
                        for home in contact["phoneNumbers"]:
                            home["personalNumber"] = input("Enter New number: ")
                        print(loaded_contacts)
                        write_contacts(loaded_contacts) # calling write function
                    if number_edit_choice == 2:
                        for office in contact["phoneNumbers"]:
                            office["officeNumber"] = input("Enter New number: ")
                        print(loaded_contacts)
                        write_contacts(loaded_contacts) # calling write function
                
                elif edit_choice == 3: # edit on email
                    print(
                        "Edit On\n",
                        "--------------\n",
                        "1. Home\n",
                        "2. Office\n") # edit choice list
                    email_edit_choice = int(input("Enetr choice: "))
                    if email_edit_choice == 1:
                        for home in contact["mailIds"]:
                            home["personalEmailValue"] = input("Enter New email: ")
                        print(loaded_contacts)
                        write_contacts(loaded_contacts)
                    if email_edit_choice == 2:
                        for office in contact["maildIds"]:
                            office["officeEmailValue"] = input("Enter New email: ")
                        print(loaded_contacts)
                        write_contacts(loaded_contacts) # calling write function
                            
                elif number_edit_choice == 4: # edit for job details
                    for job in contact["job"]:
                        """loop for iterating jobs"""
                        job["companyName"] = input("Enter New company name: ")
                        job["jobTitle"] = input("Enter new job title: ")
                        write_contacts(loaded_contacts) # calling write function
                
                else:
                    print("Undefined input")
    elif search_choice == 2: # Search with number
        searching_number = input("Enter number to Serach")
        for contact in loaded_contacts: # loop to iterate through contacts
            for number in contact["phoneNumbers"]: # loop for itering numbers
                if number["personalNumber"] == searching_number \
                    or number["officeNumber"] == searching_number:
                    print(
                        "Edit on Contact\n",
                        "--------------------\n",
                        "1. Name\n",
                        "2. Number\n",
                        "3. Email\n",
                        "4. Job Details\n") # edit choice list
                    edit_choice = int(input()) # search choice
                    if edit_choice == 1: # 3dit on name
                        contact["name"] = input("Enter new Name: ")
                        write_contacts(loaded_contacts) # calling write function

                    elif edit_choice == 2: # edit on number
                        print(
                            "Edit On Number section\n",
                            "-------------------------\n",
                            "1. Home\n",
                            "2. Office\n") # edit choice list
                        number_edit_choice = int(input("Enetr choice: "))
                        if number_edit_choice == 1:
                            for home in contact["phoneNumbers"]:
                                home["personalNumber"] = input("Enter New number: ")
                            print(loaded_contacts)
                            write_contacts(loaded_contacts) # calling write function
                        if number_edit_choice == 2:
                            for home in contact["phoneNumbers"]:
                                home["officeNumber"] = input("Enter New number: ")
                            print(loaded_contacts)
                            write_contacts(loaded_contacts) # calling write function
                    
                    elif edit_choice == 3: # edit on email details
                        print(
                            "Edit On\n",
                            "------------------\n",
                            "1. Home\n",
                            "2. Office\n") # edit choice list
                        email_edit_choice = int(input("Enetr choice: "))
                        if email_edit_choice == 1:
                            for home in contact["mailIds"]:
                                home["personalEmailValue"] = input("Enter New email: ")
                            print(loaded_contacts)
                            write_contacts(loaded_contacts)
                        if email_edit_choice == 2:
                            for office in contact["mailIds"]:
                                office["officeEmailValue"] = input("Enter New email: ")
                            print(loaded_contacts)
                            write_contacts(loaded_contacts) # calling write function
                                
                    elif number_edit_choice == 4: # edit for job details
                        for job in contact["job"]:
                            """loop for iterating jobs"""
                            job["companyName"] = input("Enter New company name: ")
                            job["jobTitle"] = input("Enter new job title: ")
                            write_contacts(loaded_contacts) # calling write function
                    else:
                        print("Undefined input")

def delete_contact():
    """function for deleting a contact."""
    try:
        loaded_contacts = read_contacts()
        print(loaded_contacts)
        print(
            "Delete by\n",
            "-----------------\n",
            "1. Name\n",
            "2. Number\n") # search choice list
        search_choice = int(input()) # search choice
        if search_choice == 1:
            search_name = input("Enter name to search: ") 
            for contact in loaded_contacts: # loop to iterate through contacts
                if contact["name"] == search_name: # check for same name
                    loaded_contacts.remove(contact)
                    write_contacts(loaded_contacts) # calling write function
                else:
                    print("no contact found\n")
        elif search_choice == 2: # Search with number
            searching_number = input("Enter number to Serach")
            for contact in loaded_contacts: # loop to iterate through contacts
                for number in contact["phoneNumbers"]: # loop for itering numbers
                    if number["personalNumber"] == searching_number \
                        or number["officeNumber"] == searching_number:
                        loaded_contacts.remove(contact)
                        write_contacts(loaded_contacts) # calling write function
    except json.JSONDecodeError:
        print(" no Data inside the file")
    