#!/usr/bin/env python 
"""
fit a beta distribution with several parameterizations
"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

## declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10,6))
splot = 0

## loop through parameterizations of the beta
for a,b in [(1,5),(0.75,0.75),(5,1)]:
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    rv = scs.beta(a,b)
    r = scs.beta.rvs(a,b,size=1000)
    pdf_range = np.linspace(scs.expon.ppf(0.01),scs.expon.ppf(0.99), 100)

    ax.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,normed=1,histtype='stepfilled')
    ax.plot(pdf_range, rv.pdf(pdf_range), '#FF0099', lw=5, label='frozen pdf')
    ax.set_xlim((0,1))
    ax.set_title("a=%s, b=%s"%(a,b))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    
plt.show()
