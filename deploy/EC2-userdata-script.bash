sudo yum install -y git
cd /home/ec2-user
git clone https://github.com/drumadrian/aws-bathroom-status-app.git
bash aws-bathroom-status-app/deploy/configureBathroomAppConfigInstance.bash

