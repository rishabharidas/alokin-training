from time import process_time # importing time

def main_function(decorator_function): # function to call decorator
    def sub_function():
        print("before the function")
        start_time = process_time() # measure start tme
        deco =  decorator_function()
        end_time = process_time() # measure end time
        print("after running function")
        return deco, start_time, end_time
    return sub_function

def sending_function(): # function calling inside the function
    print("on function ----->")
    return "test_sucess"

send_function = main_function(sending_function)

a,b,c = send_function()

print(a) # calling the assigned main function
print("Time took for decorator: ", c-b)

