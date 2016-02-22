import numpy as np
import matplotlib as mpl
mpl.rc_file('/home/wwilliams/.config/matplotlib/matplotlibrc')  # <-- the file containing your settings
import matplotlib.pyplot as plt


def fig_save_many(f, name, types=[".png",".pdf"], dpi=200):
    for ext in types:
        f.savefig(name+ext, dpi=dpi)
    return

def paper_single(TW = 6.64, AR = 0.74, FF = 1.):
    '''paper_single(TW = 6.64, AR = 0.74, FF = 1.)
    TW = 3.32
    AR = 0.74
    FF = 1.
    #mpl.rc('figure', figsize=(4.5,3.34), dpi=200)
    mpl.rc('figure', figsize=(FF*TW, FF*TW*AR), dpi=200)
    mpl.rc('figure.subplot', left=0.18, right=0.97, bottom=0.18, top=0.9)
    mpl.rc('lines', linewidth=1.0, markersize=4.0)
    mpl.rc('font', size=9.0, family="serif", serif="CM")
    mpl.rc('xtick', labelsize='small')
    mpl.rc('ytick', labelsize='small')
    mpl.rc('axes', linewidth=0.75)
    mpl.rc('legend', fontsize='small', numpoints=1, labelspacing=0.4, frameon=False) 
    mpl.rc('text', usetex=True) 
    mpl.rc('savefig', dpi=300)
    '''
    #import matplotlib as mpl
    # textwidht = 42pc = 42 * 12 pt = 42 * 12 * 1/72.27 inches
    # columnsep = 2pc
    # ... colwidth = 20pc
    
    #mpl.rc('figure', figsize=(4.5,3.34), dpi=200)
    mpl.rc('figure', figsize=(FF*TW, FF*TW*AR), dpi=100)
    mpl.rc('figure.subplot', left=0.15, right=0.95, bottom=0.15, top=0.92)
    mpl.rc('lines', linewidth=1.75, markersize=8.0, markeredgewidth=0.75)
    mpl.rc('font', size=18.0, family="serif", serif="CM")
    mpl.rc('xtick', labelsize='small')
    mpl.rc('ytick', labelsize='small')
    mpl.rc('xtick.major', width=1.0, size=8)
    mpl.rc('ytick.major', width=1.0, size=8)
    mpl.rc('xtick.minor', width=1.0, size=4)
    mpl.rc('ytick.minor', width=1.0, size=4)
    mpl.rc('axes', linewidth=1.5)
    mpl.rc('legend', fontsize='small', numpoints=1, labelspacing=0.4, frameon=False) 
    mpl.rc('text', usetex=True) 
    mpl.rc('savefig', dpi=300)
    
    
    
def paper_single_mult_ax(nrows=1, ncols=1, **kwargs):
    #import matplotlib as mpl
    paper_single(FF=max(nrows,ncols))
    f, ax = plt.subplots(nrows=nrows, ncols=ncols, **kwargs)
    plt.minorticks_on()
    ylocator6 = plt.MaxNLocator(5)
    xlocator6 = plt.MaxNLocator(6)
    if len(ax.shape) > 1:
        for axrow in ax:
            for axcol in axrow:
                axcol.xaxis.set_major_locator(xlocator6)
                axcol.yaxis.set_major_locator(ylocator6)
    else:
        for axcol in ax:
            axcol.xaxis.set_major_locator(xlocator6)
            axcol.yaxis.set_major_locator(ylocator6)
    return f, ax
    
    
def paper_single_ax(TW = 6.64, AR = 0.74, FF = 1.):
    #import matplotlib as mpl
    paper_single(TW=TW, AR=AR, FF=FF)
    f = plt.figure()
    ax = plt.subplot(111)
    plt.minorticks_on()
    ylocator6 = plt.MaxNLocator(5)
    xlocator6 = plt.MaxNLocator(6)
    ax.xaxis.set_major_locator(xlocator6)
    ax.yaxis.set_major_locator(ylocator6)
    return f, ax

