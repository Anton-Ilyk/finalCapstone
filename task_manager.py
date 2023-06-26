# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: pass
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
import time

from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

next_task = 0

#Add new task
def add_task():
    
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    while(True):
        if task_username not in username_password.keys():
            print("\nUser does not exist. Please enter a valid username\n")
            continue
        else:
            break
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "num_task": next_task,
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)

    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['num_task'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    renew_tasks()
#Reg new user function
def reg_user():
    while(True):
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")
        
        if new_username in username_password.keys():
            print("\nUsername exist!\nTry other username!\n")
            continue

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
                
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
                break

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

#My tasks show function
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
    '''
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"------------------Task Number: {t['num_task']}--------------------\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Task Completed:  {t['completed']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += "-----------------------------------------------------\n"
            print(disp_str)
    specific_task()

#Function which shows all tasks
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
    '''
    for t in task_list:
            disp_str = f"\n------------------Task Number: {t['num_task']}--------------------\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Task Completed:  {t['completed']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += "-----------------------------------------------------\n"
            print(disp_str)    

#Specific task show function
def specific_task(): 
    while(True):

        #Check if user input number correctly
        while(True):
            try:
                task_num = input("\nInput number of task which you want to see(input \"-1\" to exit): ")
                task_num = int(task_num)
                break
            except:
                print("\nInput CORRECT number of the task!\n")
                time.sleep(1)
        #Check and print task only if it exists; -1 input will move user to main menu
        if task_num != -1:
            task_dict = []
            for f in task_list:
                task_num = str(task_num)
                if task_num in f.get('num_task'):
                    task_dict = f
            #Displaying specific task
            if (task_dict != [] and f['username'] == curr_user) or (task_dict != [] and curr_user == "admin"):        
                task_str = f"\n------------------Task Number: {task_dict['num_task']}--------------------\n"
                task_str += f"Task: \t\t {task_dict['title']}\n"
                task_str += f"Task Completed:  {task_dict['completed']}\n"
                task_str += f"Assigned to: \t {task_dict['username']}\n"
                task_str += f"Date Assigned: \t {task_dict['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                task_str += f"Due Date: \t {task_dict['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                task_str += f"Task Description: \n {task_dict['description']}\n"
                task_str += "-----------------------------------------------------\n"
                print(task_str)

                task_modif(task_num)
               
            else:
                print("\nThis task doesn`t exist or this task assigned to other user!\n")
                time.sleep(1)           
        else:
            break    

#Function for task editing
def task_modif(task_num):
    upd_check = True
    while(True):
        edit_task = input("\nWould you like to edit or mark as a completed any of these tasks?\nTo edit the task print - edit, to mark task as a completed print - complete: ")
        if edit_task == "edit" or edit_task == "complete":
            break
        else:
            print("\nYou choose incorrect type of procedure!\n")
            time.sleep(1)  
            continue
    #Collecting new info about this task from user input       
    for j in task_list:
        if edit_task == "edit" :
            if j['num_task'] == task_num and j['completed'] == True:
                print("\nYou can`t edit completed task!\n")
                upd_check = False

            elif j['num_task'] == task_num and j['completed'] == False:    
                while(True):
                    task_username = input("Name of person you want to re-assign the task: ")
                    if task_username not in username_password.keys():
                        print("\nUser does not exist. Please enter a valid username\n")
                        time.sleep(1)
                        continue
                    else:
                        break

                task_title = input("The new title of the task: ")
                task_description = input("The new description of the task: ")

                while True:
                    try:
                        task_due_date = input("Updated due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
                
                j['username'] = task_username
                j['title'] = task_title
                j['description'] = task_description
                j['due_date'] = due_date_time
                

        elif j['num_task'] == task_num and edit_task == "complete" and j['completed'] == False:
            j['completed'] = "Yes"

        elif j['num_task'] == task_num and edit_task == "complete" and j['completed'] == True:
            print("\nThis task already completed!\n")
            upd_check = False
    #Final check if program can and need rewrite txt file with tasks
    if upd_check == True:    
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['num_task'],
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("\nTask successfully edited or completed!\n")
        renew_tasks()
# Function which generates tasks report
# wr_check defines type of report which will be created
# 1 - for saving report in txt file
# 2 - for displaying real time report
# 3 - for displaying report log from txt file    
def generate_reports(wr_check):
    
    # Create tasks.txt if it doesn't exist
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass

    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
             
    num_tasks = len(task_list)
    num_users = len(username_password.keys())
    comp_tasks = 0
    uncomp_tasks = 0
    ovd_tasks = 0 
    for j in task_list:

        if j['completed'] == True:
            comp_tasks += 1
        elif datetime.now() < j['due_date'] and j['completed'] == False:
            uncomp_tasks += 1
        elif datetime.now() > j['due_date'] and j['completed'] == False:
            ovd_tasks += 1

    #Brief task overview report
    report_str = f"-------------Brief tasks report-------------\n---------{datetime.now()}---------\n\n"
    report_str += f"Total amount of tasks: \t\t\t{num_tasks}\n"
    report_str += f"Total amount of completed tasks: \t{comp_tasks}\n"
    report_str += f"Total amount of uncompleted tasks: \t{uncomp_tasks}\n"
    report_str += f"Total amount of overdue tasks: \t\t{ovd_tasks}\n"
    report_str += f"Percentage of incomplete tasks: \t{round(uncomp_tasks / num_tasks * 100, 2)}%\n"
    report_str += f"Percentage of overdue tasks: \t\t{round(ovd_tasks / num_tasks * 100, 2)}%\n"
    report_str += "--------------------------------------------------\n"
    
    #Check if we need save report in txt file, display it or display log-report
    if wr_check == 0:
        with open("task_overview.txt", "a") as task_file:
            task_file.write(f"{report_str}\n")
            print("\nBrief report succesfully saved to task_overview.txt!\n")
    elif wr_check == 1:
        print(report_str) 
    elif wr_check == 2:
        brief_report = open('task_overview.txt', 'r')
        for line in brief_report:
            print(line)
        brief_report.close()
    
    #Detailed report for each user
    user_rep_str = f"-------------Users tasks report-------------\n---------{datetime.now()}---------\n\n"
    user_rep_str += f"Total amount of users: \t\t\t{num_users}\n"
    user_rep_str += f"Total amount of tasks: \t\t\t{num_tasks}\n"

    for t in username_password.keys():
        usr_tasks = 0
        usr_comp_tasks = 0
        usr_uncomp_tasks = 0
        us_ovd_tasks = 0

        for j in task_list:
            if t == j['username']:
                usr_tasks += 1
                if j['completed'] == True:
                    usr_comp_tasks += 1
                elif datetime.now() < j['due_date'] and j['completed'] == False:
                    usr_uncomp_tasks += 1
                elif datetime.now() > j['due_date'] and j['completed'] == False:
                    us_ovd_tasks += 1
         
        user_rep_str += f"\n----------------- USER: {t} -----------------\n"
        user_rep_str += f"Total amount of tasks for {t}: \t{usr_tasks}\n"
        user_rep_str += f"Percentage of total tasks: \t\t{round(usr_tasks / num_tasks * 100, 2)}%\n"
        user_rep_str += f"Percentage of completed tasks: \t\t{round(usr_comp_tasks / usr_tasks * 100, 2)}%\n"
        user_rep_str += f"Percentage of incompleted tasks: \t{round(usr_uncomp_tasks / usr_tasks * 100, 2)}%\n"
        user_rep_str += f"Percentage of overdue tasks: \t\t{round(us_ovd_tasks / usr_tasks * 100, 2)}%\n"
        user_rep_str += "-----------------------------------------------\n"
    #Check if we need save report in txt file, display it or display log-report
    if wr_check == 0:
        with open("user_overview.txt", "a") as user_file:
            user_file.write(f"{user_rep_str}\n")
            print("\nUsers report succesfully saved to user_overview.txt!\n")
    elif wr_check == 1:
        print(user_rep_str)
    elif wr_check == 2:
        user_report = open('user_overview.txt', 'r')
        for line in user_report:
            print(line) 
        user_report.close()       

#Function for easily choose type of report which is needed to user       
def report_check():
    while(True):
        num_rep = str(input("\nYou can choose two type or reports. Available options:\n1. If you would like to see live report\n2. If you would like to see report log\n"))
        if num_rep == "1" or num_rep == "2":
            break
        else:
            print("\nYou choose incorrect type of procedure!\n")
            time.sleep(1)  
            continue
    
    if num_rep == "1":
        generate_reports(1)
    elif num_rep == "2":
        generate_reports(2)

#Function for renew data of tasks after each action with it`s(like additing, adding the new one)
def renew_tasks():
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
    renew_list = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['num_task'] = task_components[0]
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[6] == "Yes" else False

        renew_list.append(curr_t)
    global task_list 
    global next_task 
    next_task = str(int(curr_t['num_task']) + 1)   
    task_list = renew_list
       

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['num_task'] = task_components[0]
    curr_t['username'] = task_components[1]
    curr_t['title'] = task_components[2]
    curr_t['description'] = task_components[3]
    curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[6] == "Yes" else False

    task_list.append(curr_t)
    
    next_task = str(int(curr_t['num_task']) + 1)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
rc - Display current report or report log
e - Exit
: ''').lower()
    
    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
               
    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports(0) 

    elif menu == 'rc':
        report_check()
                            
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")