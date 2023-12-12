## v0.1.0 (2022-06-08)

### Refactor

- **v1/employee.py,config.py,player_schema.py,customer_schema.py,common_schema.py,employee_schema.py**: SX-220/add prefix in config file,change url path for list employee,remove logger from health check
- **test_healthcheck.py**: SX-220/add prefix to api url
- **employee.py,customer.py.player.py.healthcheck.py**: SX-220/made changes in api service added prefix accountsh
- **employee_Crud.py,player_crud.py,employee_schema.py,player_schema.py,customer_schema.py,customer_crud.py**: SX-220/remove password field from customer,remove validation for password in constants file,remove id from player table,update schema create for player table
- **customer.py,employee.py**: SX-220/update query parameter field
- **player_crud.py,customer_crud.py,player_schema.py,customer_schema.py**: SX-220/made changes in all files based on changes in specs
- **customer.py,employee.py**: SX-220/added limit and offset for list api
- **employee.py**: SX-230/made changes in query parameter description
- **main.py,customer_crud.py,player_crud.py,customer_crud.py,employee_crud.py,player.py,employee.py,customer.py**: SX-220/create query parameter for list api of employee and customer and return header from crud to router file
- **main.py,customer_crud.py,employee_crud.py,player_crud.py,constants.py,customer_schema.py,employee_schema.py,common_schema.py,employee_exception.py**: SX-220/create coomon_schema file for common schema,modified exception,query parameter with string validation,
- **player_crud.py,employee_crud.py,customer_crud.py,player_exception.py,customer_exception.py,employee_exception.py,constants.py,main.py**: SX-220/create EmployeeDoesNotExist,CustomerDoesNotExist,PlayerDoesNotExist,exception update this in all CRUD files
- **customer_crud.py,customer_schema.py,customer_exception.py,v1/customer.py**: SX-220/rename exception file for customer,change name of exception also
- **employee_crud.py,player_crud.py,customer_crud.py,customer.py,list_of_all_customers.py,player_schema.py,customer_schema.py,list_of_player.json**: SX-220/change schem for player and customer ,rename all files which start with parent to customer,create list api for player and customer ,change url path etc
- **CHANGELOG.md**: update changelog file
- **test_config.py**: sx-220/make changes in test case, check config variable exist or not
- **employee_crud.py,parent_crud.py,player_crud.py,employee.py,player.py,parent.py**: SX-220/return Response object from create,update api of all tables
- **employee_crud.py,player_crud.py,parent_crud.py,constants.py,employee_schema.py,player_schema.py,parent_schema.py,list_of_parent.json,list_employee.json,get_employee.json,list_of_player.json,main.py**: SX-220/make the all changes based on the changes in API specs like remove type from address,added first_name and last_name in player and parent table schema,make constant all regex,for all json files add the updated response body
- **emplyee_crud,parent_crud.py,employee_schema.py,parent_Schema.py,list_employee.json,list_of_parent.json,get_employee.json**: SX-220/make changes in employee and parent all files based on changes in API specs like request body ,schema for employee and parent ,email validation etc
- **constants.py,v1/employee.py,employee_schema.py,employee_exception.py**: SX-220/specify constant value for country in schema,also did some validation for integer,secondary phone number,gender ,rate and experience etc
- **database.py,employee_schema.py,routes/v1/employee.py**: SX-220/write code in without class in database.py file,delete update_employee schema
- **CHANGELOG.md**: update changelog file
- **employee_crud.py,parent_crud.py,player_crud.py,employee.py.parent.py,player.py,all-json-file**: changes all urls for api,update schemas,change crud file return schema object
- **parent_crud.py,employee_schema.py,parent_schema.py**: change the parent_id with customer_id and add address id in update and list api
- **employee_crud.py,player_crud.py,parent_crud.py,player_schema.py,parent_schema.py,amployee_schema.py,json-file**: change address schema ,urls format in player,parent and employee table
- **parent_schema.py,player_schema.py,employee_schema.py,employee_json,list_of_parent.json,list_employee.json**: change address schema which was in list format,inherited schema where it's duplicate and update json files
- **employee_crud.py,player_crud.py,parent_schema.py,test_config.py,common_exception.py**: change the test case for config ,write json file in try and except block,create custom exeption etc
- **test_config.py,employee_exception.py**: changes the test cases if variable not initialized properly
- **employee_crud.py,employee_schema.py,test_config.py,employee_exception.py**: validate the postal address,address street 1,street2,add the test case for config variable initialization
- **Dockerfile,constants.py,poetry.lock,test_healthcheck.py,CHANGELOG.md,.gitignore**: i have solve merge conflict with develop
- **Dockerfile,database.py**: add run command in dcokerfile and update the code in database
- **test_healthcheck.py**: modify value
- **constants.py,database.py,employess_schema.py**: log format has changed
- **parent_crud.py,player_crud.py,employee_crud.py,player.py,parent.py,employee.py**: change responses in files and status code also
- **employee_schema.py,player_schema.py,parent_schema.py,accounts.utils.py,list_of_parent.json,player.py,parent.py,employee.py**: i have validated field and using json file return static response and remove dictionary part
- **parent_crud,player_crud.py**: update this file
- **parent_crud.py,player_crud.py**: reformat the files

### Fix

- **DockerFile,entrypoint.sh,databse.py,test_healthcheck.py**: addedd run command in dockerr file (#4)

### Feat

- **player.py,parent.py,parent_schema.py,player_schema.py,player_crud.py,parent_crud.py,list_of_player.json**: i have created mock api for player and parent table and also did some changes in employee table
- **main.py,employee_crud.py,employee_schema.py,employee.py,employee_exception.py**: create a update employee and delete employee and list of employee api and exception also created
- **main.py,mock_employee.py,employee_schema.py**: create mock_employee file for create and get method
- **employee_schema.py,employee.py,main.py**: create schema for the employee and create api