def paper_double_ax():
    #import matplotlib as mpl
    paper_single(TW = 12)
    f = plt.figure()
    ax = plt.subplot(111)
    plt.minorticks_on()
    ylocator6 = plt.MaxNLocator(5)
    xlocator6 = plt.MaxNLocator(6)
    ax.xaxis.set_major_locator(xlocator6)
    ax.yaxis.set_major_locator(ylocator6)
    return f, ax

def paper_double_mult_ax(nrows=1, ncols=1, setticks=True, **kwargs):
    #import matplotlib as mpl
    paper_single()
    #TW = 6.97
    #AR = 0.74
    #FF = 1.
    #mpl.rc('figure', figsize=(FF*TW, FF*TW*AR), dpi=200)
    #mpl.rc('figure.subplot', left=0.08, right=0.95, bottom=0.08, top=0.95)
    #mpl.rc('font', size=12.0, family="serif", serif="CM")
    #f = plt.figure()
    #ax = plt.subplot(111)
    #plt.minorticks_on()
    #ylocator6 = plt.MaxNLocator(7)
    #xlocator6 = plt.MaxNLocator(8)
    #ax.xaxis.set_major_locator(xlocator6)
    #ax.yaxis.set_major_locator(ylocator6)
    
    
    TW = 6.97*2
    AR = 0.74
    FF = 1.
    mpl.rc('figure', figsize=(FF*TW, FF*TW*AR), dpi=200)
    mpl.rc('figure.subplot', left=0.1, right=0.97, bottom=0.1, top=0.97)
    mpl.rc('font', size=24.0, family="serif", serif="CM")
    
    f, ax = plt.subplots(nrows=nrows, ncols=ncols, **kwargs)
    plt.minorticks_on()
    if setticks:
        ylocator6 = plt.MaxNLocator(5)
        xlocator6 = plt.MaxNLocator(6)
        if len(ax.shape) > 1:
            for axrow in ax:
                for axcol in axrow:
                    axcol.xaxis.set_major_locator(xlocator6)
                    axcol.yaxis.set_major_locator(ylocator6)
        else:
            for axcol in ax:
                axcol.xaxis.set_major_locator(xlocator6)
                axcol.yaxis.set_major_locator(ylocator6)
    return f, ax



def donley_mask(f_ch1, f_ch2, f_ch3, f_ch4, mags=True):
    '''Select sources using the Donley+ 2012 criteria
    returns  - array 1 where source in stern wedge, 0 where outside and -1 where any mag is nan
    '''
    
    if mags:
        f_ch1 = -2.5*np.log(f_ch1)
        f_ch2 = -2.5*np.log(f_ch2)
        f_ch3 = -2.5*np.log(f_ch3)
        f_ch4 = -2.5*np.log(f_ch4)
    
    x = np.log10(f_ch3/f_ch1)
    y = np.log10(f_ch4/f_ch2)
    
    s1 = (x >= 0.08)
    s2 = (y >= 0.15)
    s3 = (y >= 1.21*x - 0.27)
    s4 = (y <= 1.21*x + 0.27)
    s5 = (f_ch2 > f_ch1)
    s6 = (f_ch3 > f_ch2)
    s7 = (f_ch4 > f_ch3)
    nan1 = np.isnan(f_ch1)
    nan2 = np.isnan(f_ch2)
    nan3 = np.isnan(f_ch3)
    nan4 = np.isnan(f_ch4)
    nanmask = nan1 & nan2 & nan3 & nan4
    donleymask = s1 & s2 & s3 & s4 & s5 & s6 & s7 
    #maskind = np.where(mask)[0]
    donleymask[nanmask] = np.nan
    return donleymask

def stern_mask(m_ch1, m_ch2, m_ch3, m_ch4):
    '''Select sources in the Stern wedge
    returns  - array 1 where source in stern wedge, 0 where outside and -1 where any mag is nan
    '''
    s1 = ( (m_ch3 - m_ch4) > 0.6 )
    s2 = ( (m_ch1 - m_ch2) > 0.2*(m_ch3 - m_ch4) +0.18 )
    s3 = ( (m_ch1 - m_ch2) > 2.5*(m_ch3 - m_ch4) - 3.5 )
    nan1 = np.isnan(m_ch1)
    nan2 = np.isnan(m_ch2)
    nan3 = np.isnan(m_ch3)
    nan4 = np.isnan(m_ch4)
    nanmask = nan1 & nan2 & nan3 & nan4
    sternmask = s1 & s2 & s3
    #maskind = np.where(mask)[0]
    sternmask[nanmask] = np.nan
    return sternmask

