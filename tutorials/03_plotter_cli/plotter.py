import matplotlib.pylab as plt
# import ccrs for map projections
import cartopy.crs as ccrs
from netCDF4 import Dataset

import os
DATADIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data')
AIR_DS = os.path.join(DATADIR, 'air.mon.ltm.nc')


def simple_plot(resource, variable=None, output='plot.png'):
    """
    Generates a nice and simple plot.
    """
    print("Plotting {} ...".format(resource))

    # Create dataset from resource ... a local NetCDF file or a remote OpenDAP URL
    ds = Dataset(resource)

    # Get the values of the given variable
    values = ds.variables[variable]

    # Prepare plot with a given size
    fig = plt.figure(figsize=(20, 10))

    # add projection
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Render a contour plot for the first timestep
    plt.contourf(values[0, :, :])

    # add background image with coastlines
    ax.stock_img()
    ax.coastlines()

    # add a colorbar
    plt.colorbar()

    # Save the plot to filesystem
    fig.savefig(output)
    plt.close()
    print("Plot written to {}".format(output))
    return output


def test_simple_plot():
    # raise NotImplementedError("This test is not implemented yet. Help wanted!")

    # run default test
    output = simple_plot(resource=AIR_DS, variable='air')
    assert output == 'plot.png'

    # try an invalid variable
    try:
        simple_plot(resource=AIR_DS, variable='water')
    except KeyError:
        pass


if __name__ == '__main__':
    simple_plot(resource=AIR_DS, variable="air")
