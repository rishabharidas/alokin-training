import json,operator

from sqlalchemy import delete
from databasedata import connected_engine
from sqlalchemy.sql import insert, update, delete

from tables import contactstable

phone_choice_quotes = """
Phone Details:
1. Insert Personal Number Only 
2. Insert Personal & office Number\n"""
email_choice_quotes = """
Email Details: 
1. Insert Personal email only 
2. Insert Personal & office email\n"""


def write_contacts():
    """function for writing contacts to file."""
    contacts_from_db = []
    write_file_data = open("day_5/contacts/contacts.json","w")
    query = f"""
        select json_object("name", name, "phones", phones,
        "emails", emails, "notes", notes,
        "jobDetails", jobDetails) as contact from contactstable"""
    data = connected_engine.execute(query)
    for i in data:
        contacts_from_db.append(json.loads(i.contact))
        if contacts_from_db:
            write_file_data.write(json.dumps(contacts_from_db))
        else:
            write_file_data.writr("<------- No Data here -------->")
        write_file_data.close()


def read_contacts():
    """function for reading contacts from file."""
    write_contacts()
    file_data = open("day_5/contacts/contacts.json","r")
    loaded_contacts = list(json.loads(file_data.readline()))
    file_data.close()
    return loaded_contacts

def contact_creation():
    """function for contact creation."""
    try:
        contacts = read_contacts()
    except json.JSONDecodeError:
        contacts = []    
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
    contact["phones"] = str(numbers)

    email_value = int(input(email_choice_quotes)) #user choice for emails
    if email_value == 1: # choice for personal email only
        email["type"] = "personal"
        email["personalEmailValue"] = input("Enter Personal email: ")
        emails.append(email)
    elif email_value == 2: # choice for office & personal emails
        email["type"] = "personal"
        email["personalEmailValue"] = input("Enter Personal email: ")
        emails.append(email)
        email["type"] = "office"
        email["officeEnailValue"] = input("Enter Office email: ")
        emails.append(email)
    contact["emails"] = str(emails)

    contact["notes"] = input("Enter notes: ") #contact notes section

    work_details = {} # Contact Job section
    work_details["companyName"] = input("Enter company name: ")
    work_details["jobTitle"] = input("Enter Job title: ")
    contact["jobDetails"] = str(work_details)

    query = insert(contactstable).values(**contact)
    connected_engine.execute(query)

    contacts.append(contact) # insert contact to contacts
    write_contacts() # write contacts to file
    return contact

def list_all_contacts():
    """function to list all contacts."""
    
    try:
        # query = f"""
        # select json_object("name", name, "phones", phones,
        # "emails", emails, "notes", notes,
        # "jobDetails", jobDetails) as contact from contactstable"""
        # data = connected_engine.execute(query)
        # for i in data:
        #     contacts_from_db.append(json.loads(i.contact))

        print(sorted(read_contacts(), key=lambda k : k['name'])) # loads contacts
    except json.JSONDecodeError:
        print("Nothing to show")

def search_contact():
    """function to search for a contact."""
    loaded_contacts = read_contacts() # loads contacts from json
    print(
        "Search by\n",
        "----------------\n",
        "1. Name\n",
        "2. Number\n") # search choice list
    search_choice = int(input()) # search choice
    if search_choice == 1:
        search_name = input("Enter name to search: ") 
        for contact in loaded_contacts: # loop to iterate through contacts
            if contact["name"] == search_name: # check for same name
                print(contact,"\n")
            else:
                print("no contact found\n")
    elif search_choice == 2:
        searching_number = input("Enter number to Serach: ")
        for contact in loaded_contacts: # loop to iterate through contacts
            for number in eval(contact["phones"]): # loop for itering numbers
                if number["personalNumber"] == searching_number \
                    or number["officeNumber"] == searching_number:
                    print(contact,"\n")
                else:
                    print("No Data Found ")

