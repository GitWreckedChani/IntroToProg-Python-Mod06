# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Chani,8.16.2021,Modified the original script
# Chani,8.17.2021,Edited for aesthetic
# Chani,8.17.2021,Edited for spelling and script breaks, addressed weak warnings
# Chani,8.17.2021,Edited Variables and Constants, added a Newline to print_current_task_list
# --------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #

# Declare variables and constants
file_name = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}   # {"priority": priority.strip(), "task": task.strip()}
list_of_rows = []  # A list that acts as a 'table' of rows
menu_choice = ""  # Captures the user option selection
task = ""  # Captures the user task data
priority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of a processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """ Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """
        Converts variables to a dictionary and appends dictionary to a list
        :param task: (string) key variable:
        :param priority: (string) key variable:
        :param list_of_rows: (list) you want to add a dictionary to:
        :return: (list) of dictionary rows
        """
        dicRow = {"Priority": priority.strip(), "Task": task.strip()}
        list_of_rows.append(dicRow)  # < adds this item(dic) to the list
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """
        Remove a dictionary from a list
        :param task: (string) key associated with dictionary:
        :param list_of_rows: (list) you want dictionary removed from:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            if task.lower() == row["Task"].lower():
                list_of_rows.remove(row)
                return list_of_rows, 'Success'

        print("Task not found.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Unpack a list of dictionaries and write that data to a file
        :param file_name: (string) file you want to write to
        :param list_of_rows: (list) you want to unpack
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")
        for dicRow in list_of_rows:
            objFile.write(dicRow["Priority"] + ' , ' + dicRow["Task"] + '\n')
        objFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """
        Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """
        Gets the menu choice from a user
        :return: string
        """
        menu_choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return menu_choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """
        Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current Tasks To Do are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """
        Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """
        Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """
        User assigns to the variables 'task' and 'priority'
        :return: task, priority
        """
        print("Record a chore, errand, or aspiration...\n\t(Example: \"Put out that kitchen fire - high priority)\"\n")
        task = input("\tDescribe the Task you're considering doing: ")
        priority = input("\tOn a relative scale, where would you prioritize this task?: ")
        print("YOU HAVEN'T ALREADY " + task + "!!!???")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """
        Gets a yes or no choice from the user
        :return: string
        """
        task = str(input("What would you like to remove?: ")).strip()
        return task


# Main Body of Script  ------------------------------------------------------ #

# When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, list_of_rows)  # read file data

# Display a menu of choices to the user
while True:
    # Show current data
    IO.print_current_Tasks_in_list(list_of_rows)       # Show current data in the list/table
    IO.print_menu_Tasks()                              # Show menu
    menu_choice = IO.input_menu_choice()               # Get menuChoice

    # Option 1 - Add New Data
    if menu_choice.strip() == '1':
        task, priority = IO.input_new_task_and_priority()         # Get users new task and priority
        Processor.add_data_to_list(task, priority, list_of_rows)   # Make a dic and add user input to Master List
                                                                  # Script pause
        IO.input_press_to_continue("\t\tI've added that to your to-do list!")
        continue                                                  # Show the menu

    # Option 2 - Remove an Existing Task
    elif menu_choice == '2':
        IO.print_current_Tasks_in_list(list_of_rows)       # Show current task list
        task = IO.input_task_to_remove()                   # Determine task to remove
                                                           # Ask yes/no if they want to remove
        choice = IO.input_yes_no_choice("Are you sure you want to remove *" + task + "*, (y or n)? ")
        if choice.lower().strip() == 'y':
            Processor.remove_data_from_list(task, list_of_rows)     # Search list for task and remove
        IO.input_press_to_continue()
        continue                                      # Show the menu

    # Option 3 - Save Data to File
    elif menu_choice == '3':
        choice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")     # Last stop
        if choice.lower().strip() == "y":                                       # Well okey then..
            Processor.write_data_to_file(file_name, list_of_rows)               # Append the list to the file
            IO.input_press_to_continue("To-Do List Has Been Saved!")  # Script break
        else:
            IO.input_press_to_continue("Save Cancelled!")      # Or don't
        continue                                                                # Show the menu

    # Option 4 - Reload Data from File
    elif menu_choice == '4':
        print("Warning: Unsaved Data Will Be Lost!")
        choice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if choice.lower().strip() == 'y':
            Processor.read_data_from_file(file_name, list_of_rows)    # Override the current list with file list
            IO.input_press_to_continue()                              # Script break
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")     # Script break
        continue                                                      # Show the menu

    # Option 5 - Exit Program
    elif menu_choice == '5':
        print("Goodbye!")
        break                                                          # Exit
