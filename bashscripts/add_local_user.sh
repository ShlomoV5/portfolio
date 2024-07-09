#!/bin/bash

#############################################
# ADD LOCAL USER SCRIPT                     #
#############################################

# This script adds a local user. Checks if action was successfull
# And returns a nice user ticket

# Check if root user:
if [[ "${UID}" -ne 0 ]] # not root user
then
    echo "Your are not authorized for this action! This script will exit."
    exit 1
fi

# Accept user details from prompt
read -p "Enter the desired username: " USER_NAME
read -p "Enter the user's real name: " REAL_NAME
read -p "Enter desired password: " PASSWORD

# Create the user
useradd -c "${REAL_NAME}" -m "${USER_NAME}"

# Validate if user was created (exit code 0)
if [[ "${?}" -ne 0 ]] # last action returned an error
then
    echo "Error creating user! This script will exit."
    exit 1
fi

# Set user password
echo "${USER_NAME}:${PASSWORD}" | chpasswd

# Validate if password was set (exit code 0)
if [[ "${?}" -ne 0 ]] # last action returned an error
then
    echo "Error setting password! This script will exit."
    exit 1
fi

# Force password reset on first login
passwd -e ${USER_NAME}

# Create an easy-to-read summary of new user details for Help Desk

echo -e "User created succesfully! Here are the user details for: \e[4m${REAL_NAME}\e[0m"
echo -e "\e[4mUsername\e[0m: ${USER_NAME}"
echo -e "\e[4mPassword\e[0m: ${PASSWORD}"
echo -e "\e[4mHostname\e[0m: ${HOSTNAME}"
echo ""

# DEBUG INFO. REMOVE FOR REAL USE
# Info from /etc/passwd:
echo "Debug info:"
echo "Last user register on /etc/passwd:"
tail -1 /etc/passwd
echo ""

# Delete the user
echo "Deleting user '${USER_NAME}!' No need for it any more."
deluser $USER_NAME
