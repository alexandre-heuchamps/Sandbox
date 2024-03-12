import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==============================================================================
def speed_to_Ma(v: float, vsound: float = 330.0) -> float:
    """ Converts a speed expressed in m/s to a speed expressed in Ma

    Parameters
    ----------
    v: <class 'float'>
        Speed to convert in Ma
    vsound: <class 'float'> (default: 330.0)
        Speed of sound

    Returns
    -------
    _: <class 'float'>
        Equivalent of input speed, in terms of Ma """
    return (v / vsound)
# ==============================================================================

# ==============================================================================
def Ma_to_speed(Ma: float, vsound: float = 330.0) -> float:
    """ Converts a speed expressed in Ma to a speed expressed in m/s

    Parameters
    ----------
    Ma: <class 'float'>
        Speed to convert in m/s
    vsound: <class 'float'> (default: 330.0)
        Speed of sound

    Returns
    -------
    _: <class 'float'>
        Equivalent of input speed, in terms of m/s """
    return (Ma * vsound)
# ==============================================================================

# ==============================================================================
def speed_to_kph(v: float) -> float:
    """ Converts a speed expressed in m/s to a speed expressed in km/h

    Parameters
    ----------
    v: <class 'float'>
        Speed of to convert in km/h

    Returns
    -------
    _: <class 'float'>
        Equivalent of input speed, in terms of km/h """
    return (3.6 * v)
# ==============================================================================

# ==============================================================================
def kph_to_speed(v: float) -> float:
    """ Converts a speed expressed in km/h to a speed expressed in m/s

    Parameters
    ----------
    v: <class 'float'>
        Speed of to convert in m/s

    Returns
    -------
    _: <class 'float'>
        Equivalent of input speed, in terms of m/s """
    return (v / 3.6)
# ==============================================================================

# ==============================================================================
def vecnorm(v: np.array) -> float:
    """ Returns the norm of the input vector

    Parameters
    ----------
    v: <class 'numpy.array'>
        Vector for which the norm is returned

    Returns
    -------
    _: <class 'float'>
        Norm of the input vector, computed through numpy.linalg.norm(v) """
    return np.linalg.norm(v)
# ==============================================================================

# ==============================================================================
def gravity_effect(m: float, g: np.array = np.array([0.0, 0.0, -9.81])) -> np.array:
    """ Returns the gravity force

    Parameters
    ----------
    m: <class 'float'>
        Mass of the object on which the gravity force is applied
    g: <class 'numpy.array'> (default: np.array([0.0, 0.0, -9.81]))
        Gravity vector

    Returns
    -------
    _: <class 'numpy.array'>
        Gravity force, computed as m * g """
    return m * g
# ==============================================================================

# ==============================================================================
def plot_vals(self, *v: np.array) -> None:
    """ Function plotting vectors against each other

    Parameters
    ----------
    *v: <class 'numpy.array'>
        Vectors to consider

    Returns
    -------
    _: """
    if len(v) == 2:
        plt.figure()
        plt.plot(*v)
        plt.show()
    elif len(v) == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(*v)
        plt.show()
    else:
        print("Invalid number of arguments. Provide only 2 or 3 arguments.")
# ==============================================================================