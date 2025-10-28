#!/usr/bin/python3

# INET4031
# Wyatt Halsa
# Date Created: 10/27/2025
# Date Last Modified: 10/27/2025

# This script automates adding multiple users to a Linux system.
# It reads user data from an input file and creates accounts,
# sets passwords, and assigns group memberships.
# It can run in “dry-run” mode to simulate commands
# without actually making system changes.

import os
import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: sudo ./create-users2.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Ask user if they want to do a dry run
    dry_input = input("Would you like to do a dry run? (Y/N): ").strip().lower()
    dry_run = dry_input == 'y'

    comment_pattern = re.compile(r'^\s*#')

    # Read from the input file
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Skip comment lines
            if comment_pattern.match(line):
                if dry_run:
                    print(f"Skipping line (comment): {line}")
                continue

            fields = line.split(':')

            # Validate field count
            if len(fields) != 5:
                if dry_run:
                    print(f"Error: Line does not have 5 fields: {line}")
                continue

            # Extract user information from fields
            username = fields[0]
            password = fields[1]
            last_name = fields[2]
            first_name = fields[3]
            groups_field = fields[4]

            gecos = f"{first_name} {last_name},,,"
            groups = groups_field.split(',')

            # Display what’s being done
            print(f"==> Creating account for {username}...")

            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            if dry_run:
                print(f"[Dry-run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Set password
            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            if dry_run:
                print(f"[Dry-run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Assign user to groups
            for group in groups:
                if group.strip() == '-' or group.strip() == '':
                    continue
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(f"[Dry-run] Would run: {cmd}")
                else:
                    os.system(cmd)


if __name__ == '__main__':
    main()
