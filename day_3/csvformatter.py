"""Program to input a csv file with csv data as first name, lastname, phone1,
phone2, email1, email2
Validatephone number and email and format phonenumber and 
display all the outputs to another CSV file """

import re
from csv import reader,writer
rows_list = []
number_reg_eleven_digits = "^[1](\d{3})(\d{3})(\d{4})$" 
number_reg_twelve_digits = "^[+][1](\d{3})(\d{3})(\d{4})$"
number_reg_ten_digits= "^(\d{3})(\d{3})(\d{4})$"
email_reg = "^[A-za-z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,3}$"

with open("day_3/csvtest.csv","r") as csv_data: # loading file to csv_data
    table_data = reader(csv_data) # reads data from csv
    next(table_data) # skips first row
    for row in table_data: # iteration loop for each row of data
        row_list = []
        """matching regx for phone number1.-------------------------------"""
        match_test_row_number1 = re.match(number_reg_eleven_digits,row[2])
        match_test2_row_number1 = re.match(number_reg_ten_digits,row[2])
        match_test3_row_number1 = re.match(number_reg_twelve_digits,row[2])
        """----------------------------------------------------------------"""
        """matching regx for phone number2.-------------------------------"""
        match_test_row_number2 = re.match(number_reg_eleven_digits,row[3])
        match_test2_row_number2 = re.match(number_reg_ten_digits,row[3])
        match_test3_row_number2 = re.match(number_reg_twelve_digits,row[3])
        """----------------------------------------------------------------"""
        if match_test_row_number1: # condition for if eleven digits
            row_number1 = \
                f"+1({match_test_row_number1[1]})"\
                + f" {match_test_row_number1[2]}-"\
                + f"{match_test_row_number1[3]}" # save number as the US format
        elif match_test2_row_number1: # condition for if 10 digits
            row_number1 = \
                f"+1({match_test2_row_number1[1]})"\
                + f" {match_test2_row_number1[2]}-"\
                + f"{match_test2_row_number1[3]}" # save number as the US format
        elif match_test3_row_number1: # condition for if 12 digits
            row_number1 = \
                f"+1({match_test3_row_number1[1]})"\
                + f" {match_test3_row_number1[2]}-"\
                + f"{match_test3_row_number1[3]}" # save number as the US format
        else:
            row_number1 = "invalid phone number"

        if match_test_row_number2: # condition for if eleven digits
            row_number2 = \
                f"+1({match_test_row_number2[1]})"\
                + f" {match_test_row_number2[2]}-"\
                + f"{match_test_row_number2[3]}" # save number as the US format
        elif match_test2_row_number2: # condition for if 10 digits
            row_number2 = \
                f"+1({match_test2_row_number2[1]})"\
                + f" {match_test2_row_number2[2]}-"\
                + f"{match_test2_row_number2[3]}" # save number as the US format
        elif match_test3_row_number2: # condition for if 12 digits3
            row_number2 = \
                f"+1({match_test3_row_number2[1]})"\
                + f" {match_test3_row_number2[2]}-"\
                + f"{match_test_row_number2[3]}" # save number as the US format
        else:
            row_number2 = "invalid phone number"

        match_test_row_email1 = re.search(email_reg,row[4]) # matching regx for email1
        if match_test_row_email1: 
            row_email1 = row[4] # saved if correctly formatted
        else:
            row_email1 = "invalid email"

        match_test_row_email2 = re.search(email_reg,row[5]) # matching regx for email2
        if match_test_row_email2:
            row_email2 = row[5] # saves if correctily formatted
        else:
            row_email2 = "invalid email"
        
        row_list = [ # List for inserting row values
            row[0], row[1],
            row[2], row_number1,
            row[3], row_number2,
            row[4], row_email1,
            row[5], row_email2
        ]
        rows_list.append(row_list)
    csv_data.close() # closing opened file for reading data
rows_list = sorted(rows_list)
header = [ # row for headers of CSV file
    "first Name", "LastName",
    "Phone1", "validatedPhone1",
    "Phone2", "validdatedPhone2",
    "Email1", "validatedEmail1",
    "Email2", "validatedemail2"
    ]
rows_list.insert(0,header)
with open("day_3/csvvalidated.csv","w") as csv_write_data: # opening csv file to write data
    write = writer(csv_write_data)
    write.writerows(rows_list) # write rows to csv file
    csv_write_data.close() # close opened file for write operation
print(rows_list)