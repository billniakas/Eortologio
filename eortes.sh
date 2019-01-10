#!/bin/bash
if [[ "$#" == "0" ]];
then
	datevar=$(date +'%-d/%-m')
        else
	datevar=$1
fi

# echo $datevar
if [[ $datevar == $(date +'%-d/%-m') ]];
	then
	date_message="Σήμερα"
	else
	date_message="Στις $datevar"
fi
simera=$(cat < eortes.dat | grep -Pzo "\b"$datevar" : \K[^\w]*" | tr -d '\0')   # για κάποιο λόγο βγάζει null byte
bytlen=${#simera}
if [ $bytlen = 0 ];
	then
	echo "Καμία γιορτή σήμερα"
	else
	#echo "$date_message γιορτάζει"
	echo "$simera"
fi

