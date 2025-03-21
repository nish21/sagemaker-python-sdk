# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Helper methods for testing."""
from __future__ import absolute_import

from sagemaker.workflow.properties import Properties
from sagemaker.workflow.steps import Step, StepTypeEnum


def ordered(obj):
    """Helper function for dict comparison.

    Recursively orders a json-like dict or list of dicts.

    Args:
        obj: either a list or a dict

    Returns:
        either a sorted list of elements or sorted list of tuples
    """
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


class CustomStep(Step):
    def __init__(self, name, display_name=None, description=None, depends_on=None):
        super(CustomStep, self).__init__(
            name, display_name, description, StepTypeEnum.TRAINING, depends_on
        )
        self._properties = Properties(path=f"Steps.{name}")

    @property
    def arguments(self):
        return dict()

    @property
    def properties(self):
        return self._properties
