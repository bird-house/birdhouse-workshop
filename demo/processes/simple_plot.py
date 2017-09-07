
from pywps import Process, LiteralInput, ComplexInput, ComplexOutput
from pywps import Format

from demo.plotter import simple_plot

import logging
LOGGER = logging.getLogger('PYWPS')


class SimplePlot(Process):
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'Dataset', supported_formats=[Format('application/x-netcdf')]),
            LiteralInput('variable', 'Variable', data_type='string',
                         min_occurs=0),
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
        if 'variable' in request.inputs:
            variable = request.inputs['variable'][0].data
        else:
            variable = None
        LOGGER.info('collected inputs')
        output = simple_plot(
            resource=request.inputs['dataset'][0].file,
            variable=variable)
        LOGGER.info("produces output: %s", output)
        response.outputs['output'].file = output
        response.update_status("simple_plot done", 100)
        return response
