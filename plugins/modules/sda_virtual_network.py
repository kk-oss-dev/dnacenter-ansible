#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network
short_description: Resource module for Sda Virtual Network
description:
- Manage operations create and delete of the resource Sda Virtual Network.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Virtual Network's payload.
    suboptions:
      siteNameHierarchy:
        description: Sda Virtual Network's siteNameHierarchy.
        type: str
      virtualNetworkName:
        description: Sda Virtual Network's virtualNetworkName.
        type: str
    type: list
  siteNameHierarchy:
    description: SiteNameHierarchy query parameter.
    type: str
  virtualNetworkName:
    description: VirtualNetworkName query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Virtual Network reference
  description: Complete reference of the Sda Virtual Network object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_virtual_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Delete all
  cisco.dnac.sda_virtual_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string
    virtualNetworkName: string

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
      "name": "string",
      "roles": [
        "string"
      ],
      "deviceManagementIpAddress": "string",
      "siteHierarchy": "string"
    }
"""
