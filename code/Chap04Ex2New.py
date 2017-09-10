import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot


sample = np.random.random(1000)
hist = thinkstats2.Hist(sample)
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Random Nos.', ylabel='Frequency')

#Distribution is uniform with equal probability of occurance for each Random No.

pmf = thinkstats2.Pmf(sample)
thinkplot.Pmf(pmf,linewidth=0.1)
thinkplot.Show(xlabel='Random Nos.', ylabel='PMF')

#Distribution is uniform as cdf of the sample values is linear

sample_cdf = thinkstats2.Cdf(sample, label='Random Nos.')
thinkplot.Cdf(sample_cdf)
thinkplot.Show(xlabel='Random Nos.', ylabel='CDF')