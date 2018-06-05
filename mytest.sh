#!/bin/bash
task_id=$1
outdir=$2
#echo "task id is $task_id" > $outdir/out.$task_id
python3 ./python_files/compute.py ./data/split/exons_chicken.txt.part$task_id ./data/features/class1/exons_chicken.txt.features.part.$task_id
python3 ./python_files/compute.py ./data/split/promoters_500_chicken.txt.part$task_id ./data/features/class2/promoters_500_chicken.txt.features.part.$task_id


