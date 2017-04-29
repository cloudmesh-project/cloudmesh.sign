#!/bin/sh
echo 'Install Ansible '
echo '--------------------------------'
sudo apt-get install ansible
echo 'Setup Local Environment for Cloudmesh_Client'
echo '--------------------------------'
rm hosts
touch hosts
ansible-playbook env_setup.yaml --ask-sudo-pass -v
echo 'Add newly created vms to host'
echo '--------------------------------'
chmod u+x host_edit.sh
./host_edit.sh
echo 'Configure Cluster Nodes for OpenCV '
echo '--------------------------------'
rm $HOME/.ssh/known_hosts
touch $HOME/.ssh/known_hosts
ansible-playbook opencv_setup.yaml -i hosts --ask-sudo-pass -v


