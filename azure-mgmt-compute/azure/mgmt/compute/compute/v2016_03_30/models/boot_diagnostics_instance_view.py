# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BootDiagnosticsInstanceView(Model):
    """The instance view of a virtual machine boot diagnostics.

    :param console_screenshot_blob_uri: The console screenshot blob URI.
    :type console_screenshot_blob_uri: str
    :param serial_console_log_blob_uri: The Linux serial console log blob Uri.
    :type serial_console_log_blob_uri: str
    """

    _attribute_map = {
        'console_screenshot_blob_uri': {'key': 'consoleScreenshotBlobUri', 'type': 'str'},
        'serial_console_log_blob_uri': {'key': 'serialConsoleLogBlobUri', 'type': 'str'},
    }

    def __init__(self, console_screenshot_blob_uri=None, serial_console_log_blob_uri=None):
        self.console_screenshot_blob_uri = console_screenshot_blob_uri
        self.serial_console_log_blob_uri = serial_console_log_blob_uri
