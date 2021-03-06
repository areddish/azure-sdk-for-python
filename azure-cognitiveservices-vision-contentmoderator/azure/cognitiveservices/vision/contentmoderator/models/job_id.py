# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobId(Model):
    """JobId.

    :param job_id: Id of the created job.
    :type job_id: str
    """

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
    }

    def __init__(self, job_id=None):
        super(JobId, self).__init__()
        self.job_id = job_id
