from matplotlib import pyplot as plt

def plot_cupon_collector_results(cupons, mean, expected, std_dev=None):

  figure = plt.figure(dpi=160, facecolor='w', edgecolor='k')

  ax_num_cupons = figure.add_subplot(111)
    
  ax_num_cupons.set_title('Cupons collector')
  ax_num_cupons.set_xlabel('Number of cupons')
  ax_num_cupons.set_ylabel('Number of boxes')

  ax_num_cupons.plot(cupons, mean, 'g-', label='Experiment mean', linewidth=0.7)
  ax_num_cupons.plot(cupons, expected, 'r--', label='Expected result (n log(n))', linewidth=0.7)

  if std_dev is not None:
    ax_num_cupons.errorbar(cupons, mean, std_dev, label='Standard deviation', linestyle='None', capsize=2, linewidth=0.7)

  ax_num_cupons.legend(loc='upper left')


  return figure