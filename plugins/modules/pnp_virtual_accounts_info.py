#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_virtual_accounts_info
short_description: Information module for Pnp Virtual Accounts
description:
- Get all Pnp Virtual Accounts.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  domain:
    description:
    - Domain path parameter. Smart Account Domain.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Pnp Virtual Accounts reference
  description: Complete reference of the Pnp Virtual Accounts object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Pnp Virtual Accounts
  cisco.dnac.pnp_virtual_accounts_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    domain: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
