# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# JWray,12.9.2021,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as Emp  # data classes
    import ProcessingClasses as Fp  # processing classes
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp.Person("Bob", "Smith")
objP2 = Emp.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = Fp.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = Emp.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test data module
objP1 = Emp.Employee(1, "Bob", "Smith")
objP2 = Emp.Employee(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()  # Clear list before loading from file
for line in lstFileData: # Convert list of string to Employee objects
    lstTable.append(Emp.Employee(line[0], line[1], line[2].strip()))
for row in lstTable: # show Employee data from refilled list
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())