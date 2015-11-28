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

###########################

"""Reading and writing files (tables).
    script to read a data table, do some calculations using some of the columns and writing the results in a new table
    """
data= Table.read('')


