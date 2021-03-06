# -*- coding: utf-8 -*-
# Copyright 2018 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
from cloudkittyclient.tests.unit.v1 import base


class TestStorage(base.BaseAPIEndpointTestCase):

    def test_get_dataframes(self):
        self.storage.get_dataframes()
        self.api_client.get.assert_called_once_with('/v1/storage/dataframes')

    def test_get_dataframes_with_begin_end(self):
        self.storage.get_dataframes(begin='begin', end='end')
        try:
            self.api_client.get.assert_called_once_with(
                '/v1/storage/dataframes?begin=begin&end=end')
        # Passing a dict to urlencode can change arg order
        except AssertionError:
            self.api_client.get.assert_called_once_with(
                '/v1/storage/dataframes?end=end&begin=begin')
