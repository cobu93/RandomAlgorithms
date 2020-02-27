import numpy as np
import math
from utils import plot_coupon_collector_results
import time
import argparse

parser = argparse.ArgumentParser(description='Coupon collector\'s problem simulation in python')
parser.add_argument('coupons', type=int, help='Max number of coupons to be tested')
parser.add_argument('repetitions', type=int, help='Number of test repetitions')
parser.add_argument('step', nargs='?', type=int, default=5, help='Step between coupons test')
try:
  args = parser.parse_args()
except SystemExit:
  parser.print_help()
  raise



n_coupons = args.coupons
n_repetitions = args.repetitions
evaluation_step = args.step

start = time.time()

coupons_history = range(0, n_coupons + evaluation_step - 1, evaluation_step)

boxes_history = []

# Repeat the experiment n_repetitions times
for _ in range(n_repetitions):
  rep_boxes_history = []

  for coupons in coupons_history:
    # Represents the coupon's album
    exists = np.array([False] * coupons)
    
    # Opened boxes
    boxes = 0

    # While the album isn't complete
    while False in exists:
      # Open a box and get a coupon
      value = np.random.randint(0, coupons, size=1)
      # Add coupon to album
      exists[value] = True
      # Sum 1 to used boxes
      boxes += 1

    # Store used boxes for each experiment
    rep_boxes_history.append(boxes)

  # Appends used boxes for each number of coupons evaluated
  boxes_history.append(rep_boxes_history)


end = time.time()

print('Python script:[Coupons:{}][Experiments:{}][Step:{}][Time:{:.5f}]'.format(n_coupons, n_repetitions, evaluation_step, end - start))


mean_history = np.mean(boxes_history, axis=0)
error_history = np.std(boxes_history, axis=0)
expected_history = [coupons * math.log(coupons + 1e-15) for coupons in coupons_history]

figure = plot_coupon_collector_results(
    coupons=coupons_history, 
    mean=mean_history, 
    expected=expected_history, 
    std_dev=error_history
)

figure.savefig('python_results.png')