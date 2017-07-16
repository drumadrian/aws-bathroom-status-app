############################################################
# Sources: 
# 	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
# 	https://www.tecmint.com/install-python-in-linux/
# 	https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv
#	https://forums.aws.amazon.com/thread.jspa?messageID=705010
#	https://gist.github.com/diegopacheco/ee7ac81deb6e33a8cf7ae9f674e0df6a
# 	
############################################################
# Note: This script mostly runs from the ec2-user's home directory

echo -e "\n\n ######### Installing system updates and Prerequisites #########  \n"


cd /home/ec2-user
echo -e "\n COMPLETED: cd /home/ec2-user \n"

# su ec2-user
# echo -e "\n COMPLETED: su ec2-user \n"

whoami
echo -e "\n COMPLETED: whoami \n"

yum -y update
echo -e "\n COMPLETED: yum update -y \n"

yum -y install yum-utils
echo -e "\n COMPLETED: yum -y install yum-utils \n"

yum -y groupinstall development
echo -e "\n COMPLETED: yum -y groupinstall development \n"

yum -y install zlib-devel
echo -e "\n COMPLETED: yum -y install zlib-devel \n"

# wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
echo -e "\n COMPLETED: wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz \n"

tar xJf Python-3.6.0.tar.xz
echo -e "\n COMPLETED: tar xJf Python-3.6.0.tar.xz \n"

cd Python-3.6.0
echo -e "\n COMPLETED: cd Python-3.6.0 \n"

./configure
echo -e "\n COMPLETED: ./configure \n"

make
echo -e "\n COMPLETED: make \n"

make install
echo -e "\n COMPLETED: make install \n"







echo "export PATH=$PATH:/usr/local/bin/python3"
export PATH=$PATH:/usr/local/bin/python3




echo ""
echo ""
echo "(might not work for root user) your Python version is now: "
python3 -V
echo ""
echo ""


yum install -y python34-setuptools
echo -e "\n COMPLETED: yum install -y python34-setuptools \n"

easy_install-3.4 pip
echo -e "\n COMPLETED: easy_install-3.4 pip \n"

pip install --upgrade pip
echo -e "\n COMPLETED: pip install --upgrade pip \n"

echo -e "\n\n ######### Setting up Python Virtual Environment #########  \n"

cd
mkdir environments
cd environments

pip install --upgrade virtualenv
echo -e "\n COMPLETED: pip install --upgrade virtualenv \n"

virtualenv -p python3 venvironmentforconfig
echo -e "\n COMPLETED: virtualenv -p python3 venvironmentforconfig \n"

source venvironmentforconfig/bin/activate
echo -e "\n COMPLETED: source venvironmentforconfig/bin/activate \n"


pip install boto3
echo -e "\n COMPLETED: pip install boto3 \n"

# pip install json
# echo -e "\n COMPLETED: pip install json \n"

# pip install os
# echo -e "\n COMPLETED: pip install os \n"


echo -e "\n\n ######### COMPLETED:  system updates and Prerequisites: COMPLETED #########  \n"







echo -e "\n\n ######### Starting The Bathroom App System Config Script #########  \n"

cd /home/ec2-user
mkdir outputs
python aws-bathroom-status-app/deploy/config-script.py


deactivate


echo -e "\n\n ######### COMPLETED: The Bathroom App System Config Script #########  \n"

