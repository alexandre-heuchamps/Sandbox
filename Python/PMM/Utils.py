import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from xml.etree import ElementTree as ET

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

# ==============================================================================
def get_tree(file: str = "./Drone_Flight_Path.kml") -> ET:
    """ Get the tree corresponding to the file, passed as a string

    Parameters
    ----------
    file: <class 'str'> (default: "./Drone_Flight_Path.kml")
        File containing all the data

    Returns
    -------
    _: <class 'xml.etree.ElementTree.ElementTree'>
        Tree containing all the data """
    return ET.parse(file)
# ==============================================================================

# ==============================================================================
def get_root(tree: ET) -> ET.Element:
    """ Returns the root of the tree passed as input

    Parameters
    ----------
    tree: <class 'xml.etree.ElementTree.ElementTree'>
        Tree from which the root is extracted

    Returns
    -------
    _: <class 'xml.etree.ElementTree.Element'>
        Root of the tree """
    return tree.getroot()
# ==============================================================================

# ==============================================================================
def get_namespaces(root: ET.Element) -> dict:
    """ Returns the namespace used by the .kml file containing the path
    coordinates

    Parameters
    ----------
    root: <class 'xml.etree.ElementTree.Element'>
        Tree root from which coordinates are extracted

    Returns
    -------
    _: <class 'dict'>
        Dictionnary containing the file namespace """
    namespace_uri = root.tag.split("}")[0][1:]
    return {"kml": f"{namespace_uri}"}
# ==============================================================================

# ==============================================================================
def create_kml_path(*places: tuple):
    """ Concatenates strings to meet the specific format
    .//kml:PLACE1/kml:PLACE2/kml:PLACE3
    where PLACE1, PLACE2, PLACE3, etc. are the strings contained in *places

    Parameters
    ----------
    places: <class 'tuple'>
        List of strings used to create the correct path to search in the file

    Returns
    -------
    _: <class 'str'>
        Path to search for in the kml file """
    return ".//" + "/".join(f"kml:{place}" for place in places)
# ==============================================================================

# ==============================================================================
def get_coordinates(root: ET.Element,
                        is_big: bool = True,
                        kw: str = "coordinates",
                        *strings: str,
                    ) -> tuple:
    """ Returns the path coordinates stored in the file corresponding to the
    input root. Depending on the parameter 'is_big', one method or another
    is used: is True, the structure of the file is assumed to be known and
    contained in 'strings', so the coordinates are taken directly from the
    correct location. If False, the stucture is not take for granted,
    and an iteration is performed on all elements up to the first appearrance
    of the 'kw' parameter to get the desired data

    Parameters
    ----------
    root: <class 'xml.etree.ElementTree.Element'>
        Tree root from which coordinates are extracted
    is_big: <class 'bool'> (default: True)
        Tells if the kml file is big or not. If not, the structure is not
        assumed, and the whole file is iterated to extract the desired
        coordinates. If True, the structure is assumed, and the coordinates are
        expected to be strored under the concatenation of *strings
    *strings: <class 'str'>
        Structure where to look

    Returns
    -------
    _: <class 'list', class 'list', class 'list'>
        Path coordinates (x, y, and z) """

    if is_big is True:
        path = create_kml_path(*strings)
        return get_coordinates_assumed(root = root, path = path)
    else:
        return get_coordinates_iter(root = root, kw = kw)
# ==============================================================================

# ==============================================================================
def get_coordinates_assumed(root: ET.Element, path: str) -> tuple:
    """ Returns the path coordinates stored in the file corresponding to the
    input root, using the string contained in 'path' input

    Parameters
    ----------
    root: <class 'xml.etree.ElementTree.Element'>
        Tree root from which coordinates are extracted
    path: <class 'str'>
        Structure where to look

    Returns
    -------
    _: <class 'list', class 'list', class 'list'>
        Path coordinates (x, y, and z) """
    namespace = get_namespaces(root = root)
    xyz = root.find(path, namespace)
    xyz = xyz.text
    xyz = xyz.split()

    x = []
    y = []
    z = []
    for coords in xyz:
        data = coords.split(",")
        x.append( float(data[0]) )
        y.append( float(data[1]) )
        z.append( float(data[2]) )

    return x, y, z
# ==============================================================================