def plot_stern_wedge(ax):
    # Stern+ 2005
    # [5.8]-[8.0] > 0.6 U [3.6]-[4.6] > 0.2([5.8]-[8.0]) +0.18 U ([3.6]-[4.5]) > 2.5([5.8]-[8.0]) - 3.5
    # intercepts (0.6, ymax) (0.6, 0.3) (1.6,0.5) (xmax, 2.5*xmax-3.5)  [0.6, -2.0]

    xmin,xmax = ax.get_xlim()
    ymin,ymax = ax.get_ylim()
    yd = 2.5*xmax -3.5
    if yd > ymax:
        xd = xmax
    else:
        xd = (ymax + 3.5)/2.5
        yd = ymax 
    ax.plot([0.6, 0.6, 1.6, xd], [ymax, 0.3, 0.5, yd], 'k')
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    return

def MIR_flux_to_mag(f1,f2,f3,f4,zp=25.):
    ## Vega mags  : add the extra (to go from AB to vega)
    ## 
    #m1 = -2.5*np.log10(f1) + 23.9 -2.788
    #m2 = -2.5*np.log10(f2) + 23.9 -3.255
    #m3 = -2.5*np.log10(f3) + 23.9 -3.743
    #m4 = -2.5*np.log10(f4) + 23.9 -4.372
    
    m1 = -2.5*np.log10(f1) + zp -2.788
    m2 = -2.5*np.log10(f2) + zp -3.255
    m3 = -2.5*np.log10(f3) + zp -3.743
    m4 = -2.5*np.log10(f4) + zp -4.372
    return [m1,m2,m3,m4]


def MIR_AGN(m1,m2,m3,m4, mode='flux'):
    if mode == 'flux':
        ## Vega mags  : add the extra
        m1,m2,m3,m4 = MIR_flux_to_mag(m1,m2,m3,m4)
    agn_mask = stern_mask(m1, m2, m3, m4)
    return agn_mask

def plot_mir_colours(m1,m2,m3,m4, ax=None, spec_ind=None, col=None, vmin=None, vmax=None):
    
    if ax is None:
        f, ax = paper_single_ax()
    
    ax.minorticks_on()
    
    A = 0.5
    if len(m1) > 1000:
        A = 0.1
    elif len(m1) > 10000:
        A = 0.01
        
    if col is None:
        ax.plot(m3 -m4,  m1-m2, 'k.', alpha=A)
    else:
        if vmin is None:
            vmin = min(col)
        if vmax is None:
            vmax = max(col)
        c=ax.scatter(m3 -m4,  m1-m2, c=col, marker='o', edgecolor='none', vmin=vmin, vmax=vmax)
        try: plt.colorbar(c)
        except: print "error"
    
    if spec_ind is not None:
        if col is None:
            ax.plot((m3-m4)[spec_ind],  (m1-m2)[spec_ind], 'rx', alpha=A)
        else:
            ax.plot((m3-m4)[spec_ind],  (m1-m2)[spec_ind], 'rx', alpha=A)
        
    
    plot_stern_wedge(ax)
    
    ax.set_xlabel('[5.8] - [8.0]')
    ax.set_ylabel('[3.6] - [4.5]')
    
    #ax.set_xlim(-5,5)
    #ax.set_ylim(-0.4, 1.2)
    
    #plt.savefig(savename)
    
    return f,ax


