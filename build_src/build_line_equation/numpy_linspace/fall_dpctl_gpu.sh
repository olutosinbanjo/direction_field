#!/bin/bash
source opt/intel/oneapi/setvars.sh > /dev/null 2>&1
/bin/echo "##" $(whoami) is compiling ~/direction_field/src/line_equation/numpy_linspace/fall_dpctl_gpu.py
python3 ~/direction_field/src/line_equation/numpy_linspace/fall_dpctl_gpu.py
