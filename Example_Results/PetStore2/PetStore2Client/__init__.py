"""PetStore2Client package."""

import logging

from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from .client import PetStore2Client
from .modules import Pet, Store, User

LIBRARIES = ["Pet", "Store", "User"]

RFW = BuiltIn()
try:
    for name in LIBRARIES:
        RFW.import_library("PetStore2Client." + name)
except RobotNotRunningError:
    pass

# initialize logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
