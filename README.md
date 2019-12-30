This is a Command Line Interface App built using python to implement Key-Value Store. 
For illustrating the concept, the key-value pair considered is- 
Key - Employee ID
Value - Name

Firebase database is used to store the Data. The mode opted for the db is "Realtime Database in Test Mode". 

The basic structure of the Database looks like this- 
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/db_structure.png)

Now, Firebase provides a REST API for the database. Hence, this API is used to develop the CLI commands as illustrated - 

All the commands start with - employee
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-command.png)

Command - 1
employee --help

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-command.png)

Command - 2
employee add (employee_id) -n (employee_name)
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-add.png)

Command - 3
employee list-all
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-list-all.png)

Command - 4
employee view (employee_id)

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-view.png)

Command - 5
employee update (employee_id) -n (name)
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-update.png)

Command - 6
employee delete (employee_id)
![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-delete.png)
