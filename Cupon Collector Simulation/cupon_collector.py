import numpy as np
import math
from utils import plot_cupon_collector_results

n_cupons = 100
n_repetitions = 100
evaluation_step = 5

cupons_history = range(0, n_cupons, evaluation_step)

boxes_history = []

# Repeat the experiment n_repetitions times
for _ in range(n_repetitions):
  rep_boxes_history = []

  for cupons in cupons_history:
    # Represents the cupon's album
    exists = np.array([False] * cupons)
    
    # Opened boxes
    boxes = 0

    # While the album isn't complete
    while False in exists:
      # Open a box and get a cupon
      value = np.random.randint(0, cupons, size=1)
      # Add cupon to album
      exists[value] = True
      # Sum 1 to used boxes
      boxes += 1

    # Store used boxes for each experiment
    rep_boxes_history.append(boxes)

  # Appends used boxes for each number of cupons evaluated
  boxes_history.append(rep_boxes_history)

mean_history = np.mean(boxes_history, axis=0)
error_history = np.std(boxes_history, axis=0)
expected_history = [cupons * math.log(cupons + 1e-15) for cupons in cupons_history]

figure = plot_cupon_collector_results(
    cupons=cupons_history, 
    mean=mean_history, 
    expected=expected_history, 
    std_dev=error_history
)

figure.savefig('python_results.png')