def hist2d(ax, xdat, ydat, xyrange, bins, thresh=2, cmap=plt.cm.Greys, log=False, scatterother=False):
    import scipy

    tt = ax.get_aspect()

    # histogram the data
    hh, locx, locy = scipy.histogram2d(xdat, ydat, range=xyrange, bins=bins)
    mhh = np.mean(hh)
    shh = np.std(hh)
    if log:
        lhh = np.log10(hh)
    else:
        lhh = hh
    posx = np.digitize(xdat, locx)
    posy = np.digitize(ydat, locy)


    #select points within the histogram
    ind = (posx > 0) & (posx <= bins[0]) & (posy > 0) & (posy <= bins[1])
    hhsub = hh[posx[ind] - 1, posy[ind] - 1] # values of the histogram where the points are
    xdat1 = xdat[ind][hhsub < thresh] # low density points
    ydat1 = ydat[ind][hhsub < thresh]
    lhh[hh  < thresh] = np.nan # fill the areas with low density by NaNs

    ar = (0.6/0.65)*(np.diff(xyrange[0])/np.diff(xyrange[1]))[0]
    c = ax.imshow(np.flipud(lhh.T),extent=np.array(xyrange).flatten(), interpolation='none', cmap=cmap, aspect=ar)  
    
    ax.set_aspect(tt)
    
    if scatterother:
        ax.plot(xdat1, ydat1, 'k,')    
    
    
    return c


def make_ax3():
    paper_single(TW=9, AR=0.9)
    f = plt.figure()
    
    from matplotlib.ticker import NullFormatter, MaxNLocator

    nullfmt   = NullFormatter()         # no labels

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.6
    bottom_h = bottom+height+0.02
    left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    ax = plt.axes(rect_scatter)
    plt.minorticks_on()
    axx = plt.axes(rect_histx)
    plt.minorticks_on()
    axy = plt.axes(rect_histy)
    plt.minorticks_on()

    # no labels
    axx.xaxis.set_major_formatter(nullfmt)
    axy.yaxis.set_major_formatter(nullfmt)
    
    
    axy.xaxis.set_major_locator(MaxNLocator(4))
    axx.yaxis.set_major_locator(MaxNLocator(4))
    
    return f,ax,axx,axy



def nanhist(x,**kwargs):
    
    n,b,p = plt.hist(x[np.isfinite(x)],**kwargs)
    return n,b,p

#xmin,xmax = ax.get_xlim()
#ymin,ymax = ax.get_ylim()
#ax.plot([0.6, 0.6, 1.6, xmax], [ymax, 0.3, 0.5, 2.5*xmax -3.5], 'k')


markers=['o','s','D','p','H','v','^','<','>','1','2','3','4','h']
mylinestyles = ['-', '--','-.', ':' ]
mylinestyles = ['-', '-','-', '-' ,'-','-','-']

#sample_colours = ['#ff0000', '#ff0e00', '#ff1b00', '#ff2900', '#ff3700', '#ff4500', '#ff5200', '#ff6000', '#ff6e00', '#ff7c00', '#ff8a00', '#ff9700' ', ''#ffa500']
#sample_colours = ['#ff0000', '#ff5200', '#ffa500']
sample_colours = ['#fecc5c','#fd8d3c', '#e31a1c','darkred']
sample_markers = ['s', '^', 'o']
sample_colours = ['#fecc5c','#fd8d3c', '#e31a1c','darkred']

def sample_color_range(Ncol):
    return plt.cm.YlOrRd(np.linspace(0, 1, Ncol))
sample_markers = ['s', '^', 'o','D','d','h']


pcut_colours = ['#e31a1c', '#fd8d3c', '#fecc5c']

#massbin_colours = ['#eaad15', '#bfbb40', '#95ca6a', '#6ada95', '#40e8bf','#15f7ea']
#massbin_colours = [ '#6ada95','#95ca6a', '#bfbb40', '#eaad15']
#massbin_colours = [ '#6ada95','#95ca6a', '#eaad15']
#massbin_colours = [ '#6ada95','#eaad15', '#eaad15']
#massbin_colours = ['#5ab4ac','#d8b365']
# http://colorbrewer2.org/
massbin_colours = ['#018571','#80cdc1','#dfc27d','#a6611a']
massbin_markers = ['s', '^','o','D']
#massbin_colours = [ '#6ada95', '#eaad15']
 
#massbin_colours = ['#005d61','#006155','#005d61','#004d61','#004561']
#massbin_colours = ['#005d61','#00614d','#006155','#00615d','#005d61','#005561','#004d61','#004561']

