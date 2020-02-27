from matplotlib import pyplot as plt

def plot_coupon_collector_results(coupons, mean, expected, std_dev=None):

  figure = plt.figure(dpi=160, facecolor='w', edgecolor='k')

  ax_num_coupons = figure.add_subplot(111)
    
  ax_num_coupons.set_title('Coupons collector')
  ax_num_coupons.set_xlabel('Number of coupons')
  ax_num_coupons.set_ylabel('Number of boxes')

  ax_num_coupons.plot(coupons, mean, 'g-', label='Experiment mean', linewidth=0.7)
  ax_num_coupons.plot(coupons, expected, 'r--', label='Expected result (n log(n))', linewidth=0.7)

  if std_dev is not None:
    ax_num_coupons.errorbar(coupons, mean, std_dev, label='Standard deviation', linestyle='None', capsize=2, linewidth=0.7)

  ax_num_coupons.legend(loc='upper left')


  return figure