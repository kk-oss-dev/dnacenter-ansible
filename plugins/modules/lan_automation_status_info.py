#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_status_info
short_description: Information module for Lan Automation Status
description:
- Get all Lan Automation Status.
- Get Lan Automation Status by id.
- Invoke this API to get the LAN Automation session status based on the given Lan Automation session Id.
- Invoke this API to get the LAN Automation session status.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. Offset/starting row of the LAN Automation session from which status needs to be retrieved.
    type: str
  limit:
    description:
    - Limit query parameter. Number of LAN Automations session status to be retrieved.
    type: str
  id:
    description:
    - Id path parameter. LAN Automation Session Identifier.
    type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_status,
    lan_automation.LanAutomation.lan_automation_status_by_id,

  - Paths used are
    get /dna/intent/api/v1/lan-automation/status,
    get /dna/intent/api/v1/lan-automation/status/{id},

"""

EXAMPLES = r"""
- name: Get all Lan Automation Status
  cisco.dnac.lan_automation_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    offset: string
    limit: string
  register: result

- name: Get Lan Automation Status by id
  cisco.dnac.lan_automation_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
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
      "response": [
        {
          "id": "string",
          "discoveredDeviceSiteNameHierarchy": "string",
          "primaryDeviceManagmentIPAddress": "string",
          "ipPoolList": [
            {
              "ipPoolName": "string",
              "ipPoolRole": "string"
            }
          ],
          "primaryDeviceInterfaceNames": [
            "string"
          ],
          "status": "string",
          "action": "string",
          "creationTime": "string",
          "multicastEnabled": true,
          "peerDeviceManagmentIPAddress": "string",
          "discoveredDeviceList": [
            {
              "name": "string",
              "serialNumber": "string",
              "state": "string",
              "ipAddressInUseList": [
                "string"
              ]
            }
          ]
        }
      ],
      "version": "string"
    }
"""