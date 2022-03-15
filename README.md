# Synopsis

The Airbnb clone project for which we are creating a copy of the Airbnb


## Features

### Command Interpreter

#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Retrieve an object from a file.
+ Update object's attributes.
+ Destroy an object.

#### Usage

```./console.py ```

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** | Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Bugs
+ No known bugs at this time.
