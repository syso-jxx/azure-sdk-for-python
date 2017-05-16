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


class DiagnosticsProfile(Model):
    """Describes a diagnostics profile.

    :param boot_diagnostics: Boot Diagnostics is a debugging feature which
     allows the user to view console output and/or a screenshot of the virtual
     machine from the hypervisor.
    :type boot_diagnostics: :class:`BootDiagnostics
     <azure.mgmt.compute.compute.v2015_06_15.models.BootDiagnostics>`
    """

    _attribute_map = {
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnostics'},
    }

    def __init__(self, boot_diagnostics=None):
        self.boot_diagnostics = boot_diagnostics
