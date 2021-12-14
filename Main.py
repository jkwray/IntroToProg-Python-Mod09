# ------------------------------------------------------------------------
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# JWray,12.13.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------

if __name__ == "__main__":
    import DataClasses as Emp
    import ProcessingClasses as Fp  # processing classes
    from IOClasses import EmployeeIO as Eio  # input/Output classes
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ----------------------------------------------------
strFileName = 'EmployeeData.txt'
lstOfEmployees = []

try:
    # Load data from file into a list of employee objects when script starts
    lstData = Fp.FileProcessor.read_data_from_file(strFileName)

    # convert list of strings to list of objects
    for line in lstData:
        lstOfEmployees.append(Emp.Employee(line[0], line[1], line[2].strip()))

    while True:
        # Show user a menu of options
        Eio.print_menu_items()

        # Get user's menu option choice
        choice_str = Eio.input_menu_options()

        if choice_str.strip() == '1':
            # Show user current data in the list of employee objects
            Eio.print_current_list_items(lstOfEmployees)
            continue

        elif choice_str == '2':
            # Let user add data to the list of employee objects
            new_employee = Eio.input_employee_data()
            lstOfEmployees.append(new_employee)
            print('New employee successfully added!')

            # print current product list to show new one added
            Eio.print_current_list_items(lstOfEmployees)
            continue

        elif choice_str == '3':  # Save data
            Fp.FileProcessor.save_data_to_file(strFileName, lstOfEmployees)
            print('Employee list saved!')
            continue

        elif choice_str == '4':  # Save data and exit
            Fp.FileProcessor.save_data_to_file(strFileName, lstOfEmployees)
            print('Good-bye!')
            break

        else:
            print('"', choice_str, '"', 'is not a valid menu choice.')
            print()
            continue

except Exception as e:
    print(e)
    print()

# Main Body of Script  ---------------------------------------------------- #
