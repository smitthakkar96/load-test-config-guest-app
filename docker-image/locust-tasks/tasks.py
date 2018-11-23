#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid
import json

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class PostTaskSet(TaskSet):

    @task(2)
    def post_guest(self):
    	headers = {'content-type': 'application/json'}
        self.client.post(
            "/rest/insert", 
            data=json.dumps({"first": "guest_" + str(uuid.uuid4()), "last": str(datetime.now())}), 
            headers=headers
        )

    @task(1)
    def get_guest_list(self):
        self.client.get('/rest/query')

class PostLocust(HttpLocust):
    task_set = PostTaskSet
