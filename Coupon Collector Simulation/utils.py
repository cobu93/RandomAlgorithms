from matplotlib import pyplot as plt

def plot_coupon_collector_results(coupons, mean, expected, std_dev=None):

  figure = plt.figure(dpi=160, facecolor='w', edgecolor='k')

  ax_num_coupons = figure.add_subplot(111)
    
  ax_num_coupons.set_title('E[boxes] = n log(n)')
  ax_num_coupons.set_xlabel('Number of coupons')
  ax_num_coupons.set_ylabel('Number of boxes')

  ax_num_coupons.plot(coupons, mean, 'g-', label='Experiment mean', linewidth=0.7)
  ax_num_coupons.plot(coupons, expected, 'r--', label='Expected result (n log(n))', linewidth=0.7)

  if std_dev is not None:
    ax_num_coupons.errorbar(coupons, mean, std_dev, label='Standard deviation', linestyle='None', capsize=2, linewidth=0.7)

  ax_num_coupons.legend(loc='upper left')


  return figure


def plot_coupon_collector_probability(factors, probabilities):

  figure = plt.figure(dpi=160, facecolor='w', edgecolor='k')

  ax_prob_coupons = figure.add_subplot(111)
    
  ax_prob_coupons.set_title('Pr(steps ≤ n log(n) + cn)')
  ax_prob_coupons.set_xlabel('Factor (c)')
  ax_prob_coupons.set_ylabel('Probability')


  for key in probabilities.keys():
    ax_prob_coupons.plot(factors, probabilities[key], label='coupons={}'.format(key), linewidth=0.7)

  return figure