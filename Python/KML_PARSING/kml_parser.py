import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from xml.etree import ElementTree as ET



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



def get_coordinates(root: ET.Element,
                        is_big: bool = True,
                        kw: str = "coordinates",
                        *strings: str,
                    ) -> list | list | list:
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



def get_coordinates_assumed(root: ET.Element,
                                path: str
                            ) -> list | list | list:
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



def get_coordinates_iter(root: ET.Element,
                            kw: str = "coordinates"
                        ) -> list | list | list:
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





if __name__ == "__main__":
    tree = get_tree()
    root = get_root(tree)
    x, y, z = get_coordinates(root,
                                True,
                                "Placemark",
                                "Polygon",
                                "outerBoundaryIs",
                                "LinearRing",
                                "coordinates"
                            )

    x, y, z = get_coordinates(root,
                                False,
                                "coordinates"
                            )

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()
    # ".//kml:Placemark/kml:Polygon/kml:outerBoundaryIs/kml:LinearRing/kml:coordinates"