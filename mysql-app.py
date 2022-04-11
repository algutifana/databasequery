#query ClassicModels database - November 9, 2021
import mysql.connector

def menu():
    print("Choose an option from the menu:")
    print("1. Show number of employees from the Americas")
    print("2. Show all managers")
    print("3. Show the department with the largest number of dependents")
    print("4. Show number of hires in 1997")
    print("5. Show total salary for the Finance department")
    print("6. Show job title and salary for the job with the highest salary")
    print("7. Show employees with no children")
    print("8. Show countries with no locations")
    print("9. Exit")

def get_input():
    menu()
    inp = int(input("Enter option: "))
    return inp 


def get_american_employees(mycursor):
    query = "SELECT * FROM EmployeesPerRegion WHERE region_name = \"Americas\";"

    mycursor.execute(query)

    result = mycursor.fetchall()


    for record in result:
        print(f"\nRegion Name: {record[0]} - Number of Employees: {record[1]}\n")


def get_managers(mycursor):
    query = "SELECT department_name, COUNT(department_name) FROM managers GROUP BY department_name;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nDepartment Name: {record[0]} - Number of Managers: {record[1]}\n")

def get_department_dependents(mycursor):
    query = "SELECT * FROM DependentsByDepartment ORDER BY dependents DESC LIMIT 1;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nDepartment Name: {record[0]} - Number of Dependents: {record[1]}\n")

def get_1997_hires(mycursor):
    query = "SELECT * FROM HiresByYear WHERE yearhired = 1997;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nYear hired: {record[0]} - Number of Employees: {record[1]}\n")

def get_finance_salary(mycursor):
    query = "SELECT * FROM SalaryByDepartment WHERE department_name = \"Finance\";"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nDepartment Name: {record[0]} - Total Salary: {record[1]}\n")

def get_highest_salary(mycursor):
    query = "SELECT * FROM SalaryByJobTitle ORDER BY totalsalary DESC LIMIT 1;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nJob Title: {record[0]} - Total Salary: {record[1]}\n")

def get_childless_employees(mycursor):
    query = "SELECT * FROM EmployeeDependents WHERE dependents = 0;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nEmployee name: {record[0]} {record[1]} - Phone Number: {record[2]} - Number of Dependents: {record[3]}\n") 

def get_locationless_countries(mycursor):
    query = "SELECT * FROM CountryLocation WHERE locations = 0;"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for record in result:
        print(f"\nCountry Name: {record[0]} - Number of Locations: {record[1]}\n")

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="finalproject"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):

        option = get_input()

        if option == 1: 
            get_american_employees(mycursor)

        if option == 2:
            get_managers(mycursor)

        if option == 3:
            get_department_dependents(mycursor)

        if option == 4:
            get_1997_hires(mycursor)

        if option == 5:
            get_finance_salary(mycursor)

        if option == 6:
            get_highest_salary(mycursor) 

        if option == 7:
            get_childless_employees(mycursor)

        if option == 8:
            get_locationless_countries(mycursor)

        if option == 9:
            print("Goodbye!")
            break
main()
    

