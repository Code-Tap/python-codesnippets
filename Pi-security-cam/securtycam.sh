#!/bin/bash

DATE=$(date +"%d-%m-%Y_%H"00)

raspistill -o /home/pi/$DATE.jpg

python3 /home/pi/send-email.py "Security Pi $Date" "/home/pi/$DATE.jpg"

rm /home/pi/$DATE.jpg

