
import nsfg
import thinkstats2
import thinkplot


def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

resp = nsfg.ReadFemResp()

actual_pmf=thinkstats2.Pmf(resp.numkdhh,label='Actual')
biased_pmf=BiasPmf(actual_pmf,label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show(xlabel='No. of children in a Household', ylabel='PMF')

print('Actual Mean: ',actual_pmf.Mean(),'\nBiased/Observed Mean: ', biased_pmf.Mean())
