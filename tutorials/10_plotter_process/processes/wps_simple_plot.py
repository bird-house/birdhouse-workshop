
from pywps import Process, LiteralInput, ComplexInput, ComplexOutput
from pywps import Format

from plotter import simple_plot

import logging
LOGGER = logging.getLogger('PYWPS')

AIR_DS = 'https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc'


class SimplePlot(Process):
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'Dataset', supported_formats=[Format('application/x-netcdf')],
                         default=AIR_DS,
                         abstract='Example: {0}'.format(AIR_DS)),
            LiteralInput('variable', 'Variable', data_type='string',
                         default='air',
                         abstract='Enter the variable name.'),
        ]
        outputs = [
            ComplexOutput('output', 'Simple Plot', supported_formats=[Format('image/png')],
                          as_reference=True),
        ]

        super(SimplePlot, self).__init__(
            self._handler,
            identifier='simple_plot',
            title='Simple Plot',
            abstract='Returns a nice and simple plot.',
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        variable = request.inputs['variable'][0].data
        # Call simple_plot function
        output = simple_plot(
            resource=request.inputs['dataset'][0].file,
            variable=variable)
        LOGGER.info("produced output: %s", output)
        response.outputs['output'].file = output
        response.update_status("simple_plot done", 100)
        return response
