#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_info
short_description: Information module for Interface
description:
- Get all Interface.
- Get list of all properties & operations valid for an interface.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceUuid:
    description:
    - InterfaceUuid path parameter. Interface ID.
    type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    devices.Devices.legit_operations_for_interface,

  - Paths used are
    get /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation,

"""

EXAMPLES = r"""
- name: Get all Interface
  cisco.dnac.interface_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    interfaceUuid: string
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
        "type": "string",
        "properties": {
          "interfaceUuid": {
            "type": "string"
          },
          "properties": {
            "type": "string",
            "items": [
              {
                "type": "string",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "applicable": {
                    "type": "string"
                  },
                  "failureReason": {
                    "type": "string"
                  }
                },
                "required": [
                  "string"
                ]
              }
            ]
          },
          "operations": {
            "type": "string",
            "items": [
              {
                "type": "string",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "applicable": {
                    "type": "string"
                  },
                  "failureReason": {
                    "type": "string"
                  }
                },
                "required": [
                  "string"
                ]
              }
            ]
          }
        },
        "required": [
          "string"
        ]
      },
      "version": {
        "type": "string"
      }
    }
"""