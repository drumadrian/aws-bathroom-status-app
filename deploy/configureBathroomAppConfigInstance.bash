############################################################
# Sources: 
# 	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
# 	
############################################################


echo -e "\n\n ######### Installing system updates and Prerequisites #########  \n"

cd
sudo yum -y update
echo -e "\n COMPLETED: sudo yum -y update \n"

sudo yum -y install yum-utils
echo -e "\n COMPLETED: sudo yum -y install yum-utils \n"

sudo yum -y groupinstall development
echo -e "\n COMPLETED: sudo yum -y groupinstall development \n"

sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
echo -e "\n COMPLETED: sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm \n"

sudo yum -y install python36u
echo -e "\n COMPLETED: sudo yum -y install python36u \n"


echo ""
echo ""
echo "your Python version is now: "
python3.6 -V
echo ""
echo ""


sudo yum -y install python36u-pip
echo -e "\n COMPLETED: sudo yum -y install python36u-pip \n"

sudo yum -y install python36u-devel
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


echo -e "\n\n ######### Cloning Git Repo #########  \n"

sudo yum install -Y git
cd 
git clone https://github.com/drumadrian/aws-bathroom-status-app.git



echo -e "\n\n ######### COMPLETED #########  \n"


