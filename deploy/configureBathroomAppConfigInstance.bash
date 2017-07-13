############################################################
# Sources: 
# 	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
# 	
############################################################
# Note: This script mostly runs from the ec2-user's home directory

echo -e "\n\n ######### Installing system updates and Prerequisites #########  \n"

cd
sudo yum update
echo -e "\n COMPLETED: sudo yum update -y \n"

sudo yum install -y yum-utils
echo -e "\n COMPLETED: sudo yum -y install yum-utils \n"

sudo yum groupinstall development
echo -e "\n COMPLETED: sudo yum -y groupinstall development \n"

sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
echo -e "\n COMPLETED: sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm \n"

sudo yum install -y python36u
echo -e "\n COMPLETED: sudo yum -y install python36u \n"


echo ""
echo ""
echo "your Python version is now: "
python3.6 -V
echo ""
echo ""


sudo yum install -y python36u-pip
echo -e "\n COMPLETED: sudo yum -y install python36u-pip \n"

sudo yum install -y python36u-devel
echo -e "\n COMPLETED: sudo yum -y install python36u-devel \n"

sudo pip3.6 install json
echo -e "\n COMPLETED: sudo pip3.6 install json \n"

sudo pip3.6 install os
echo -e "\n COMPLETED: sudo pip3.6 install os \n"



echo -e "\n\n ######### Setting up Python Virtual Environment #########  \n"

cd
mkdir environments
cd environments
python3.6 -m venv venvironmentforconfig
source venvironmentforconfig/bin/activate

echo -e "\n\n ######### COMPLETED:  system updates and Prerequisites: COMPLETED #########  \n"







echo -e "\n\n ######### Running The Bathroom App System Config Script #########  \n"

cd
python aws-bathroom-status-app/deploy/config-script.py






