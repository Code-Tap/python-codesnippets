#!/bin/bash

LOCK=/tmp/lock
echo "Lockfile test"
if [ -f $LOCK ]; then            # 'test' -> race begin
  echo Job is already running\!
  exit 6
fi

function clean_up {
	# Perform program exit housekeeping
        echo "Remove Lockfile"
	rm $LOCK 2>/dev/null
        echo "Clear PHAT LED"
        /usr/bin/python3 /root/msg.py &
}

trap "clean_up; exit" 0 1 2 3 15

echo "Create lockfile"
>$LOCK
echo "Start Phat"
/usr/bin/python3 /root/cpuphat.py &
PID=$!
echo "Process ID - $PID"
echo "Start PDF Script"
/usr/bin/python3 /root/PdfSplit.py
echo "Kill it With Fire"
kill -9 $PID
exit
