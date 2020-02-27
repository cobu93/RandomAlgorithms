import numpy as np
from utils import plot_coupon_collector_results
import subprocess
import re
import math
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
result = subprocess.run(['./coupon_collector.sh', str(n_coupons), str(n_repetitions), str(evaluation_step)], stdout=subprocess.PIPE)
end = time.time()
print('Python script:[Coupons:{}][Experiments:{}][Step:{}][Time:{:.5f}]'.format(n_coupons, n_repetitions, evaluation_step, end - start))

values = result.stdout.decode('utf-8').split(':')

coupons_history = np.fromstring(values[0], dtype=int, sep=' ')
boxes_history = np.asarray(np.matrix(';'.join((values[1].split(';')[:-1]))))

mean_history = np.mean(boxes_history, axis=0)
error_history = np.squeeze(np.std(boxes_history, axis=0))
expected_history = [coupons * math.log(coupons + 1e-15) for coupons in coupons_history]

figure = plot_coupon_collector_results(
    coupons=coupons_history, 
    mean=mean_history, 
    expected=expected_history, 
    std_dev=error_history
)

figure.savefig('bash_results.png')