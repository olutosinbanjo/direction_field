#                      Direction Field Visualization with Python
#
# Copyright 2022 Oluwatosin Odubanjo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Device information with data parallel control

07-07-2022
"""

import dpctl

class devices:

    def __init__(self, name):
        self.name = name
        if (self.name == "all"):
            self.device = dpctl.get_devices()
        elif (self.name == "default"):
            self.device = dpctl.select_default_device()
        elif (self.name == "gpu"):
            self.device = dpctl.select_gpu_device()
        else:
            self.device = dpctl.select_cpu_device()

    def __str__(self):
        return f"The {self.name} device on this system is:\n\n {self.device}"

   
def main():
    
    # These are objects of the class devices
    device_all = devices("all")
    device_default = devices("default") 
    device_gpu = devices("gpu")
    device_cpu = devices("cpu")

    print(device_all, '\n')
    print(device_default, '\n')
    print(device_gpu, '\n')
    print(device_cpu, '\n')

if __name__ == "__main__":
    main()
