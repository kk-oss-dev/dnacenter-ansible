#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_functional_capability_info
short_description: Information module for Network Device Functional Capability
description:
- Get all Network Device Functional Capability.
- Get Network Device Functional Capability by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Functional Capability UUID.
    type: str
  deviceId:
    description:
    - >
      DeviceId query parameter. Accepts comma separated deviceid's and return list of functional-capabilities for
      the given id's. If invalid or not-found id's are provided, null entry will be returned in the list.
    type: str
  functionName:
    description:
    - FunctionName query parameter.
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Network Device Functional Capability reference
  description: Complete reference of the Network Device Functional Capability object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Device Functional Capability
  cisco.dnac.network_device_functional_capability_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    functionName: []
  register: result

- name: Get Network Device Functional Capability by id
  cisco.dnac.network_device_functional_capability_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "attributeInfo": {},
        "functionDetails": [
          {
            "attributeInfo": {},
            "id": "string",
            "propertyName": "string",
            "stringValue": "string"
          }
        ],
        "functionName": "string",
        "functionOpState": "string",
        "id": "string"
      },
      "version": "string"
    }
"""
