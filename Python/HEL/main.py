from src.body.Simulator import Simulator
from src.body.World import World
from src.parser.CLParser import CLParser



if __name__ == "__main__":
    cl = CLParser()
    w = World()
    sim = Simulator(cl_parser = cl, world = w)