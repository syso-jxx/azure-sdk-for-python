# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AgentPool
from ._models_py3 import AgentPoolAvailableVersions
from ._models_py3 import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
from ._models_py3 import AgentPoolListResult
from ._models_py3 import AgentPoolUpgradeProfile
from ._models_py3 import AgentPoolUpgradeProfilePropertiesUpgradesItem
from ._models_py3 import AgentPoolUpgradeSettings
from ._models_py3 import BaseManagedCluster
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerServiceDiagnosticsProfile
from ._models_py3 import ContainerServiceLinuxProfile
from ._models_py3 import ContainerServiceMasterProfile
from ._models_py3 import ContainerServiceNetworkProfile
from ._models_py3 import ContainerServiceSshConfiguration
from ._models_py3 import ContainerServiceSshPublicKey
from ._models_py3 import ContainerServiceVMDiagnostics
from ._models_py3 import CredentialResult
from ._models_py3 import CredentialResults
from ._models_py3 import ManagedCluster
from ._models_py3 import ManagedClusterAADProfile
from ._models_py3 import ManagedClusterAPIServerAccessProfile
from ._models_py3 import ManagedClusterAccessProfile
from ._models_py3 import ManagedClusterAddonProfile
from ._models_py3 import ManagedClusterAddonProfileIdentity
from ._models_py3 import ManagedClusterAgentPoolProfile
from ._models_py3 import ManagedClusterAgentPoolProfileProperties
from ._models_py3 import ManagedClusterIdentity
from ._models_py3 import ManagedClusterIdentityUserAssignedIdentitiesValue
from ._models_py3 import ManagedClusterListResult
from ._models_py3 import ManagedClusterLoadBalancerProfile
from ._models_py3 import ManagedClusterLoadBalancerProfileManagedOutboundIPs
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPPrefixes
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPs
from ._models_py3 import ManagedClusterPoolUpgradeProfile
from ._models_py3 import ManagedClusterPoolUpgradeProfileUpgradesItem
from ._models_py3 import ManagedClusterPropertiesAutoScalerProfile
from ._models_py3 import ManagedClusterPropertiesIdentityProfileValue
from ._models_py3 import ManagedClusterSKU
from ._models_py3 import ManagedClusterServicePrincipalProfile
from ._models_py3 import ManagedClusterUpgradeProfile
from ._models_py3 import ManagedClusterWindowsProfile
from ._models_py3 import OperationListResult
from ._models_py3 import OperationValue
from ._models_py3 import PowerState
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourcesListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceReference
from ._models_py3 import SubResource
from ._models_py3 import TagsObject
from ._models_py3 import UserAssignedIdentity

from ._container_service_client_enums import AgentPoolMode
from ._container_service_client_enums import AgentPoolType
from ._container_service_client_enums import Code
from ._container_service_client_enums import ConnectionStatus
from ._container_service_client_enums import ContainerServiceStorageProfileTypes
from ._container_service_client_enums import ContainerServiceVMSizeTypes
from ._container_service_client_enums import Count
from ._container_service_client_enums import Expander
from ._container_service_client_enums import LicenseType
from ._container_service_client_enums import LoadBalancerSku
from ._container_service_client_enums import ManagedClusterSKUName
from ._container_service_client_enums import ManagedClusterSKUTier
from ._container_service_client_enums import NetworkMode
from ._container_service_client_enums import NetworkPlugin
from ._container_service_client_enums import NetworkPolicy
from ._container_service_client_enums import OSDiskType
from ._container_service_client_enums import OSType
from ._container_service_client_enums import OutboundType
from ._container_service_client_enums import PrivateEndpointConnectionProvisioningState
from ._container_service_client_enums import ResourceIdentityType
from ._container_service_client_enums import ScaleSetEvictionPolicy
from ._container_service_client_enums import ScaleSetPriority
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AgentPool",
    "AgentPoolAvailableVersions",
    "AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem",
    "AgentPoolListResult",
    "AgentPoolUpgradeProfile",
    "AgentPoolUpgradeProfilePropertiesUpgradesItem",
    "AgentPoolUpgradeSettings",
    "BaseManagedCluster",
    "CloudErrorBody",
    "ContainerServiceDiagnosticsProfile",
    "ContainerServiceLinuxProfile",
    "ContainerServiceMasterProfile",
    "ContainerServiceNetworkProfile",
    "ContainerServiceSshConfiguration",
    "ContainerServiceSshPublicKey",
    "ContainerServiceVMDiagnostics",
    "CredentialResult",
    "CredentialResults",
    "ManagedCluster",
    "ManagedClusterAADProfile",
    "ManagedClusterAPIServerAccessProfile",
    "ManagedClusterAccessProfile",
    "ManagedClusterAddonProfile",
    "ManagedClusterAddonProfileIdentity",
    "ManagedClusterAgentPoolProfile",
    "ManagedClusterAgentPoolProfileProperties",
    "ManagedClusterIdentity",
    "ManagedClusterIdentityUserAssignedIdentitiesValue",
    "ManagedClusterListResult",
    "ManagedClusterLoadBalancerProfile",
    "ManagedClusterLoadBalancerProfileManagedOutboundIPs",
    "ManagedClusterLoadBalancerProfileOutboundIPPrefixes",
    "ManagedClusterLoadBalancerProfileOutboundIPs",
    "ManagedClusterPoolUpgradeProfile",
    "ManagedClusterPoolUpgradeProfileUpgradesItem",
    "ManagedClusterPropertiesAutoScalerProfile",
    "ManagedClusterPropertiesIdentityProfileValue",
    "ManagedClusterSKU",
    "ManagedClusterServicePrincipalProfile",
    "ManagedClusterUpgradeProfile",
    "ManagedClusterWindowsProfile",
    "OperationListResult",
    "OperationValue",
    "PowerState",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourcesListResult",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ResourceReference",
    "SubResource",
    "TagsObject",
    "UserAssignedIdentity",
    "AgentPoolMode",
    "AgentPoolType",
    "Code",
    "ConnectionStatus",
    "ContainerServiceStorageProfileTypes",
    "ContainerServiceVMSizeTypes",
    "Count",
    "Expander",
    "LicenseType",
    "LoadBalancerSku",
    "ManagedClusterSKUName",
    "ManagedClusterSKUTier",
    "NetworkMode",
    "NetworkPlugin",
    "NetworkPolicy",
    "OSDiskType",
    "OSType",
    "OutboundType",
    "PrivateEndpointConnectionProvisioningState",
    "ResourceIdentityType",
    "ScaleSetEvictionPolicy",
    "ScaleSetPriority",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
