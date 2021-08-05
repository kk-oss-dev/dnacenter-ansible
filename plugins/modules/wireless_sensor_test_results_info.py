#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_sensor_test_results_info
short_description: Information module for Wireless Sensor Test Results
description:
- Get all Wireless Sensor Test Results.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  siteId:
    description:
    - SiteId query parameter. Assurance site UUID.
    type: str
  startTime:
    description:
    - StartTime query parameter. The epoch time in milliseconds.
    type: int
  endTime:
    description:
    - EndTime query parameter. The epoch time in milliseconds.
    type: int
  testFailureBy:
    description:
    - TestFailureBy query parameter. Obtain failure statistics group by "area", "building", or "floor".
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Wireless Sensor Test Results reference
  description: Complete reference of the Wireless Sensor Test Results object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Wireless Sensor Test Results
  cisco.dnac.wireless_sensor_test_results_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    siteId: string
    startTime: 0
    endTime: 0
    testFailureBy: area
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "summary": {
        "totalTestCount": 0,
        "ONBOARDING": {
          "AUTH": {
            "passCount": 0,
            "failCount": 0
          },
          "DHCP": {
            "passCount": 0,
            "failCount": 0
          },
          "ASSOC": {
            "passCount": 0,
            "failCount": 0
          }
        },
        "PERFORMANCE": {
          "IPSLASENDER": {
            "passCount": 0,
            "failCount": 0
          }
        },
        "NETWORK_SERVICES": {
          "DNS": {
            "passCount": 0,
            "failCount": 0
          }
        },
        "APP_CONNECTIVITY": {
          "HOST_REACHABILITY": {
            "passCount": 0,
            "failCount": 0
          },
          "WEBSERVER": {
            "passCount": 0,
            "failCount": 0
          },
          "FILETRANSFER": {
            "passCount": 0,
            "failCount": 0
          }
        },
        "RF_ASSESSMENT": {
          "DATA_RATE": {
            "passCount": 0,
            "failCount": 0
          },
          "SNR": {
            "passCount": 0,
            "failCount": 0
          }
        },
        "EMAIL": {
          "MAILSERVER": {
            "passCount": 0,
            "failCount": 0
          }
        }
      },
      "failureStats": [
        {
          "errorCode": 0,
          "errorTitle": "string",
          "testType": "string",
          "testCategory": "string"
        }
      ]
    }
"""
