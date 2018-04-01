eval "$(ssh-agent -s)"
chmod 600 .travis/deploy_rsa
ssh-add .travis/deploy_rsa

scp noarch/tigeros-backgrounds-1.0-16.fc27.noarch.rpm zethra@zserv.student.rit.edu:.
