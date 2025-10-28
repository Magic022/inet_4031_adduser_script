# INET4031 Add Users Script and User List

## Program Description
This Python program automates the process of adding multiple users and groups to an Ubuntu system. Normally, a system administrator would manually run commands such as `adduser`, `passwd`, and `usermod` to create each account, set passwords, and assign users to groups. This script performs all of these tasks automatically by reading from an input file, eliminating repetitive manual work and reducing the chance of errors. Administrators can efficiently provision multiple accounts on a server with a single command.


## Program User Operation
The script reads a list of user accounts and group assignments from a structured input file and executes system commands to create users, set passwords, and assign group memberships. The user must prepare the input file and then run the script either in a "dry run" mode to verify the actions or in full execution mode to actually create the users.

### Input File Format
The input file is a colon-delimited text file with **five fields per line** in the following order:

1. **Username** – The login name for the new account.  
2. **Password** – The initial password for the account.  
3. **Last Name** – The user’s last name.  
4. **First Name** – The user’s first name.  
5. **Groups** – A comma-separated list of supplemental groups the user should belong to. If a user should not belong to any additional groups, use a single `-`.  

**Special instructions:**
- To skip a line, start the line with `#`.  
- Lines that do not contain exactly five fields are ignored automatically by the script.

### Command Execution
Before running the script, ensure it is executable:  
bash
chmod +x create-users.py
Run the script by redirecting the input file:

bash
Copy code
./create-users.py < create-users.input
For full execution with system modifications, run with sudo:

bash
Copy code
sudo ./create-users.py < create-users.input
The script will then create the users, set passwords, and assign them to the specified groups automatically.

Dry Run
A dry run allows the user to test the script without making any changes to the system. To perform a dry run, keep all os.system(cmd) commands commented out in the script. During a dry run, the script will print all the commands that would be executed, allowing the administrator to verify correctness and catch any input file errors before performing real operations.
