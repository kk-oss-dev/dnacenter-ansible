#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: itsm_integration_events_failed_info
short_description: Information module for Itsm Integration Events Failed
description:
- Get all Itsm Integration Events Failed.
- Used to retrieve the list of integration events that failed to create tickets in ITSM.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  instanceId:
    description:
    - InstanceId query parameter. Instance Id of the failed event as in the Runtime Dashboard.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_failed_itsm_events used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    itsm.Itsm.get_failed_itsm_events

notes:
  - Paths used: get /dna/intent/api/v1/integration/events
"""

EXAMPLES = r"""
- name: Get all Itsm Integration Events Failed
  cisco.dnac.itsm_integration_events_failed_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    instanceId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "instanceId": "string",
        "eventId": "string",
        "name": "string",
        "type": "string",
        "category": "string",
        "domain": "string",
        "subDomain": "string",
        "severity": "string",
        "source": "string",
        "timestamp": 0,
        "enrichmentInfo": {
          "eventStatus": "string",
          "errorCode": "string",
          "errorDescription": "string",
          "responseReceivedFromITSMSystem": {}
        },
        "description": "string"
      }
    ]
"""
