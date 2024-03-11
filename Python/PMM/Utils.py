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