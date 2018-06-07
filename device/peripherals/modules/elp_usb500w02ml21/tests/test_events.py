# Import standard python libraries
import sys, os, json

# Import module...
try:
    # ... if running tests from project root
    sys.path.append(".")
    from device.peripherals.modules.elp_usb500w02ml21.manager import ELPUSB500W02ML21
except:
    # ... if running tests from same dir as manger.py
    os.chdir("../../../../")
    from device.peripherals.modules.elp_usb500w02ml21.manager import ELPUSB500W02ML21

# Import device utilities
from device.utilities.modes import Modes
from device.utilities.accessors import get_peripheral_config
    
# Import shared memory
from device.state import State

# Import test config
device_config = json.load(open("device/peripherals/modules/elp_usb500w02ml21/tests/config.json"))
peripheral_config = get_peripheral_config(device_config["peripherals"], "Camera-1")

# Initialize state
state = State()


def test_init():
    manager = ELPUSB500W02ML21(
        name = "Test",
        state = state,
        config = peripheral_config,
        simulate = True,
    )