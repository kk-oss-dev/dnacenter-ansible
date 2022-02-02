#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool
short_description: Resource module for Sda Virtual Network Ip Pool
description:
- Manage operations create and delete of the resource Sda Virtual Network Ip Pool.
- Add IP Pool in SDA Virtual Network.
- Delete IP Pool from SDA Virtual Network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  authenticationPolicyName:
    version_added: "4.0.0"
    description: Deprecated, same as vlanName, please use vlanName.
    type: str
  ipPoolName:
    version_added: "4.0.0"
    description: IpPoolName query parameter.
    type: str
  isL2FloodingEnabled:
    version_added: "4.0.0"
    description: Layer2 flooding enablement flag.
    type: bool
  isThisCriticalPool:
    version_added: "4.0.0"
    description: Critical pool enablement flag where depending on the pool type (data
      or voice), a corresponding Critical Vlan gets assigned to the Critical Pool.
    type: bool
  isWirelessPool:
    version_added: "4.0.0"
    description: Wireless Pool enablement flag.
    type: str
  poolType:
    version_added: "4.0.0"
    description: Pool Type (needed when assigning segment to INFRA_VN) (Example AP.).
    type: str
  scalableGroupName:
    version_added: "4.0.0"
    description: Scalable Group, that is associated to Virtual Network.
    type: str
  siteNameHierarchy:
    version_added: "4.0.0"
    description: Full path of sda fabric siteNameHierarchy.
    type: str
  trafficType:
    version_added: "4.0.0"
    description: Traffic type.
    type: str
  virtualNetworkName:
    description: VirtualNetworkName query parameter.
    type: str
  vlanName:
    version_added: "4.0.0"
    description: Vlan name for this segment, represent the segment name, if empty, vlanName
      would be auto generated by API.
    type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_ip_pool_in_sda_virtual_network,
    sda.Sda.delete_ip_pool_from_sda_virtual_network,

  - Paths used are
    post /dna/intent/api/v1/business/sda/virtualnetwork/ippool,
    delete /dna/intent/api/v1/business/sda/virtualnetwork/ippool,

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ipPoolName: string
    virtualNetworkName: string

- name: Create
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticationPolicyName: string
    ipPoolName: string
    isL2FloodingEnabled: true
    isThisCriticalPool: true
    isWirelessPool: string
    poolType: string
    scalableGroupName: string
    siteNameHierarchy: string
    trafficType: string
    virtualNetworkName: string
    vlanName: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""
