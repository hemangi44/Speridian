from datetime import datetime

from settings import db


# Employee model
class EmployeeModel(db.Document):
    emp_id = db.IntField()
    first_name = db.StringField()
    last_name = db.StringField()
    gender = db.StringField()
    date_of_birth = db.DateTimeField()
    salutation = db.StringField()
    designation = db.StringField()
    email = db.StringField()
    mobile = db.IntField()
    address_line_1 = db.StringField()
    address_line_2 = db.StringField()
    city = db.StringField()
    state = db.StringField()
    pin = db.IntField()
    country = db.StringField()

    def __str__(self):
        return self.emp_id


class EmployeeModelSerializer:
    def __init__(self, employee_model: EmployeeModel = None):
        self.employee_model = employee_model

    def from_request_to_model(self, request_data):
        employee_model = EmployeeModel(
            emp_id=request_data['emp_id'],
            first_name=request_data['first_name'],
            last_name=request_data['last_name'],
            gender=request_data['gender'],
            date_of_birth=datetime.strptime(request_data['date_of_birth'], '%d-%m-%Y'),
            salutation=request_data['salutation'],
            designation=request_data['designation'],
            email=request_data['email'],
            mobile=request_data['mobile'],
            address_line_1=request_data['address_line_1'],
            address_line_2=request_data['address_line_2'],
            city=request_data['city'],
            state=request_data['state'],
            pin=request_data['pin'],
            country=request_data['country']
        )
        self.employee_model = employee_model
        return employee_model

    def from_model_to_dict(self):
        return {'emp_id': self.employee_model.emp_id,
                'first_name': self.employee_model.first_name,
                'last_name': self.employee_model.last_name,
                'gender': self.employee_model.gender,
                'date_of_birth': self.employee_model.date_of_birth.strftime('%d-%m-%Y'),
                'salutation': self.employee_model.salutation,
                'designation': self.employee_model.designation,
                'email': self.employee_model.email,
                'mobile': self.employee_model.mobile,
                'address_line_1': self.employee_model.address_line_1,
                'address_line_2': self.employee_model.address_line_2,
                'city': self.employee_model.city,
                'state': self.employee_model.state,
                'pin': self.employee_model.pin,
                'country': self.employee_model.country
                }
