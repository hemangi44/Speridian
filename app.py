from flask import request

from models import EmployeeModel, EmployeeModelSerializer
from settings import app
from util import create_response


@app.route('/home')
def index():
    return 'Hello World'

# Fetch all employee details
@app.route('/employees', methods=['GET'])
def get_all_employees_details():
    employees = EmployeeModel.query.all()
    final_response = []
    for i in range(len(employees)):
        employeeModelSerialier = EmployeeModelSerializer(employees[i])
        final_response.append(employeeModelSerialier.from_model_to_dict())
    return create_response(final_response, 200)

# Fetch employee data for an employee id
@app.route('/employee/<employee_id>', methods=['GET'])
def get_employee_details_from(employee_id):
    existing_employee = EmployeeModel.query.filter(EmployeeModel.emp_id == int(employee_id)).first()
    if existing_employee:
        employeeModelSerialier = EmployeeModelSerializer(existing_employee)
        return create_response(employeeModelSerialier.from_model_to_dict(), 200)
    return create_response({'message': 'Could not find employee details using below emp id',
                                    'emp_id': employee_id}, 404) 


# Delete employee data for an employee id
@app.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee_details_by(employee_id):
    existing_employee = EmployeeModel.query.filter(EmployeeModel.emp_id == int(employee_id)).first()
    if existing_employee:
        existing_employee.remove()
        return create_response({'message': 'Employee details deleted',
                                'emp_id': employee_id}, 200)
    return create_response({'message': 'Could not delete employee details as below emp id does not exists',
                            'emp_id': employee_id}, 404)

# Add employee data
@app.route('/employee', methods=['POST'])
def add_employee_details():
    try:
        request_data = request.get_json()
        existing_employee = EmployeeModel.query.filter(EmployeeModel.emp_id == int(request_data['emp_id'])).first()
        if existing_employee:
            return create_response({'message': 'Could not add employee details as below emp id already exists',
                                    'emp_id': request_data['emp_id']}, 409)
        employeeModelSerialier = EmployeeModelSerializer()
        new_employee = employeeModelSerialier.from_request_to_model(request_data)
        new_employee.save()
        return create_response(employeeModelSerialier.from_model_to_dict(), 200)
    except Exception as e:
        print(e)
        return create_response({'error_message': 'Technical error at server side ',
                                'error_code': 503}, 503)

# Update employee data for an employee id
@app.route('/employee', methods=['PUT'])
def update_employee_details():
    try:
        request_data = request.get_json()
        existing_employee = EmployeeModel.query.filter(EmployeeModel.emp_id == int(request_data['emp_id'])).first()
        if existing_employee:
            existing_employee.remove()

            employeeModelSerialier = EmployeeModelSerializer()
            new_employee = employeeModelSerialier.from_request_to_model(request_data)
            new_employee.save()
            return create_response(employeeModelSerialier.from_model_to_dict(), 200)
        return create_response({'message': 'Could not update employee details as below emp id does not exists',
                                'emp_id': request_data['emp_id']}, 404)

    except Exception as e:
        print(e)
        return create_response({'error_message': 'Technical error at server side ',
                                'error_code': 503}, 503)


if __name__ == '__main__':
    app.run(debug=True)
