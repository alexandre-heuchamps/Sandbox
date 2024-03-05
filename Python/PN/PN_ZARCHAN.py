#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Simulation related parameters
    T = 0.0                     # time
    S = 0.0                     # time ("second version")
    n = 0                       # time iteration counter
    NDT = 300                   # maximum number of time iterations

    # Target related parameters
    VT = 50.0                   # target speed
    XNT = .5 * 32.2             # target normal acceleration (in ft/s*s)
    RT1 = 1E3                   # target position (x-axis)
    RT2 = 1E3                   # target position (y-axis)
    BETA = 0.0                  # target orientation
    VT1 = -VT * np.cos(BETA)    # target speed (x-axis)
    VT2 = VT * np.sin(BETA)     # target speed (y-axis)

    # Missile related parameters
    VM = 800.0                  # missile speed
    XNP = 4.0                   # missile normal acceleration (in g's)
    RM1 = 0.0                   # missile position (x-axis)
    RM2 = 0.0                   # missile position (y-axis)
    HEDEG = -20.0               # missile heading error (in deg)
    HE = HEDEG/57.3             # missile heading error (in rad)

    # LOS & relative values related parameters
    RTM1 = RT1 - RM1                                    # LOS vector (x-axis)
    RTM2 = RT2 - RM2                                    # LOS vector (y-axis)
    RTM = np.sqrt(RTM1**2 + RTM2**2)                    # LOS vector (norm)
    XLAM = np.arctan2(RTM2, RTM1)                       # LOS angle

    # Missile related parameters (continued)
    XLEAD = np.arcsin(VT * np.sin(BETA + XLAM) / VM)    # missile lead angle
    THET = XLAM + XLEAD
    VM1 = VM * np.cos(THET + HE)                        # missile speed (x-axis)
    VM2 = VM * np.sin(THET + HE)                        # missile speed (y-axis)

    # LOS & relative values related parameters (continued)
    VTM1 = VT1 - VM1                        # relative speed (x-axis)
    VTM2 = VT2 - VM2                        # relative speed (y-axis)
    VC = -(RTM1 * VTM1 + RTM2 * VTM2) / RTM # closing speed

    # Storage lists
    ArrayT = []
    ArrayRT1 = []
    ArrayRT2 = []
    ArrayRM1 = []
    ArrayRM2 = []
    ArrayXNCG = []
    ArrayRTM = []