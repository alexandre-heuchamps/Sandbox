import numpy as np
import scipy as sp
from matplotlib import cm
import matplotlib.pyplot as plt
from HEL import HEL

class HELActions:
    """ A class to compute various HEL quantities """

    def __init__(self) -> None:
        pass

    def get_theta_diff(self, HEL) -> float:
        return HEL.wavelength / (np.pi * HEL.w0)

    def get_theta_M2(self, HEL) -> float:
        return (HEL.M2**2 - 1) * self.get_theta_diff(HEL)

    def get_theta_tot(self, HEL) -> float:
        return np.sqrt(self.get_theta_diff(HEL)**2 +  self.get_theta_M2(HEL)**2 + HEL.J**2)

    def get_spot_size(self, HEL, z: float) -> float:
        return 1.0

    def get_peak_irradiance(self, HEL) -> float:
        return 2.0 * HEL.P / (np.pi * HEL.w0)

    def irradiance(self, X, Y, z, HEL):
        wz = self.get_spot_size(HEL, z)
        Hm = sp.special.hermite(HEL.mode[0])(np.sqrt(2) * X / wz)
        Hn = sp.special.hermite(HEL.mode[1])(np.sqrt(2) * Y / wz)
        I0 = self.get_peak_irradiance(HEL)
        return I0 * (Hm**2) * (Hn**2) * np.exp(-2 * (X**2 + Y**2) / wz**2)


if __name__ == "__main__":
    r = 1.9
    x = np.linspace(start = -r, stop = r, num = 1000)
    y = np.linspace(start = -r, stop = r, num = 1000)
    X, Y = np.meshgrid(x, y, sparse = True)

    HEL = HEL()
    HEL.mode = (4, 6)
    z = 1.0
    I = HELActions().irradiance(X, Y, z, HEL)
    plt.contourf(x, y, I, cmap = cm.plasma)
    plt.colorbar()
    plt.show()