# -*- coding: utf-8 -*-
#
# This file is part of the EventReceiver project
#
# Matteo Canzari
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" EventReceiver

EventReceiver Training Example
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
# PROTECTED REGION ID(EventReceiver.additionnal_import) ENABLED START #
from tango import DeviceProxy
import sys
# PROTECTED REGION END #    //  EventReceiver.additionnal_import

__all__ = ["EventReceiver", "main"]


class EventReceiver(Device):
    """
    EventReceiver Training Example
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(EventReceiver.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  EventReceiver.class_variable

    # ----------
    # Attributes
    # ----------

    EventReceived = attribute(
        dtype='bool',
    )

    TestSpectrumType = attribute(
        dtype=('uint16',),
        max_dim_x=200,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(EventReceiver.init_device) ENABLED START #
        try:
            self.dev1 = DeviceProxy("test/chaos/1")
            self.dev1.subscribe_event("RandomAttr", PyTango.EventType.CHANGE_EVENT, self.HandleEvent2, stateless=True)
        except:
            print ("Unexpected error on DeviceProxy creation:", sys.exc_info()[0])

        # PROTECTED REGION END #    //  EventReceiver.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(EventReceiver.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  EventReceiver.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(EventReceiver.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  EventReceiver.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_EventReceived(self):
        # PROTECTED REGION ID(EventReceiver.EventReceived_read) ENABLED START #
        try:
            return self.attr_EventReceived
        except: 
            print ("Unexpected error on (self.attr_EventReceived = False):", sys.exc_info()[0])
        # PROTECTED REGION END #    //  EventReceiver.EventReceived_read

    def read_TestSpectrumType(self):
        # PROTECTED REGION ID(EventReceiver.TestSpectrumType_read) ENABLED START #
        self.TestSpectrumType=[1,2,3]
        return self.TestSpectrumType
        # PROTECTED REGION END #    //  EventReceiver.TestSpectrumType_read


    # --------
    # Commands
    # --------

    def HandleEvent (self, args):
        try:
            print("Event arrived")
            self.attr_EventReceived = True
        except:
            print ("Unexpected error on (self.attr_EventReceived = False):", sys.exc_info()[0])

    def HandleEvent2 (self, args):
        try:
            print("Event Chaos arrived")
            print(args)
        except:
            print ("Unexpected error on (self.attr_EventReceived = False):", sys.exc_info()[0])

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(EventReceiver.main) ENABLED START #
    return run((EventReceiver,), args=args, **kwargs)
    # PROTECTED REGION END #    //  EventReceiver.main

if __name__ == '__main__':
    main()
