#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: task_count_info
short_description: Information module for Task Count
description:
- Get all Task Count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  startTime:
    description:
    - StartTime query parameter. This is the epoch start time from which tasks need to be fetched.
    type: str
  endTime:
    description:
    - EndTime query parameter. This is the epoch end time upto which audit records need to be fetched.
    type: str
  data:
    description:
    - Data query parameter. Fetch tasks that contains this data.
    type: str
  errorCode:
    description:
    - ErrorCode query parameter. Fetch tasks that have this error code.
    type: str
  serviceType:
    description:
    - ServiceType query parameter. Fetch tasks with this service type.
    type: str
  username:
    description:
    - Username query parameter. Fetch tasks with this username.
    type: str
  progress:
    description:
    - Progress query parameter. Fetch tasks that contains this progress.
    type: str
  isError:
    description:
    - IsError query parameter. Fetch tasks ended as success or failure. Valid values true, false.
    type: str
  failureReason:
    description:
    - FailureReason query parameter. Fetch tasks that contains this failure reason.
    type: str
  parentId:
    description:
    - ParentId query parameter. Fetch tasks that have this parent Id.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Task Count reference
  description: Complete reference of the Task Count object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Task Count
  cisco.dnac.task_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    startTime: string
    endTime: string
    data: string
    errorCode: string
    serviceType: string
    username: string
    progress: string
    isError: string
    failureReason: string
    parentId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
