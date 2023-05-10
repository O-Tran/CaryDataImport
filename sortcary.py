#v1. 3.6.23 - > final  3.17.23
#adding additonal parser (direction to the .csv file)
import sys
import csv 
import numpy as np 
import pandas as pd 
import subprocess 

#main argument  
    #infile is the directory of the CSV Cary file 
"""
    Purpose: Sort CARY file to easy-to-undestand small file 
    1. converts raw files to organize dictionary *done*  
    2. prints out a rough picture of the wavelength absorbance *done* 
    3. Make a jupyternotebook with all the dictionary/ability to plots *in progress* 
    3. have capabilities to pick specific data I want to display via image/file (in a form of the list) on jupyter *progress*

    Usage:
    1.python sortcapy.py 
        - have the CSV file in the same folder 
    2. Insert the CSV file in the "infile"
     
    By: Oanh TN Tran
    Version: 1.1, started: february 24, 2022

------------------- DESCRIPTION --------------------------------------------------------------

    Get energy from input file. convert to Jupyter notebook with sorted dictionary and a printed file of graphed rough-combined absorbances. 
    
    Parameters
    ----------
    inputfile : str
        The directory of CSV. from CARY (poulos lab)
    
    outputfile: str
        The directory of Jupyternotebook with already Processed* and Sorted* data 
        The name of output file. Extension include: .ipynb, .txt, 

    Returns
    -------
    output file:
        outputfile: gives Dictionary, Jupyter notebook, and a rough wavelength absorbance of all the data in the specific directory 
"""

subprocess.run(["conda", "activate", "matplotlib"])
subprocess.run(["jupytext", "--to", "notebook", "sortcary.py"])
subprocess.run(["jupyter", "notebook", "sortcary.ipynb"])


#def makingtuple(infile):
#sort data (make Dict of list { Wavelength: [number, number, ... ]
                            # items : [number, number, ... ]...  }
nestedDatadict = {} 
i = 0
#convert data to numpy array  
with open (infile) as caryfile:
    data=[tuple(line) for line in csv.reader(caryfile)]
    numpdata = np.array(data[2:603])

    #convert numpy array to dictionary of list (of the values corresponding to specific wavelength)
    nestedDatadict["wavelength"] = list(float(numpdata[a,0]) for a in range(601))
    for items in data[0]:
        nestedDatadict[items] = list(float(numpdata[a,i+1]) for a in range(601))
        if i < len(data[0]) - 3 :
            i += 2 
        else:
            break

#sset dataset as a list of all the keys 
dataset= nestedDatadict.keys()
caryfile.close()

#make dictionary into data frame for graphing purposes 
data = pd.DataFrame(nestedDatadict)
outputdata = data.head() #make a dataframe chart 

#plotting rough absorbance of data 
dataplot = data.plot(x='wavelength', title = 'Rough absorption', 
                     ylim=(0,0.5), xlim=(250,700),
                     colormap = 'viridis', legend='reverse');
dataplot.set_ylabel('Absorbance')
dataplot.set_xlabel('Wavelength (nm)')
dataplot.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
fig = dataplot.get_figure()
fig.savefig('Roughplot.png', dpi=1000)


#new section for inputting data that you want 
import matplotlib.pyplot as plt 
#%matplotlib inline
datawant = ['fill in here', '', '', '', '', '']
#plt.figsize().set_figwidth() #or .set_figheight()
for items in datawant:
    plt.plot(nestedDatadict['wavelength'], nestedDatadict[items], label = items)
    #print (nestedDatadict[items])
plt.xlabel('Absorbance')
plt.ylabel('Wavelength (nm)')
plt.ylim([0,0.5])
plt.xlim([250,700])
plt.legend()
plt.savefig('matplotlibchosen.png', dpi=1000)
plt.show()

#if __name__ == "__main__":
#    nestedDatadict, dataset = makingtuple(sys.argv[1])
    
print ('Here are the datasets: ./n' + '%s' %dataset)

      

