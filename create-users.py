#!/usr/bin/python3

# INET4031
# Wyatt Halsa
# Date Created 10/27/2025
# Last Modified 10/27/2025

# os: Executing system commands to create users and groups
# re: Use regular expressions to detect comment lines
# sys: Read input from standard input
import os
import re
import sys


def main():

	# Loop through each line of input from input file
    for line in sys.stdin:

        # Check if the line starts with #
        match = re.match("^#",line)

        #Split each  line into fields bases on colon
        fields = line.strip().split(':')

        # Skip this line if it is a comment or does not have exactly 5 fields.
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0] # Login name
        password = fields[1] # Password
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split group list field into individual groups
        groups = fields[4].split(',')

        # Show user what account is being created
        print("==> Creating account for %s..." % (username))
        # Build the system command to create user with no password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        os.system(cmd)

        # Inform the user that the password is being set
        print("==> Setting the password for %s..." % (username))
        # Build the system command to set the password for the user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        os.system(cmd)
        for group in groups:
            # If the group is not empty add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
            os.system(cmd)

if __name__ == '__main__':
    main()
