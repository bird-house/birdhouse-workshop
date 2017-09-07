import matplotlib.pylab as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset


def simple_plot(resource, variable=None, output=None):
    output = output or 'plot.png'
    ds = Dataset(resource)
    values = ds.variables[variable]
    fig = plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.contourf(values[0, :, :])
    ax.stock_img()
    ax.coastlines()
    plt.colorbar()
    fig.savefig(output)
    plt.close()
    return output
