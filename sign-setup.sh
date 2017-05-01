
# CM_USER , chameleon user can be different from local USER env variable
export CM_USER=`cm info | grep user| awk  '{print $4}'`


