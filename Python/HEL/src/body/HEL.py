from typing import Dict, Tuple, Union


class HEL:
    """ Class for parametric high-energy laser (HEL) representation """

    __cnt: int = 0

    def __init__(self,
                    name: str = "HEL1",
                    wavelength: float = 1e-6,
                    P: float = 1.0,
                    M2: float = 1.2,
                    J: float = 1e-3,
                    w0: float = 2.5e-3,
                    r0: float = 1.0,
                    x0: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                    mode: Tuple[int, int] = (0, 0),
                ) -> None:
        """ Function initialising a new HEL

        Parameters
        ----------
        name: <class 'str'> (default: "HEL1")
            Name of the HEL
        wavelength: <class 'float'> (default: 1e-6)
            Wavelength of the HEL
        P: <class 'float'> (default: 1.0)
            Power of the HEL
        M2: <class 'float'> (default: 1.2)
            Beam quality of the HEL
        J: <class 'float'> (default: 1e-3)
            Jitter of the HEL
        w0: <class 'float'> (default: 2.5e-3)
            Beam waist of the HEL
        r0: <class 'float'> (default: 1.0)
            Distance from the HEL position at which the beam waist occurs
        x0: <class 'tuple'> (default: (0.0, 0.0, 0.0))
            Initial position of the HEL
        mode: <class 'tuple'> (default: (0.0, 0.0))
            Mode of the HEL (used for Hermitte-Gaussian beams) """
        __class__.__cnt += 1
        self._name: str = name
        self._wavelength: float = wavelength
        self._P: float = P
        self._M2: float = M2
        self._J: float = J
        self._w0: float = w0
        self._r0: float = r0
        self._x0: Tuple[float, float, float] = x0
        self._mode: Tuple[float, float] = mode

    # ==========================================================================
    def __del__(self) -> None:
        __class__.__cnt -= 1
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def get_count(cls) -> int:
        return cls.__cnt
    # ==========================================================================

    # ==========================================================================
    @property
    def name(self) -> str:
        """ Get or set the HEL name """
        return self._name

    @name.setter
    def name(self, name: str = "HEL1") -> None:
        self._name = name
    # ==========================================================================

    # ==========================================================================
    @property
    def wavelength(self) -> float:
        """ Get or set the HEL wavelength """
        return self._wavelength

    @wavelength.setter
    def wavelength(self, wavelength: float = 1.5e-6) -> None:
        self._wavelength = wavelength
    # ==========================================================================

    # ==========================================================================
    @property
    def P(self) -> float:
        """ Get or set the HEL power """
        return self._P

    @P.setter
    def P(self, P: float = 1.5) -> None:
        self._P = P
    # ==========================================================================

    # ==========================================================================
    @property
    def M2(self) -> float:
        """ Get or set the HEL beam quality factor """
        return self._M2

    @M2.setter
    def M2(self, M2: float = 1.65) -> None:
        self._M2 = M2
    # =========================================================================

    # ==========================================================================
    @property
    def J(self) -> float:
        """ Get or set the HEL beam jitter """
        return self._J

    @J.setter
    def J(self, J: float = 1.5) -> None:
        self._J = J
    # ==========================================================================

    # ==========================================================================
    @property
    def w0(self) -> float:
        """ Get or set the HEL beam waist """
        return self._w0

    @w0.setter
    def w0(self, w0: float = .15e3) -> None:
        self._w0 = w0
    # ==========================================================================

    # ==========================================================================
    @property
    def r0(self) -> float:
        """ Get or set the HEL beam waist distance """
        return self._r0

    @r0.setter
    def r0(self, r0: float = 1.0) -> None:
        self._r0 = r0
    # ==========================================================================

    # ==========================================================================
    @property
    def x0(self) -> Tuple[float, float, float]:
        """ Get or set the HEL initial position """
        return self._x0

    @x0.setter
    def x0(self, x0: Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:
        self._x0 = x0
    # ==========================================================================

    # ==========================================================================
    @property
    def mode(self) -> Tuple[float, float]:
        """ Get or set the HEL mode """
        return self._mode

    @mode.setter
    def mode(self, mode: Tuple[float, float] = (0.0, 0.0)) -> None:
        self._mode = mode
    # ==========================================================================





if __name__ == "__main__":
    HEL1 = HEL()
    print(HEL1.wavelength)
    print(HEL1.pulse_params)
    HEL1.pulse_params = ("T", 3.6)
    print(HEL1.pulse_params)
    HEL1.pulse_params = ("T", 3.6)
    print(HEL1.pulse_params)
    print(HEL1.get_count())
    HEL2 = HEL()
    print(HEL.get_count())
    del HEL2
    print(HEL.get_count())