# ==============================================================================
def get_coordinates_iter(root: ET.Element, kw: str = "coordinates") -> tuple:
    """ Returns the path coordinates stored in the file corresponding to the
    input root by iterating ove all tags, up to the first appearance of the
    'kw' input

    Parameters
    ----------
    root: <class 'xml.etree.ElementTree.Element'>
        Tree root from which coordinates are extracted
    kw: <class 'str'>
        Keyword to look for to get the coordinates

    Returns
    -------
    _: <class 'list', class 'list', class 'list'>
        Path coordinates (x, y, and z) """
    x = []
    y = []
    z = []

    for elem in root.iter():
        if kw in elem.tag:
            for coord in elem.text.split():
                lon, lat, alt = map(float, coord.split(','))
                x.append(float(lon))
                y.append(float(lat))
                z.append(float(alt))

    return x, y, z
# ==============================================================================

# ==============================================================================
def get_bounding_box(x: list, y: list, z:list) -> None:
    """ Gets the bounding point coordinates for the loaded .kml file

    Parameters
    ----------
    x: <class 'list'>
        List of x coordinates
    y: <class 'list'>
        List of y coordinates
    z: <class 'list'>
        List of z coordinates

    Returns
    -------
    xmin: <class 'float'>
        Minimum x coordinate
    ymin: <class 'float'>
        Minimum y coordinate
    zmin: <class 'float'>
        Minimum z coordinate
    xmax: <class 'float'>
        Maximum x coordinate
    ymax: <class 'float'>
        Maximum y coordinate
    zmax: <class 'float'>
        Maximum z coordinate """
    xmin: float = np.min(x)
    ymin: float = np.min(y)
    zmin: float = np.min(z)
    xmax: float = np.max(x)
    ymax: float = np.max(y)
    zmax: float = np.max(z)
    return xmin, ymin, zmin, xmax, ymax, zmax
# ==============================================================================

# ==============================================================================
def get_bounding_volume(xmin: float, ymin: float, zmin:float,
                            xmax: float, ymax: float, zmax:float
                        ) -> float:
    """ Computes the volume of the bounding box around the loaded coordinates

    Parameters
    ----------
    xmin: <class 'float'>
        Minimum x coordinate
    ymin: <class 'float'>
        Minimum y coordinate
    zmin: <class 'float'>
        Minimum z coordinate
    xmax: <class 'float'>
        Maximum x coordinate
    ymax: <class 'float'>
        Maximum y coordinate
    zmax: <class 'float'>
        Maximum z coordinate

    Returns
    -------
    _: <class 'float'>
        Volume of the bounding box """
    return ((xmax - xmin) * (ymax - ymin) * (zmax - zmin))
# ==============================================================================

# ==============================================================================
def sec(x: float) -> float:
    return (1 / np.cos(x))
# ==============================================================================

# ==============================================================================
# https://github.com/openstreetmap/svn-archive/blob/main/applications/routing/pyroute/tilenames.py
def latlon2relativeXY(lon: float, lat: float) -> tuple:
    x = (lon + 180) / 360
    y = (1 - np.log(np.tan(np.deg2rad(lat)) + sec(np.deg2rad(lat))) / np.pi) / 2
    return x, y
# ==============================================================================

# ==============================================================================
# To convert longitude and latitude to X and Y, a map projection is needed.
# The most common one is the Mercator projection
def lonlat_to_xy(lon: float, lat: float):
    R = 6378137  # Earth radius in meters
    # R = 1.0  # Earth radius in meters
    x = R * np.deg2rad(lon)
    y = R * np.log(np.tan(np.pi / 4 + np.deg2rad(lat) / 2))
    return x, y
# ==============================================================================

def fromGeographic(self, lat, lon):
    radius = 6378137.
    lat = np.deg2rad(lat)
    lon = np.deg2rad(lon)
    B = np.sin(lon) * np.cos(lat)
    x = 0.5 * radius * np.log((1.+B)/(1.-B))
    y = radius * ( np.arctan(np.tan(lat)/np.cos(lon)) - lat )
    return (x, y, 0.)



import math

# Constants for the WGS84 ellipsoid
a = 6378137.0        # semi-major axis
f = 1 / 298.257223563 # flattening
b = a * (1 - f)      # semi-minor axis

def latlon_to_xyz(lat, lon, alt):
    # Convert latitude and longitude to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Calculate prime vertical radius of curvature
    N = a / math.sqrt(1 - (2*f - f*f) * math.sin(lat_rad)**2)

    # Calculate Cartesian coordinates
    x = (N + alt) * math.cos(lat_rad) * math.cos(lon_rad)
    y = (N + alt) * math.cos(lat_rad) * math.sin(lon_rad)
    z = ((b**2 / a**2) * N + alt) * math.sin(lat_rad)

    return x, y, z
