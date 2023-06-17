#!/usr/bin/python3

'''solving a real life problem'''

'''create class employee'''
class Employee:

    print('Original Employee Details\n')

    '''initialize the method'''
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):

        '''data members'''
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department 

        '''calculate salary'''
    def calculate_emp_salary(self, emp_salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.emp_salary = self.emp_salary + (overtime * (emp_salary/50))

       
        ''' assign employee a deparment'''
    def emp_assign_department(self, department):

        self.emp_department = department

        '''print employee details'''
    def print_emp_details(self):

        print('Employee Id : ', self.emp_id)
        print('Employee Name : ', self.emp_name)
        print('Employee Salary : ', self.emp_salary)
        print('Employee Department : ', self.emp_department)
        print('-----------------------------------\n')
        
'''create employee data'''
employee1 = Employee('CP084', 'David Ngure', 200000, 'Provider Success')
employee2 = Employee('CP081', 'Hudson Ngure', 200000, 'Data')
employee3 = Employee('MG09', 'Millicent Ngure', 250000, 'Finance')

'''change department'''
employee3.emp_assign_department("Debt Collection")

'''calculate salary'''
employee1.calculate_emp_salary(200000, 80)

'''print employee details'''
employee1.print_emp_details()
employee2.print_emp_details()
employee3.print_emp_details()



