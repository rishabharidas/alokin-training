from operations import * # iimporting everything from operations
input_number = "\0"
try:
    while input_number != 0:
        """Loop for users choice till exit"""
        print("Choose an Option:\n",  # Choice for the menu in contacts
            "1. Create a Contact\n", 
            "2. List all Contacts\n", 
            "3. Search for a Contact\n", 
            "4. Edit a Contact\n", 
            "5. Delete a Contact\n", 
            "0. Exit")
        input_number = int(input("\nEnter your choice: ")) # recives choice input

        switcher = { # dict to call menu functions
            1: contact_creation,
            2: list_all_contacts,
            3: search_contact,
            4: edit_contact,
            5: delete_contact
        }

        def switch(user_selection): # switch function to switch menus
            """function to switch between different functions"""
            return switcher.get(user_selection)()

        switch(input_number) # calling switch function
except TypeError:
    print("ThankYou for Using - BYE!")
    pass
