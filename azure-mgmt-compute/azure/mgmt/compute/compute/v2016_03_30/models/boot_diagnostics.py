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


class BootDiagnostics(Model):
    """Describes Boot Diagnostics.

    :param enabled: Whether boot diagnostics should be enabled on the Virtual
     Machine.
    :type enabled: bool
    :param storage_uri: URI of the storage account to use for placing the
     console output and screenshot.
    :type storage_uri: str
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
    }

    def __init__(self, enabled=None, storage_uri=None):
        self.enabled = enabled
        self.storage_uri = storage_uri
