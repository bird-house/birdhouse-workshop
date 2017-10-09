from .wps_sayhello import SayHello
# import SimplePlot process class
from .wps_simple_plot import SimplePlot

processes = [
    SayHello(),
    # add SimplePlot process instance
    SimplePlot(),
]
