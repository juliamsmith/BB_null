#!/bin/bash
cd to_run
for f in *.sh; do
    sbatch "$f" 
done
