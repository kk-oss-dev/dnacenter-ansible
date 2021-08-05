#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_module_info
short_description: Information module for Network Device Module
description:
- Get all Network Device Module.
- Get Network Device Module by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
  deviceId:
    description:
    - DeviceId query parameter.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: str
  nameList:
    description:
    - NameList query parameter.
    type: list
  vendorEquipmentTypeList:
    description:
    - VendorEquipmentTypeList query parameter.
    type: list
  partNumberList:
    description:
    - PartNumberList query parameter.
    type: list
  operationalStateCodeList:
    description:
    - OperationalStateCodeList query parameter.
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Network Device Module reference
  description: Complete reference of the Network Device Module object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Device Module
  cisco.dnac.network_device_module_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    limit: string
    offset: string
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
  register: result

- name: Get Network Device Module by id
  cisco.dnac.network_device_module_info:
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
        "assemblyNumber": "string",
        "assemblyRevision": "string",
        "attributeInfo": {},
        "containmentEntity": "string",
        "description": "string",
        "entityPhysicalIndex": "string",
        "id": "string",
        "isFieldReplaceable": "string",
        "isReportingAlarmsAllowed": "string",
        "manufacturer": "string",
        "moduleIndex": 0,
        "name": "string",
        "operationalStateCode": "string",
        "partNumber": "string",
        "serialNumber": "string",
        "vendorEquipmentType": "string"
      },
      "version": "string"
    }
"""
