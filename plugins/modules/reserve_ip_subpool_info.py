#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: reserve_ip_subpool_info
short_description: Information module for Reserve Ip Subpool
description:
- Get all Reserve Ip Subpool.
- API to get the ip subpool info.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter. Site id to get the reserve ip associated with the site.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: str
  limit:
    description:
    - Limit query parameter. No of Global Pools to be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_reserve_ip_subpool used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.network_settings.NetworkSettings.get_reserve_ip_subpool

notes:
  - Paths used: get /dna/intent/api/v1/reserve-ip-subpool
"""

EXAMPLES = r"""
- name: Get all Reserve Ip Subpool
  cisco.dnac.reserve_ip_subpool_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    siteId: string
    offset: string
    limit: string
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
          "groupName": "string",
          "ipPools": [
            {
              "ipPoolName": "string",
              "dhcpServerIps": [
                {}
              ],
              "gateways": [
                "string"
              ],
              "createTime": 0,
              "lastUpdateTime": 0,
              "totalIpAddressCount": 0,
              "usedIpAddressCount": 0,
              "parentUuid": "string",
              "owner": "string",
              "shared": true,
              "overlapping": true,
              "configureExternalDhcp": true,
              "usedPercentage": "string",
              "clientOptions": {},
              "groupUuid": "string",
              "dnsServerIps": [
                {}
              ],
              "context": [
                {
                  "owner": "string",
                  "contextKey": "string",
                  "contextValue": "string"
                }
              ],
              "ipv6": true,
              "id": "string",
              "ipPoolCidr": "string"
            }
          ],
          "siteId": "string",
          "siteHierarchy": "string",
          "type": "string",
          "groupOwner": "string"
        }
      ],
      "version": "string"
    }
"""
