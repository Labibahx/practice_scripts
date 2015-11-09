### a collection of python scripts to proctice some astro-related stuff using the NLS1 data file.


##to start ipython shell, type: ipython --pylab

# importing packages

import numpy as np

from astropy.table import Table

from astropy.io import fits



### read a fits table and make plots

data= Table.read('/Users/tammour/scripts4mark/NLS1-Data.fits') #Read FITS data file. "Users/tammour/scripts4mark" is the path to the directory (folder) where the file is save to the one where your data file is saved

data.colnames #prints the names of the columns in table "data"


##scatter plot

fig= figure() #figure object

scatter(data['EW44344684'], data['EW5007tot'], marker= 'o', s= 16, edgecolor='red', facecolor='white') # scatter plot with some plotting options: marker shape, size, and color...

#scatter(log10(data['EW44344684']), log10(data['EW5007tot']), marker= 'o', s= 10, edgecolor='r', facecolor='w') # this now plots the log10 for each of x and y

xlabel(r'EW(Fe II$\lambda 4570$) ($\AA$)') #x-axis label. The $$ allows using Latex syntax for math symbols... this is not important now.
ylabel(r'EW ([O III]$\lambda 5007$) ($\AA$)')

xlim(-50, 140) #x-axis limit. this will be set automatically if you did not specify it
ylim(-5, 300) # those limits will need to be chaged if you plot the log10 values

fig.savefig('fevso3.pdf') #save the figure as pdf file. could be in other formats such as eps, png and jpeg...

##histogram

fig= figure()

hist(data['LBOL']/data['L_EDD'], histtype= 'step', lw=2, color='navy') #histogram for the Lbol/LEdd ratoi -note how we calculated the value within the plotting.
#you can do the calculation separately, e.g.,
#l= data['LBOL']/data['L_EDD']
#hist(l, histtype= 'step', lw=2, color='maroon') #lw is the line width

fig= figure()
hist(data['EW5007tot'][data['lHbetaw'] >2000], histtype='stepfilled', bins= 20, lw=2, color='grey', alpha= 0.5, label= r'FWHM(H$\beta$) > 2000 km/s')

hist(data['EW5007tot'][data['lHbetaw'] <2000], histtype='step', bins= 20, lw=2, color='purple', label= r'FWHM(H$\beta$) < 2000 km/s')

#histogram with 20 bins.
#note the synatx here: data['EW5007tot'] plots all values in the column
# data['EW5007tot'][data['lHbetaw'] >2000] selects the ones that matches the condition data['lHbetaw'] >2000 

xlabel(r'EW ([O III]$\lambda5007$')
ylabel('Normalized Num')

legend()

########
########

"""
read data file, do some calculations, and save results in a table.
Example: perforem the KS test to compare NLS1 vs. BLS1 samples and save results in a table
see ref here
http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.ks_2samp.html
"""


from astropy.table import Table

from scipy.stats import ks_2samp

data= Table.read("NLS1")

## test if the distributions of FeII (given with the R4570 ratio) for the NLS1 and BLS1 samples are similar

ks1= ks_2samp(data['R4570'][data['lHbetaw'] >2000], data['R4570'][data['lHbetaw'] < 2000])

# try to type ks1. ks1 has two numbers: the KS statistic and the p value

# Now we want to repeat the test on other quantities (other than the R4570) to see if NLS1s and BLS1s are drawn from the same distribution or not. We can then save the results in a table

cols= ['L5100', 'EW5007tot', 'EWHbetatot', 'L5007tot', 'Lhbetatot', 'R4570', 'R5007']

out= open('ks_test.dat', 'wr') # open a file to write results -the 'wr' option is to allow us t oread and write
out.write("param \t KS \t p-value \n") #wite a header

for c in cols: # for through the columns and calculate the KS test for each parameter
    ks= ks_2samp(data[c][data['lHbetaw'] >2000], data[c][data['lHbetaw'] < 2000])
    out.write(c+"\t"+"{:4.5f}".format(ks[0])+"\t"+"{:4.5e}".format(ks[1])+"\n") #format the numbers

out.close() #close the file. this is important because if you did not close the file it will stay open.

### try to include an extra condition for the R4570 to do the calculations only when the ReII is detected. The data file has a column with a flag "FeII_DETECT" when it is set to 0 we detect FeII.

################
# next try to repeat the calculations using the Anderson-Darling test. This is the one I want to use in the paper to replace the KS test.
#http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson_ksamp.html

