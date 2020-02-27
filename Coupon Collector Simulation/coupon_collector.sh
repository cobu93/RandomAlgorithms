#!/bin/bash

n_coupons=$1
n_repetitions=$2
evaluation_step=$3

declare -A boxes_history

for ((reps=0; reps<$n_repetitions; reps++))
  do

  for ((i=0; i<$n_coupons + $evaluation_step - 1; i+=$evaluation_step))
    do

    declare rep_boxes_history
    let boxes=0

    exists=($(seq 1 1 $i))

    let sum_exists=${#exists[@]}

    while [ $sum_exists -gt 0 ]
      do

      if [ $sum_exists -gt 0 ]
        then
        let value=$((RANDOM % ($i + 1)))
        exists[$(($value - 1))]=0
        boxes=$(($boxes + 1))
        fi

      sum_exists=0
      for item in ${exists[*]}
        do
        sum_exists=$(($item + $sum_exists))
        done

      done

    rep_boxes_history[$i]=$boxes
    done    

    if [ $reps -eq 0 ]
      then
      echo "${!rep_boxes_history[*]}:"
      fi

    echo "${rep_boxes_history[*]};"
  done
