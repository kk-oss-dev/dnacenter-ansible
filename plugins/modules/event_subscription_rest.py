#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_rest
short_description: Resource module for Event Subscription Rest
description:
- Manage operations create and update of the resource Event Subscription Rest.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription Rest's payload.
    suboptions:
      description:
        description: Event Subscription Rest's description.
        type: str
      filter:
        description: Event Subscription Rest's filter.
        suboptions:
          eventIds:
            description: Event Subscription Rest's eventIds.
            elements: str
            type: list
        type: dict
      name:
        description: Event Subscription Rest's name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription Rest's subscriptionEndpoints.
        suboptions:
          instanceId:
            description: Event Subscription Rest's instanceId.
            type: str
          subscriptionDetails:
            description: Event Subscription Rest's subscriptionDetails.
            suboptions:
              connectorType:
                description: Event Subscription Rest's connectorType.
                type: str
            type: dict
        type: list
      subscriptionId:
        description: Event Subscription Rest's subscriptionId.
        type: str
      version:
        description: Event Subscription Rest's version.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription Rest reference
  description: Complete reference of the Event Subscription Rest object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.event_subscription_rest:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.event_subscription_rest:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
