# -*- coding: utf-8 -*-
#
# This file is part of the ChaosGenerator project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" ChaosGenerator

"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(ChaosGenerator.additionnal_import) ENABLED START #
import random
# PROTECTED REGION END #    //  ChaosGenerator.additionnal_import

__all__ = ["ChaosGenerator", "main"]


class ChaosGenerator(Device):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(ChaosGenerator.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  ChaosGenerator.class_variable

    # ----------
    # Attributes
    # ----------

    RandomAttr = attribute(
        dtype='double',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        self.set_change_event("RandomAttr", True, False)
        # PROTECTED REGION ID(ChaosGenerator.init_device) ENABLED START #
        # PROTECTED REGION END #    //  ChaosGenerator.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(ChaosGenerator.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  ChaosGenerator.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(ChaosGenerator.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  ChaosGenerator.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_RandomAttr(self):
        # PROTECTED REGION ID(ChaosGenerator.RandomAttr_read) ENABLED START #
        self.RandomAttr = random.random() * 100
        return self.RandomAttr
        # PROTECTED REGION END #    //  ChaosGenerator.RandomAttr_read


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(ChaosGenerator.main) ENABLED START #
    return run((ChaosGenerator,), args=args, **kwargs)
    # PROTECTED REGION END #    //  ChaosGenerator.main

if __name__ == '__main__':
    main()
