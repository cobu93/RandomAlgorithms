#!/bin/bash

n_coupons=$1
n_repetitions=$2
evaluation_step=$3

declare expected_steps
declare real_steps
linear_factors=($(seq -3 1 7))

for ((reps=0; reps<$n_repetitions; reps++))
  do  
  for ((i=$evaluation_step; i<$n_coupons + $evaluation_step - 1; i+=$evaluation_step))
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


    if [ $reps -eq 0 ]
      then

      for factor in $linear_factors
        do
        expected_steps[$i"_"$factor] = $(('$i*(l($count_step)+$factor)' | bc -l))
        real_steps[$i"_"$factor] = 0
        done
      fi

    for factor in $linear_factors
      do
        if [$boxes < ${expected_steps[i"_"factor]} ]
          then
            real_steps[$i"_"$factor] = $((${real_steps[i_factor]} + 1))
          fi
      done


    done    

    if [ $reps -eq 0 ]
      then
      echo "${!rep_boxes_history[*]}:"
      fi

    echo "${rep_boxes_history[*]};"
  done

echo ":${expected_steps[*]}"
echo ":${real_steps[*]}"
