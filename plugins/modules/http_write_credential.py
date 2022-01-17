#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: http_write_credential
short_description: Resource module for Http Write Credential
description:
- Manage operations create and update of the resource Http Write Credential.
- Updates global HTTP write credentials.
- Adds global HTTP write credentials.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Http Write Credential's comments.
    type: str
  credentialType:
    description: Http Write Credential's credentialType.
    type: str
  description:
    description: Http Write Credential's description.
    type: str
  id:
    description: Http Write Credential's id.
    type: str
  instanceTenantId:
    description: Http Write Credential's instanceTenantId.
    type: str
  instanceUuid:
    description: Http Write Credential's instanceUuid.
    type: str
  password:
    description: Http Write Credential's password.
    type: str
  port:
    description: Http Write Credential's port.
    type: int
  secure:
    description: Secure flag.
    type: bool
  username:
    description: Http Write Credential's username.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function create_http_write_credentials used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.create_http_write_credentials

- name: SDK function update_http_write_credentials used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.update_http_write_credentials

notes:
  - Paths used: put /dna/intent/api/v1/global-credential/http-write,
    post /dna/intent/api/v1/global-credential/http-write
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.http_write_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    port: 0
    secure: true
    username: string

- name: Create
  cisco.dnac.http_write_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    port: 0
    secure: true
    username: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
