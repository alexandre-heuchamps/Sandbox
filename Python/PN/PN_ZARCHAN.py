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
    H = 1e-3                    # timestep

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

    # Start simulation
    while((VC >= 0) and (n < NDT)):
        if RTM < 1000.0:
            H = 0.0002
        else:
            H = 0.01

        # Needed for update
        BETAOLD = BETA
        RT1OLD = RT1
        RT2OLD = RT2
        RM1OLD = RM1
        RM2OLD = RM2
        VM1OLD = VM1
        VM2OLD = VM2
        STEP = 1
        FLAG = 0        # apply a midpoint 2nd order Runge-Kutta method if set

        while(STEP <= 1):
            if FLAG == 1:
                STEP = 2
                BETA = BETA + H * BETAD
                RT1 = RT1 + H * VT1
                RT2 = RT2 + H * VT2
                RM1 = RM1 + H * VM1
                RM2 = RM2 + H * VM2
                VM1 = VM1 + H * AM1
                VM2 = VM2 + H * AM2
                T = T + H

            RTM1 = RT1 - RM1
            RTM2 = RT2 - RM2
            RTM = np.sqrt(RTM1**2 + RTM2**2)
            VTM1 = VT1 - VM1
            VTM2 = VT2 - VM2
            VC = -(RTM1 * VTM1 + RTM2 * VTM2) / RTM
            XLAM = np.arctan2(RTM2, RTM1)
            XLAMD = (RTM1 * VTM2 - RTM2 * VTM1) / (RTM**2)
            XNC = XNP * VC * XLAMD
            AM1 = -XNC * np.sin(XLAM)
            AM2 = XNC * np.cos(XLAM)
            VT1 = -VT * np.cos(BETA)
            VT2 = VT * np.sin(BETA)
            BETAD = XNT / VT            # target angular velocity
            FLAG = 1                    # set to enable midpoint RK2 solver

        # Propagate the states using a midpoint second-order Runge-Kutta method
        FLAG = 0                                    # unset to disable RK solver
        BETA = 0.5 * (BETAOLD + BETA + H * BETAD)
        RT1 = 0.5 * (RT1OLD + RT1 + H * VT1)
        RT2 = 0.5 * (RT2OLD + RT2 + H * VT2)
        RM1 = 0.5 * (RM1OLD + RM1 + H * VM1)
        RM2 = 0.5 * (RM2OLD + RM2 + H * VM2)
        VM1 = 0.5 * (VM1OLD + VM1 + H * AM1)
        VM2 = 0.5 * (VM2OLD + VM2 + H * AM2)
        S = S + H

        # Store data every 0.0999 seconds
        if S > 0.09999:
            S = 0.0
            n = n + 1
            ArrayT.append([T])
            ArrayRT1.append([RT1])
            ArrayRT2.append([RT2])
            ArrayRM1.append([RM1])
            ArrayRM2.append([RM2])
            ArrayXNCG.append([XNC / 32.2])
            ArrayRTM.append([RTM])

    # Plot results
    plt.plot(ArrayRT1, ArrayRT2, '-*', label = "Target")
    plt.plot(ArrayRM1, ArrayRM2, '-s', label = "Missile")
    plt.xlabel("Downrange (ft)")
    plt.ylabel("Altitude (ft)")
    plt.legend()
    plt.show()