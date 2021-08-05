#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_version_info
short_description: Information module for Configuration Template Version
description:
- Get Configuration Template Version by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  templateId:
    description:
    - TemplateId path parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Version reference
  description: Complete reference of the Configuration Template Version object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Configuration Template Version by id
  cisco.dnac.configuration_template_version_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    templateId: string
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
        "name": "string",
        "projectName": "string",
        "projectId": "string",
        "templateId": "string",
        "versionsInfo": [
          {
            "id": "string",
            "description": "string",
            "versionTime": 0
          }
        ],
        "composite": true
      }
    ]
"""
