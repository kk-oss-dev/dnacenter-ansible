#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: topology_site_info
short_description: Information module for Topology Site
description:
- Get all Topology Site.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Topology Site reference
  description: Complete reference of the Topology Site object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Topology Site
  cisco.dnac.topology_site_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
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
        "sites": [
          {
            "displayName": "string",
            "groupNameHierarchy": "string",
            "id": "string",
            "latitude": "string",
            "locationAddress": "string",
            "locationCountry": "string",
            "locationType": "string",
            "longitude": "string",
            "name": "string",
            "parentId": "string"
          }
        ]
      },
      "version": "string"
    }
"""
