############################################################
# Sources: 
# 	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
# 	https://www.tecmint.com/install-python-in-linux/
# 	https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv
#	https://forums.aws.amazon.com/thread.jspa?messageID=705010
#	https://gist.github.com/diegopacheco/ee7ac81deb6e33a8cf7ae9f674e0df6a
# 	http://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html
# 	https://gist.github.com/drumadrian/150c9adcb79f16be003951ff31613c21
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

wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
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

cd /home/ec2-user
mkdir /home/ec2-user/environments
cd /home/ec2-user/environments

pip install --upgrade virtualenv
echo -e "\n COMPLETED: pip install --upgrade virtualenv \n"

virtualenv -p python3 venvironmentforconfig
echo -e "\n COMPLETED: virtualenv -p python3 venvironmentforconfig \n"

source venvironmentforconfig/bin/activate
echo -e "\n COMPLETED: source venvironmentforconfig/bin/activate \n"


pip install boto3
echo -e "\n COMPLETED: pip install boto3 \n"

cd /home/ec2-user
pip install -r /home/ec2-user/aws-bathroom-status-app/requirements.txt
echo -e "\n COMPLETED: pip install -r /home/ec2-user/aws-bathroom-status-app/requirements.txt \n"


# pip install json
# echo -e "\n COMPLETED: pip install json \n"

# pip install os
# echo -e "\n COMPLETED: pip install os \n"




echo -e "\n\n ######### Begin Node.js SETUP #########  \n"


cd /home/ec2-user
wget https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh -O /home/ec2-user/install.sh
echo -e "\n COMPLETED: https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh /home/ec2-user/install.sh \n"

NVM_DIR=/usr/bin
echo -e "\n COMPLETED: NVM_DIR=/usr/bin \n"

bash /home/ec2-user/install.sh
echo -e "\n COMPLETED: bash /home/ec2-user/install.sh \n"


chmod -R 744 /root/.nvm/*
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

echo -e "\n COMPLETED: nvm setup \n"

# mv /usr/bin/nvm.sh /usr/bin/nvm
cp /root/.nvm/nvm.sh /usr/bin/nvm
echo -e "\n COMPLETED: cp /root/.nvm/nvm.sh /usr/bin/nvm \n"

nvm install 4.3
echo -e "\n COMPLETED: nvm install 4.3 \n"

node -e "console.log('Running Node.js ' + process.version)"


# Stopped here for Node setup.  The node environment is already in the git repo



















echo -e "\n\n ######### COMPLETED:  system updates and Prerequisites: COMPLETED #########  \n"



echo -e "\n\n ######### Starting The Bathroom App System Config Script #########  \n"

cd /home/ec2-user
mkdir /home/ec2-user/outputs
python aws-bathroom-status-app/deploy/config-script.py


deactivate


echo -e "\n\n ######### COMPLETED: The Bathroom App System Config Script #########  \n"







