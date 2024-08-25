# Bash Scripts I wrote

## add_local_user.sh
<p>Written for Help Desk for easily adding users accounts on linux. Usage: <code>$ ./add_local_user.sh Username Realname</code>.</p>
<p>User must change password on login.</p>

## docker-on-docker.sh
Originally written when I was experimenting in Jenkins (as a Docker image) and needed to build a docker image without using an external node. I didn't know there was an official Docker in Docker image, and also there's no Jenkins on it... SCP this script to the container and run it to install Docker.

## tree-to-filesystem.sh
This script takes a graphical file structure (the ones AI chats usually give you) from file structure.txt and creates it using mkdir and touch commands.
Example for structure:
````
base_dir/
├── nested1/
│   ├── file1
│   ├── file2
│   └── nested2/
│       └── file3
├── file4
└── file5
````

## get_transaction_runtimes.sh
I did this script as an exam. I really enjoyed creating it and am very proud to have built it in like 30 minutes of learning lots of new stuff.
