"""classic Acrobot task"""
from gym import core, spaces
from gym.utils import seeding
import numpy as np
from numpy import sin, cos, pi
import time
from acrobot import AcrobotEnv

__copyright__ = "Copyright 2013, RLPy http://acl.mit.edu/RLPy"
__credits__ = ["Alborz Geramifard", "Robert H. Klein", "Christoph Dann",
               "William Dabney", "Jonathan P. How"]
__license__ = "BSD 3-Clause"
__author__ = "Christoph Dann <cdann@cdann.de>"

# SOURCE:
# https://github.com/rlpy/rlpy/blob/master/rlpy/Domains/Acrobot.py

class Acrobot_Mass1(AcrobotEnv):
    LINK_LENGTH_1 = 1.  # [m]
    LINK_LENGTH_2 = 1.  # [m]
    LINK_MASS_1 = 0.1  #: [kg] mass of link 1
    LINK_MASS_2 = 1.

class Acrobot_Mass2(AcrobotEnv):
    LINK_LENGTH_1 = 1.  # [m]
    LINK_LENGTH_2 = 1.  # [m]
    LINK_MASS_1 = 1.  #: [kg] mass of link 1
    LINK_MASS_2 = 1.5