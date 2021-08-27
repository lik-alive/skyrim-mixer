#!/bin/bash

reload () {
    if [ "$(sudo -u www-data pm2 id $2)" = "[]" ]; then
        sudo -u www-data pm2 start $1 --name $2 --interpreter python3
    else 
        sudo -u www-data pm2 reload $1
    fi
}

reload server.py skymix_server
