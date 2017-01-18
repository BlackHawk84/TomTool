#!/bin/bash

SERVICE=$1  # "wlag" | "wluic" | "wlscheduler"
ACTION=$2  # "status" | "start" | "stop" | "restart"
PASSWORD=$3  # password

FILE="/etc/init.d/$SERVICE"
if [ -f $FILE ];
then
    echo "SUCCESS"
    cmd="echo $PASSWORD | sudo -S $FILE $ACTION"
    eval `echo $cmd`
else
    echo "FAILURE"
    echo "File $FILE does not exist."
fi

