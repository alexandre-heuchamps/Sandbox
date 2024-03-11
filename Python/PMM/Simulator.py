from World import World

class Simulator():
    """ Class to represent a 'Simulator' (for ballistic propagation) """

    def __init__(self,
                    dt: float = 1e-3,
                    ndt: int = int(1e3),
                    world: World = World(),
                 ) -> None:
        """ Initiate an object of type 'Simulator' with given timestep
        and number of timesteps

        Parameters
        ----------
        dt: <class 'float'> (default: 1e-3)
            Timestep used in the simulation
        ndt: <class 'int'> (default: int(1e3))
            Number of timesteps used in the simulation """
        self._dt: float = dt
        self._ndt: int = ndt
        self._world: World = world

    # ==========================================================================
    @property
    def dt(self) -> float:
        """ Get or set the current timestep """
        return self._dt

    @dt.setter
    def dt(self, dt: float = 1e-3) -> None:
        self._dt: float = dt
    # ==========================================================================

    # ==========================================================================
    @property
    def ndt(self) -> int:
        """ Get or set the number of timestep """
        return self._ndt

    @ndt.setter
    def ndt(self, ndt: int = int(1e3)) -> None:
        self._ndt: int = ndt
    # ==========================================================================

    # ==========================================================================
    def run(self, target, platform) -> None:
        """ Function performing the ballistic propagation

        Parameters
        ----------
        target: <class 'Target'>
            Target to be neutralised
        platform: <class 'Platform'>
            Platform neutralising the target """
        pass
    # ==========================================================================

    # ==========================================================================
    def speed_to_Ma(self, v: float, vsound: float = 330.0) -> float:
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

    def Ma_to_speed(self, Ma: float, vsound: float = 330.0) -> float:
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

    def speed_to_kph(self, v: float) -> float:
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

    def kph_to_speed(self, v: float) -> float:
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
    # ==========================================================================

    # ==========================================================================
    @property
    def world(self) -> World:
        """ Get or set the world in which the simulation takes place """
        return self._world

    @world.setter
    def world(self, world: World = World()) -> None:
        self._world: World = world
    # ==========================================================================



if __name__ == "__main__":
    sim = Simulator()
    v_mps = 330.0
    print(f"{v_mps} m/s == {sim.speed_to_kph(v_mps)} km/h == {sim.speed_to_Ma(v_mps)} Ma")