#!/bin/bash
if [[ "$#" == "0" ]];
then
	y=$(date +'%Y')
        else
	y=$1
fi

a=$(( y%19 ))
b=$(( y%4 ))
c=$(( y%7 ))
d=$(( (16+19*a)%30 ))
e=$(( ((2*b)+(4*c)+(6*d))%7 ))
day=$(( 3+d+e ))
if [ $day -le 30 ];
	then
	month=4
	if [ $y -lt $(date +'%Y') ];
		then
		echo "Το Πάσχα το έτος $y ήταν την $dayη Aπριλίου"
 		elif [ $y -gt $(date +'%Y') ];
		then
        	echo "Το Πάσχα το έτος $y θα ειναι την $dayη Aπριλίου"
		else 
		if [ $month -lt $(date +'%-m') ];
			then
			echo "Το Πάσχα φέτος ήταν την "$day"η Aπριλίου"
			else
			echo "Το Πάσχα φέτος θα είναι την "$day"η Aπριλίου"
		fi
		
	fi
	else
	day=$(( $day-30 ))
	month=5
	if [ $y -lt $(date +'%Y') ];
		then
		echo "Το Πάσχα το έτος $y ήταν την "$day"η Μαίου"
		elif [ $y -gt $(date +'%Y') ];
		then
		echo "Το Πάσχα το έτος $y θα ειναι την "$day"η Μαίου"
		else
		if [ $month -lt $(date +'%-m') ];
			then
			echo "Το Πάσχα φέτος ήταν την "$day"η Μαίου"
			else
			echo "Το Πάσχα φέτος θα είναι την "$day"η Μαίου"
		fi
	fi

fi

EASTER=$(date --date="$y-$month-$day" +"%d/%m/%Y")
MEGALO_SABBATO=$(date --date="$y-$month-$day -1 day" +"%d/%m/%Y")
MEGALI_PARASKEVI=$(date --date="$y-$month-$day -2 days" +"%d/%m/%Y")
MEGALI_PEMPTI=$(date --date="$y-$month-$day -3 days" +"%d/%m/%Y")
MEGALI_TETARTI=$(date --date="$y-$month-$day -4 days" +"%d/%m/%Y")
MEGALI_TRITI=$(date --date="$y-$month-$day -5 days" +"%d/%m/%Y")
MEGALI_DEYTERA=$(date --date="$y-$month-$day -6 days" +"%d/%m/%Y")

#echo "---------------------------------------------"
#echo " Μεγάλη Δευτέρα     |" $MEGALI_DEYTERA
#echo "---------------------------------------------"
#echo " Μεγάλη Τρίτη       |" $MEGALI_TRITI 
#echo "---------------------------------------------"
#echo " Μεγάλη Τετάρτη     |" $MEGALI_TETARTI
#echo "---------------------------------------------"
#echo " Μεγάλη Πέμπτη      |" $MEGALI_PEMPTI
#echo "---------------------------------------------"
#echo " Μεγάλη Παρασκευή   |" $MEGALI_PARASKEVI
#echo "---------------------------------------------"
#echo " Μεγάλο Σάββατο     |" $MEGALO_SABBATO
#echo "---------------------------------------------"
#echo " Κυριακή του Πάσχα  |" $EASTER 
#echo "---------------------------------------------"
 
