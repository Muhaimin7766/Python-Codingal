class Employee:
    def __init__(sel):
        print('Employee created')
    def __del__(self):
        print("Destructor called")
def Create_obj():
    print('Making Object....')
    obj=Employee()
    print('Function end....')
    return obj
print('Calling Create_obj() function....')
obj=Create_obj()
print('Program End....')