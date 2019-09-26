# -*- coding: utf-8 -*-
# file: devices.py

# This code is part of Ocelot.
#
# Copyright (c) 2019 Leandro Seixas Rocha.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

'''
  Module devices
'''

from abc import ABCMeta, abstractmethod

class Device(object):
  __metaclass__ = ABCMeta
  def __init__(self):
    pass


class Qiskit(Device):
  def __init__(self):
    # import qiskit as qk
    pass


class Dwave(Device):
  def __init__(self):
    # import dwavebinarycsp
    pass


class Quil(Device):
  def __init__(self):
    # import pyquil as pq
    pass


class Cirq(Device):
  def __init__(self):
    # import cirq as cq
    pass


class Simulator(Device):
  def __init__(self):
    pass

