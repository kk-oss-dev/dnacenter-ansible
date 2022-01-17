#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reports_view_group_info
short_description: Information module for Reports View Group
description:
- Get all Reports View Group.
- Get Reports View Group by id.
- Gives a list of summary of all view groups.
- Gives a list of summary of all views in a viewgroup. Use "Get all view groups" API to get the viewGroupIds (required as a query param for this API) for available viewgroups.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  viewGroupId:
    description:
    - ViewGroupId path parameter. ViewGroupId of viewgroup.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_all_view_groups used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    reports.Reports.get_all_view_groups

- name: SDK function get_views_for_a_given_view_group used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    reports.Reports.get_views_for_a_given_view_group

notes:
  - Paths used: get /dna/intent/api/v1/data/view-groups,
    get /dna/intent/api/v1/data/view-groups/{viewGroupId}
"""

EXAMPLES = r"""
- name: Get all Reports View Group
  cisco.dnac.reports_view_group_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
  register: result

- name: Get Reports View Group by id
  cisco.dnac.reports_view_group_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    viewGroupId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "viewGroupId": "string",
      "views": [
        {
          "description": "string",
          "viewId": "string",
          "viewName": "string"
        }
      ]
    }
"""
