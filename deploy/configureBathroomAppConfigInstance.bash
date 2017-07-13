############################################################
# Sources: 
# 	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
# 	
############################################################


cd
sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u
echo ""
echo ""
echo "your Python version is now: "
python3.6 -V
echo ""
echo ""
sudo yum -y install python36u-pip
sudo yum -y install python36u-devel
sudo pip3.6 install json
sudo pip3.6 install os

cd
mkdir environments
cd environments
python3.6 -m venv venvironmentforconfig
source venvironmentforconfig/bin/activate

sudo yum install -Y git
cd 
git clone https://github.com/drumadrian/aws-bathroom-status-app.git


