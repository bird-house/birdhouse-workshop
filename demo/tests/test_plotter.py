import pytest
import tempfile

from demo.plotter import simple_plot


@pytest.mark.online
def test_simple_plot():
    output = simple_plot(
        'http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis/surface/air.sig995.2012.nc',
        variable='air',
        output=tempfile.mkstemp(prefix='simple_plot', suffix=".png")[1])
    assert '.png' in output
