Assignment for Speridian.
How to run the project?
1. Clone the url into local folder.
2. Create virtual environment for python using-
	virtualenv venv
3. Activate the 'venv' environment using-
	venv\Scripts\activate
4. Install the python dependencies using-
	pip install -r requirements.txt
5. Download mongo db zip from https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.6-signed.msi
6. Go to bin folder of mongo db and type mongod to activate the mongo db
7. Run the flask server using-	
	python app.py
	
8. You can hit below apis

1. http://127.0.0.1:5000/employees
	-- It will list all the employees from mongodb document Employee
2. http://127.0.0.1:5000/employee/<emp_id>
	-- It will fetch one employee from mongodb document Employee for emp_id = <emp_id>
3. http://127.0.0.1:5000/employee/<emp_id>
	-- Method DELETE
	-- It will delete one employee from mongodb document Employee for emp_id = <emp_id>
4. http://127.0.0.1:5000/employee/
	-- Method POST
	-- It will add one employee into mongodb document Employee using below body
	-- Please note date format used is - 'DD-MM-YYYY'
		{
			"emp_id" : 101,
			"first_name" : "Suresh",
			"last_name" : "Rathi",
			"gender" : "Male",
			"date_of_birth" : "02-06-1980",
			"salutation" : "Mr.",
			"designation" : "Manager",
			"email" : "suresh_rathi@abc.com",
			"mobile" : 9029090290,
			"address_line_1" : "Sheetal apartments",
			"address_line_2" : "Sion",
			"city" : "Mumbai",
			"state" : "Maharashtra",
			"pin" : 400022,
			"country" : "India"
		}
5. http://127.0.0.1:5000/employee/
	-- Method PUT
	-- It will update one employee into mongodb document Employee using below body for emp_id mentioned in body
	-- Please note date format used is - 'DD-MM-YYYY'
		{
			"emp_id" : 101,
			"first_name" : "Suresh",
			"last_name" : "Rathi",
			"gender" : "Male",
			"date_of_birth" : "02-06-1980",
			"salutation" : "Mr.",
			"designation" : "Manager",
			"email" : "suresh_rathi@abc.com",
			"mobile" : 9029090290,
			"address_line_1" : "Sheetal apartments",
			"address_line_2" : "Sion",
			"city" : "Mumbai",
			"state" : "Maharashtra",
			"pin" : 400022,
			"country" : "India"
		}