#!/bin/bash

eval "$(ssh-agent -s)"
chmod 600 deploy_rsa
ssh-add deploy_rsa

scp -o StrictHostKeyChecking=no noarch/tigeros-backgrounds-1.0-16.fc27.noarch.rpm zethra@zserv.student.rit.edu:.
