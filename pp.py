import matplotlib.pyplot as plt
import numpy as np

qqprops = {
        's':1.5,
        'linewidth':0
}

umapprops = {
    'edgecolors':'none',
    's':2,
    'rasterized':True
}

def scatter_random(x, y, c=None, symmetrize=True, percentile=90, ax=None, seed=0, **kwargs):
    if ax is None:
        ax = plt.gca()
    if c is None:
        print('error: no color supplied')
        return
    kwargs.update(umapprops)
    
    ix = np.argsort(np.random.randn(len(x)))
    x = x[ix]
    y = y[ix]
    c = c[ix]
    
    if symmetrize:
        maxval = np.percentile(np.abs(c), percentile)
        kwargs.update({'vmin':-maxval, 'vmax':maxval})
    ax.scatter(x, y, c=c, **kwargs)