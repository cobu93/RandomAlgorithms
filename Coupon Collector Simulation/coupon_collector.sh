#!/bin/bash

n_coupons=$1
n_repetitions=$2
evaluation_step=$3

declare expected_steps
declare real_steps
linear_factors=($(seq -3 1 7))
count_expected_steps=0

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

      # 5 steps, all factors, 10 steps. all factors and so on

      for factor in ${linear_factors[*]}
        do
        expected_steps[$count_expected_steps]=$(echo "$i*(l($i)+$factor)" | bc -l)
        real_steps[$count_expected_steps]=0
        count_expected_steps=$(($count_expected_steps + 1))
        done
      fi

    start_index=$((($i / $evaluation_step - 1) * ${#linear_factors[@]}))
    current_factor=0
    for factor in ${linear_factors[*]}
      do
        index=$(($start_index + $current_factor))
        var="expected_steps[$index]"
        if [ $(echo "$boxes < ${expected_steps[$index]}" | bc) -ne 0 ]
          then
            real_steps[$index]=$((${real_steps[start_index + current_factor]} + 1))
          fi
        current_factor=$(($current_factor + 1))
      done


    done    

    if [ $reps -eq 0 ]
      then
      echo "${!rep_boxes_history[*]}:"
      echo "${linear_factors[*]}:"
      fi

    echo "${rep_boxes_history[*]};"
  done

echo ":${real_steps[*]}"
