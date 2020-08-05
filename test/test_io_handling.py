# BSD 3-Clause License
#
# Copyright (c) 2020, IPASC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import numpy as np
from unittest.case import TestCase

from ipasc_tool.core import PAData
from ipasc_tool.iohandler import write_data
from ipasc_tool.iohandler import load_data
from test.utils import create_complete_device_metadata_dictionary


class DeviceMetaDataCreatorTest(TestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_write_and_read_random_dictionary(self):

        device_dict = create_complete_device_metadata_dictionary()


        pa_data = PAData(time_series_data=np.zeros([256, 2048]),
                         meta_data={"test_int": 3, "test_float": 3.14, "test_string": "test", "test_list": [3, 5, 7]},
                         meta_data_device=device_dict)
        write_data("test.hdf5", pa_data)
        test_data = load_data("test.hdf5")

        for original, test in zip(pa_data.__dict__, test_data.__dict__):
            assert original == test

        print(test_data.binary_time_series_data)
        print(test_data.meta_data_device)
        print(test_data.meta_data)

        #clean up after test
        if os.path.exists("test.hdf5"):
            os.remove("test.hdf5")