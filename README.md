This is a Command Line Interface (CLI) App built using python to implement Key-Value Store. 
For illustrating the concept, the key-value pair considered is- 
</br>
</br>
**Key - Employee ID**
</br>
**Value - Name**
</br>

<b>Firebase</b> database is used to store the Data. The mode opted for the db is "Realtime Database in Test Mode".

The basic structure of the Database looks like this- 

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/db_structure.png)

Now, Firebase provides a REST API for the database. Hence, this API is used to develop the CLI commands as illustrated - 

All the commands start with - employee

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-command.png)

<h2>Command - 1 (to list all the commands)</h2>

employee --help

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-help.png)

<h2>Command - 2 (To add an employee, i.e to set the key-Value Pair)</h2>

employee add (employee_id) -n (employee_name)

The command inserts a new entry to the database, as shown, however if the employee_id is already there, it shows a message saying "Employee ID is already assigned to someone, use another ID "

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-add.png)

<h2>Command - 3 (To list all the employees)</h2>

employee list-all

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-list-all.png)

<h2>Command - 4 (To view a particular employee, i.e. to get the value for a particular key)</h2>

employee view (employee_id)

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-view.png)

<h2>Command - 5 (To update the info of an employee)</h2>

employee update (employee_id) -n (name)

If the user tries to update an existing id, it does that very smoothly, however, if a value that is not in the database, is accessed, it shows a message saying "The Employee you're trying to update dosen't exist, you may add new !!"

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-update.png)

<h2>Command - 6 (To delete a record) </h2>

employee delete (employee_id)

![alt text](https://github.com/aimanfatima/key-value-store-cli/blob/master/media/employee-delete.png)
