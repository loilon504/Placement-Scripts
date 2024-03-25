#!/bin/bash

# numTest=5

# for i in 5 10 50 100 200 500 1000 2000 5000 10000
# #for i in 5 10 50 100 200 500
# # for i in 2000 5000 10000
# # for i in 10
# do
# 	if [ "$i" -gt 500 ] 
# 	then numTest=2
# 	else numTest=5
# 	fi

#     # for ((j = 1; j <= 1; j++)) do
# 	for ((j = 1; j <= $numTest; j++)) do
# 		echo "test$i-$j "
#         ./mpboot-avx -pp_on -pp_n $i -pp_k $i -s ../../data/test$i/$j/added$i.vcf -pp_tree ../../data/test$i/$j/origin$i.fasta.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure > placementRun$i-$j.txt
# 		# ./mpboot-avx -s ../../data/test$i/$j/added$i.vcf > placementRun$i-$j.txt
# 	done
# done


# for i in 9909 19767 42438 
for i in 9909
# for i in 19767
# for i in 42438
do
	for ((j = 0; j <= 0; j++)) do
	# for ((j = 0; j <= 99; j++)) do
		echo "test$i-$j"
		./mpboot-avx -pp_on -pp_n $((i-10)) -pp_k 10 -s ../../newdata/test$i/global_$i.vcf -pp_tree ../../newdata/test$i/pruned_tree_$j.treefile -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure > Run$i-$j.txt
		# ./mpboot-avx -pp_on -pp_n $((i-10)) -pp_k 10 -s ../../newdata/test$i/global_$i.vcf -pp_tree ../../newdata/test$i/pruned_tree_$j.newick -pp_opt_spr -spr_mintrav 8 -spr_maxtrav 8 -restructure > Run$i-$j.txt
	done
done 
