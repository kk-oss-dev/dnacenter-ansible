#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: command_runner_run_command
short_description: Resource module for Command Runner Run Command
description:
- Manage operation create of the resource Command Runner Run Command.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  commands:
    description: Command Runner Run Command's commands.
    elements: str
    type: list
  description:
    description: Command Runner Run Command's description.
    type: str
  deviceUuids:
    description: Command Runner Run Command's deviceUuids.
    elements: str
    type: list
  name:
    description: Command Runner Run Command's name.
    type: str
  timeout:
    description: Command Runner Run Command's timeout.
    type: int
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Command Runner Run Command reference
  description: Complete reference of the Command Runner Run Command object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.command_runner_run_command:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    commands:
    - string
    description: string
    deviceUuids:
    - string
    name: string
    timeout: 0

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": {},
        "url": "string"
      },
      "version": "string"
    }
"""
