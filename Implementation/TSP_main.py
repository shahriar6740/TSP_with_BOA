import argparse
import numpy as np
from utilities import Utilities as util
from constants import Constants
from butterfly import Butterfly as BOA


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("5", help="display a square of a given number", type=int)
    args = parser.parse_args()

