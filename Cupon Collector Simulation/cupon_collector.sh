#!/bin/bash

n_cupons=100
n_repetitions=1
evaluation_step=5

declare -A boxes_history

for ((reps=0; reps<$n_repetitions; reps++))
  do

  declare -A rep_boxes_history
  
  for ((i=1; i<$n_cupons; i+=$evaluation_step))
    do


    exists=($(seq 0 1 $i))
    let boxes=0

    let sum_exists=1

    while [ $sum_exists -gt 0 ]
      do

      sum_exists=0

      for item in ${exists[*]}
        do
        sum_exists=$(($item + $sum_exists))
        done

      if [ $sum_exists -gt 0 ]
        then
        let value=$((RANDOM % ($i + 1)))
        exists[$value]=0
        boxes=$(($boxes + 1))
        fi
      done

      rep_boxes_history[$i]=$boxes
      echo "Boxes ${rep_boxes_history[*]}"

    done    
    boxes_history[$reps]=$rep_boxes_history 
  done


  echo "Boxes ${boxes_history[*]}"