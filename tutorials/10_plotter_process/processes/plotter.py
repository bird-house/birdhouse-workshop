import matplotlib
# no X11 server ... must be run first
# https://github.com/matplotlib/matplotlib/issues/3466/
matplotlib.use('Agg')

import matplotlib.pylab as plt
# import ccrs for map projections
import cartopy.crs as ccrs
from netCDF4 import Dataset

import os
DATADIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..', 'data')
AIR_DS = os.path.join(DATADIR, 'air.mon.ltm.nc')


def simple_plot(resource, variable=None, projection=None, output='plot.png'):
    """
    Generates a nice and simple plot.
    """
    print("Plotting {} ...".format(resource))
    projection = projection or ccrs.PlateCarree()
    print("Using map projection {}".format(projection))

    # Create dataset from resource ... a local NetCDF file or a remote OpenDAP URL
    ds = Dataset(resource)

    # Get the values of the given variable
    values = ds.variables[variable]

    # Prepare plot with a given size
    fig = plt.figure(figsize=(20, 10))

    # add projection
    ax = plt.axes(projection=projection)

    # Render a contour plot for the first timestep
    plt.contourf(values[0, :, :])

    # add background image with coastlines
    ax.stock_img()
    # ax.set_global()
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
    import argparse

    parser = argparse.ArgumentParser(description='Generates a nice and simple plot from a NetCDF file.')
    parser.add_argument('dataset', nargs=1, default=AIR_DS,
                        help='a NetCDF file or an OpenDAP URL')
    parser.add_argument('-V', '--variable', nargs='?', default='air',
                        help='variable to plot (default: air)')
    parser.add_argument('-p', '--projection', nargs='?', default='PlateCarree',
                        choices=['PlateCarree', 'Mollweide', 'Robinson'],
                        help='map projection (default: PlateCarree)')

    args = parser.parse_args()
    print("dataset={0.dataset}, variable={0.variable}".format(args))
    # output = simple_plot(resource=args.dataset[0], variable=args.variable)
    output = simple_plot(resource=args.dataset[0], variable=args.variable,
                         projection=getattr(ccrs, args.projection)())
    print("Output: {}".format(output))
