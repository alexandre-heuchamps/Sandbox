#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    """ Function representing the right hand-side of the ODEs to solve

    Parameters
    ----------
    t: <class 'float'>
        Current time
    y: <class 'numpy.ndarray'>
        State vector

    Returns
    -------
    _: <class 'numpy.ndarray'>
        Right hand-side of the equation to solve """
    return (t * y)



def euler(f, tn, yn, h):
    """ Function returning the result of a 4th order Runge-Kutta solver

    Parameters
    ----------
    f: <class 'function'>
        ODEs to solve
    tn: <class 'float'>
        Current time
    yn: <class 'numpy.ndarray'>
        Current state vector
    h: <class 'float'>
        Timestep

    Returns
    -------
    _: <class 'numpy.ndarray'>
        Updated state vector """
    return (yn + h * f(tn, yn))



def RK4(f, tn, yn, h):
    """ Function returning the result of a 4th order Runge-Kutta solver

    Parameters
    ----------
    f: <class 'function'>
        ODEs to solve
    tn: <class 'float'>
        Current time
    yn: <class 'numpy.ndarray'>
        Current state vector
    h: <class 'float'>
        Timestep

    Returns
    -------
    _: <class 'numpy.ndarray'>
        Updated state vector """
    k1 = f(tn, yn)
    k2 = f(tn + 0.5 * h, yn + 0.5 * h * k1)
    k3 = f(tn + 0.5 * h, yn + 0.5 * h * k2)
    k4 = f(tn + h, yn + h * k3)
    return (yn + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))



def solveIVP(f, tspan, y0, h, solver):
    t = np.arange(start = tspan[0], stop = tspan[1] + h, step = h)
    y = np.zeros(len(t))
    y[0] = y0

    for i_tn, v_tn in enumerate(t[:-1]):
        y[i_tn + 1] = solver(f, v_tn, y[i_tn], h)

    return t, y


if __name__ == "__main__":
    y0 = 1.0
    h = 0.2
    tspan = [0.0, 1.0]

    # Exact solution to the equation y' = t*y, y[0] = 1
    hExact = 0.01 * h
    tExact = np.arange(start = tspan[0], stop = tspan[1] + hExact, step = hExact)
    yExact = np.exp(0.5 * tExact**2)

    # Approximate solution to the equation y' = t*y, y[0] = 1
    tEuler, yEuler = solveIVP(f, tspan, y0, h, euler)
    tRK4, yRK4 = solveIVP(f, tspan, y0, h, RK4)

    # Plot a comparision between results
    plt.plot(tExact, yExact, color = 'black', label = "Exact")
    plt.plot(tEuler, yEuler, 'o-', color = 'blue', label = "Euler")
    plt.plot(tRK4, yRK4, 's-', color = 'red', label = "RK4")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y(t)$")
    plt.legend()
    plt.show()