#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N TEST_BERESFORD
#$ -cwd
#$ -o test_beresford.log
#$ -j y
#$ -t 1-10:1

./mytest.sh $SGE_TASK_ID pointless
