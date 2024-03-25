#!/bin/bash

# numTest=5

# # for i in 5 10 50 100 200 500 1000 2000 5000 10000
# # for i in 5 10 50 100 200 500
# # for i in 2000 5000 10000
# for i in 5
# do
# 	if [ "$i" -gt 500 ] 
# 	then numTest=2
# 	else numTest=5
# 	fi

# 	for ((j = 1; j <= 1; j++)) do
# 	# for ((j = 1; j <= $numTest; j++)) do
# 		echo "test$i-$j"
# 		echo "" > usherRun$i-$j.txt
# 		echo "" > matRun$i-$j.txt
# 		# ./usher -t ../../data/test$i/$j/origin$i.fasta.treefile -v ../../data/test$i/$j/added$i.vcf -T 1 -u >> usherRun$i-$j.txt
#         # ./matOptimize -t uncondensed-final-tree.nh -v ../../data/test$i/$j/added$i.vcf -T 1 -r 8 -o optimize.pb >> matRun$i-$j.txt

# 		# ./../../anothermpboot/build/mpboot-avx -pp_on -pp_n $i -pp_k $i -s ../../data/test$i/$j/added$i.vcf -pp_tree ../../data/test$i/$j/origin$i.fasta.treefile -pp_origin ../../data/test$i/$j/origin$i.fasta.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure >> matRun$i-$j.txt
# 		# echo "=====================================================================matOptimize=====================================================" >> matRun$i-$j.txt
# 		# python fixnewick.py
# 		# ./matOptimize -t addedTree.txt -v ../../data/test$i/$j/added$i.vcf -T 1 -r 8 -o optimize.pb >> matRun$i-$j.txt

# 		./usher -t ../scripts/example.fasta.treefile -v ../scripts/example.vcf -T 1 -u >> usherRun$i-$j.txt
# 		./../../anothermpboot/build/mpboot-avx -pp_on -pp_n 5 -pp_k 5 -s ../scripts/example.vcf -pp_tree ../scripts/example.fasta.treefile -pp_origin ../scripts/example.fasta.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure >> matRun$i-$j.txt
# 		echo "=====================================================================matOptimize=====================================================" >> matRun$i-$j.txt
# 		# python fixnewick.py
# 		./matOptimize -t addedTree.txt -v ../scripts/example.vcf -T 1 -r 8 -o optimize.pb >> matRun$i-$j.txt
# 	done
# done

# for i in 9909 19767 42438 
for i in 9909
# for i in 19767
# for i in 42438
do
	# for ((j = 0; j <= 0; j++)) do
	for ((j = 0; j <= 99; j++)) do
		echo "test$i-$j"
		echo "" > usherRun$i-$j.txt
		echo "" > matRun$i-$j.txt
		./mpboot-avx -pp_on -pp_n $((i-10)) -pp_k 10 -s ../../newdata/test$i/global_$i.vcf -pp_tree ../../newdata/test$i/pruned_tree_$j.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure > Run$i-$j.txt
        ./usher -t ../../newdata/test$i/pruned_tree_$j.treefile -v ../../newdata/test$i/global_$i.vcf -T 1 -u >> usherRun$i-$j.txt
		./matOptimize -t addedTree.txt -v ../../newdata/test$i/global_$i.vcf -T 1 -r 8 -o optimize.pb >> matRun$i-$j.txt
	done
done 
