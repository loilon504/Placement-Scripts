#!/bin/bash

numTest=5

# for i in 5 10 50 100 200 500 1000 2000 5000 10000
#for i in 5 10 50 100 200 500
# for i in 2000 5000 10000
# for i in 5 10 50 100
for i in 10
do
	if [ "$i" -gt 500 ] 
	then numTest=2
	else numTest=5
	fi

    for ((j = 1; j <= 1; j++)) do
	# for ((j = 1; j <= $numTest; j++)) do
		echo "test$i-$j "
        ./mpboot-avx -pp_on -pp_n $i -pp_k $i -s ../../data/test$i/$j/added$i.vcf -pp_tree ../../data/test$i/$j/origin$i.fasta.treefile -pp_origin ../../data/test$i/$j/origin$i.fasta.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure > placementRun$i-$j.txt
		# ./mpboot-avx -s ../../data/test$i/$j/added$i.vcf > placementRun$i-$j.txt
	done
done