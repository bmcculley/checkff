#!/bin/bash
check() {
	CURVERSION=`firefox -v | awk '{print $3}'`
	echo `python checkff.py $CURVERSION`
}

if check; then
	echo "we are good to go."
else
	echo "we need an update."
fi