def edit_contact():
    """function for editing a contact."""
    loaded_contacts = read_contacts()
    print(loaded_contacts)
    print(
        "Search by\n",
        "------------------\n",
        "1. Name\n",
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
                    updatequery = update(contactstable)\
                    .where(contactstable.name == search_name)\
                    .values(name= input("Enter new Name:"))
                    connected_engine.execute(updatequery)
                    write_contacts() # calling write function
                    print("\n ---- Edit Done sucessfully \n")

                elif edit_choice == 2: # edit choice on number
                    print(
                        "Edit On Number section\n",
                        "-------------------------\n",
                        "1. Home\n",
                        "2. Office\n") # edit choice list
                    number_edit_choice = int(input("Enter choice: "))
                    if number_edit_choice == 1:
                        updated_phone_data = eval(contact["phones"])
                        for home in updated_phone_data:
                            home["personalNumber"] = input("Enter New number: ")
                        # phone number update query
                        updatequery = update(contactstable)\
                        .where(contactstable.name == search_name)\
                        .values(phones = str(updated_phone_data)) 
                        connected_engine.execute(updatequery) #query execution
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")
                    elif number_edit_choice == 2:
                        updated_phone_data = eval(contact["phones"])
                        for home in updated_phone_data:
                            home["officeNumber"] = input("Enter New number: ")
                        # phone number update query
                        updatequery = update(contactstable)\
                        .where(contactstable.name == search_name)\
                        .values(phones = str(updated_phone_data))
                        connected_engine.execute(updatequery) #query execution
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")
                
                elif edit_choice == 3: # edit on email
                    print(
                        "Edit On\n",
                        "--------------\n",
                        "1. Home\n",
                        "2. Office\n") # edit choice list
                    email_edit_choice = int(input("Enetr choice: "))
                    if email_edit_choice == 1:
                        updated_email_data = eval(contact["emails"])
                        for home in updated_email_data:
                            home["personalEmailValue"] = input("Enter New email: ")
                        # email update query
                        updatequery = update(contactstable)\
                        .where(contactstable.name == search_name)\
                        .values(emails = str(updated_email_data))
                        connected_engine.execute(updatequery) #query execution
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")
                    if email_edit_choice == 2:
                        updated_email_data = eval(contact["emails"])
                        for home in updated_email_data:
                            home["officeEmailValue"] = input("Enter New email: ")
                        # phone number update query
                        updatequery = update(contactstable)\
                        .where(contactstable.name == search_name)\
                        .values(emails = str(updated_email_data))
                        connected_engine.execute(updatequery) #query execution
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")
                            
                elif edit_choice == 4: # edit for job details
                    updated_job_data = eval(contact["jobDetails"])
                    updated_job_data["companyName"] = input("Enter New company name: ")
                    updated_job_data["jobTitle"] = input("Enter new job title: ")
                    # phone number update query
                    updatequery = update(contactstable)\
                    .where(contactstable.name == search_name)\
                    .values(jobDetails = str(updated_job_data))
                    connected_engine.execute(updatequery) #query execution
                    write_contacts() # calling write function
                    print("\n ---- Edit Done sucessfully \n")
                
                else:
                    print("Undefined input")
            else:
                print("no contact found to edit")

    elif search_choice == 2: # Search with number
        searching_number = input("Enter number to Serach")
        for contact in loaded_contacts: # loop to iterate through contacts
            for number in eval(contact["phones"]): # loop for itering numbers
                if number["personalNumber"] == searching_number \
                    or number["officeNumber"] == searching_number:
                    print(
                    "Edit on Contact\n",
                    "--------------------\n",
                    "1. Name\n",
                    "2. Number\n",
                    "3. Email\n",
                    "4. Job Details\n") # edit choice 
                    edit_choice = int(input()) # search choice
                    if edit_choice == 1: # edit choice on name
                        updatequery = update(contactstable)\
                        .where(contactstable.phones == (contact["phones"]))\
                        .values(name= input("Enter new Name:"))
                        connected_engine.execute(updatequery)
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")

                    elif edit_choice == 2: # edit choice on number
                        print(
                            "Edit On Number section\n",
                            "-------------------------\n",
                            "1. Home\n",
                            "2. Office\n") # edit choice list
                        number_edit_choice = int(input("Enetr choice: "))
                        if number_edit_choice == 1:
                            updated_phone_data = eval(contact["phones"])
                            for home in updated_phone_data:
                                home["personalNumber"] = input("Enter New number: ")
                            # phone number update query
                            updatequery = update(contactstable)\
                            .where(contactstable.phones == (contact["phones"]))\
                            .values(phones = str(updated_phone_data)) 
                            connected_engine.execute(updatequery) #query execution
                            write_contacts() # calling write function
                            print("\n ---- Edit Done sucessfully \n")
                        elif number_edit_choice == 2:
                            updated_phone_data = eval(contact["phones"])
                            for home in updated_phone_data:
                                home["officeNumber"] = input("Enter New number: ")
                            # phone number update query
                            updatequery = update(contactstable)\
                            .where(contactstable.phones == (contact["phones"]))\
                            .values(phones = str(updated_phone_data))
                            connected_engine.execute(updatequery) #query execution
                            write_contacts() # calling write function
                            print("\n ---- Edit Done sucessfully \n")
                    
                    elif edit_choice == 3: # edit on email
                        print(
                            "Edit On\n",
                            "--------------\n",
                            "1. Home\n",
                            "2. Office\n") # edit choice list
                        email_edit_choice = int(input("Enetr choice: "))
                        if email_edit_choice == 1:
                            updated_email_data = eval(contact["emails"])
                            for home in updated_email_data:
                                home["personalEmailValue"] = input("Enter New email: ")
                            # email update query
                            update_query = update(contactstable)\
                            .where(contactstable.phones == (contact["phones"]))\
                            .values(emails = str(updated_email_data))
                            connected_engine.execute(update_query) #query execution
                            write_contacts() # calling write function
                            print("\n ---- Edit Done sucessfully \n")
                        if email_edit_choice == 2:
                            updated_email_data = eval(contact["emails"])
                            for home in updated_email_data:
                                home["officeEmailValue"] = input("Enter New email: ")
                            # phone number update query
                            updatequery = update(contactstable)\
                            .where(contactstable.phones == (contact["phones"]))\
                            .values(emails = str(updated_email_data))
                            connected_engine.execute(updatequery) #query execution
                            write_contacts() # calling write function
                            print("\n ---- Edit Done sucessfully \n")
                                
                    elif edit_choice == 4: # edit for job details
                        updated_job_data = eval(contact["jobDetails"])
                        updated_job_data["companyName"] = input("Enter New company name: ")
                        updated_job_data["jobTitle"] = input("Enter new job title: ")
                        # phone number update query
                        updatequery = update(contactstable)\
                        .where(contactstable.phones == (contact["phones"]))\
                        .values(jobDetails = str(updated_job_data))
                        connected_engine.execute(updatequery) #query execution
                        write_contacts() # calling write function
                        print("\n ---- Edit Done sucessfully \n")
                    
                    else:
                        print("Undefined input")
                else:
                    print(" --- No Data found")

def delete_contact():
    """function for deleting a contact."""
    try:
        loaded_contacts = read_contacts()
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
                    delete_query = delete(contactstable).where(contactstable.name == search_name)
                    connected_engine.execute(delete_query)
                    write_contacts() # calling write function
                    print("\n ---- Deleted sucessfully \n")
                else:
                    print("no contact found\n")
        elif search_choice == 2: # Search with number
            searching_number = input("Enter number to Serach")
            for contact in loaded_contacts: # loop to iterate through contacts
                for number in eval(contact["phones"]): # loop for itering numbers
                    if number["personalNumber"] == searching_number \
                        or number["officeNumber"] == searching_number:
                        loaded_contacts.remove(contact)
                        delete_query = delete(contactstable).where(contactstable.phones == (contact["phones"]))
                        connected_engine.execute(delete_query)
                        write_contacts() # calling write function
                        print("\n ---- Deleted sucessfully \n")
                    else:
                        print("no data found")
    except json.JSONDecodeError:
        print(" no Data inside the file")
    