#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_control_plane_device_info
short_description: Information module for Sda Fabric Control Plane Device
description:
- Get all Sda Fabric Control Plane Device.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description:
    - DeviceIPAddress query parameter. Device IP Address.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Fabric Control Plane Device reference
  description: Complete reference of the Sda Fabric Control Plane Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Fabric Control Plane Device
  cisco.dnac.sda_fabric_control_plane_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIPAddress: string
  register: result

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
