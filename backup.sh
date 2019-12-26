#!/bin/bash

# This script is ment to run once a day.
#
# In /etc/crontab
# 0 4 * * *     /home/pi/modbus-reader/backup.sh

influxd backup -portable -database energy -start $(date --date="${dataset_date} -1 day" --utc +%FT%TZ) /mnt/backup
