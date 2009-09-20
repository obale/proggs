#!/bin/sh
data='/tmp/gps_raw.txt'

count=0

while [ $count -lt 2 ]; do
	head -n20 /dev/ttySAC1 > ${data}
	unset ret
	ret=$(cat ${data} | grep '^$GPGSA' | awk -F, '{ print $3 }')
	eval=$(echo $ret | awk -F\  '{ print $1 }')
	if [ "$eval" = "1" ]; then 
		spd-say "No GPS fix acquired!"
	elif [ "$eval" = "2" ]; then 
		spd-say "GPS 2D fix acquired!"
		count=$(expr ${count} + 1)
	elif [ "$eval" = "3" ]; then
		spd-say "GPS 3D fix acquired!"
		count=$(expr ${count} + 1)
	else
	#	echo "No information available. Please try it another time."
		spd-say "No information available. Please try it another time."
	fi
	sleep 15
done
