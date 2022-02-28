from module import join_list  # importing from module.py module

input_list = []
odd_list = []
even_list = []
TEST_CONSTANT="defined as a constant value"
limit = int(input("Enter limit for list: "))  # receving limit for list
print("Enter Values one by one: ")
for i in range(limit):   # loop for inserting values to list on range basis
    input_list.append(int(input()))
print("\n-------------------------\n")

class SumAndLength:
    """Class for Sum and Length of List"""
    def __init__(self,passing_list):
        """Constructor."""
        self.passing_list = passing_list
        self.even_list = even_list
        self.odd_list = odd_list
    
    def sum_of_list(self):
        """ function to find sum of all list elemets."""
        print("Sum of list: ", sum(self.passing_list))

    def list_length(self):
        """ function for finding length of list."""
        print("List length: ", len(self.passing_list))


class ChildWithSort(SumAndLength):
    """ SortAndJoin inheriting SumAndLength class."""
    def list_sort(self):
        """Function for sorting a List."""
        sorted_list = sorted(self.passing_list)
        return sorted_list  # returns the sorted list on function call

    def seperate_even_and_odd(self):
        """
        function for sorting even and odd numbers
        to seperate lists."""
        for element in self.passing_list:  #  loop to iterate through list
            if element % 2 == 0:  # checks number is even or not
                self.even_list.append(element)
            else:
                self.odd_list.append(element)
        print("Even number in the List: ", self.even_list)
        print("Odd numbers in the List: ", self.odd_list)

class_obj = ChildWithSort(input_list)  # object for calling the inherited class
assert class_obj.sum_of_list() == 5  # calling functions with the objects
class_obj.list_length()
print("Sorted List: ", class_obj.list_sort())
joined_list = join_list(input_list)  # calling an imported function
print("Joined Value: ", joined_list)
print(u'\1F609', TEST_CONSTANT)
class_obj.seperate_even_and_odd()  # calls even odd checking function