from synthetic_data_generator.scripts.geometric_primitives.ORing import ORing
from synthetic_data_generator.scripts.geometric_primitives.ThroughHole import ThroughHole
from synthetic_data_generator.scripts.geometric_primitives.BlindHole import BlindHole
from synthetic_data_generator.scripts.geometric_primitives.TriangularPassage import TriangularPassage
from synthetic_data_generator.scripts.geometric_primitives.RectangularPassage import RectangularPassage
from synthetic_data_generator.scripts.geometric_primitives.TriangularPocket import TriangularPocket
from synthetic_data_generator.scripts.geometric_primitives.RectangularPocket import RectangularPocket
from synthetic_data_generator.scripts.geometric_primitives.CircularThroughSlot import CircularThroughSlot
from synthetic_data_generator.scripts.geometric_primitives.TriangularThroughSlot import TriangularThroughSlot
from synthetic_data_generator.scripts.geometric_primitives.RectangularTroughSlot import RectangularTroughSlot
from synthetic_data_generator.scripts.geometric_primitives.RectangularBlindSlot import RectangularBlindSlot
from synthetic_data_generator.scripts.geometric_primitives.CircularEndPocket import CircularEndPocket
from synthetic_data_generator.scripts.geometric_primitives.TriangularBlindStep import TriangularBlindStep
from synthetic_data_generator.scripts.geometric_primitives.CircularBlindStep import CircularBlindStep
from synthetic_data_generator.scripts.geometric_primitives.RectangularBlindStep import RectangularBlindStep
from synthetic_data_generator.scripts.geometric_primitives.RectangularTroughStep import RectangularTroughStep
from synthetic_data_generator.scripts.geometric_primitives.TwoSideThroughStep import TwoSideThroughStep
from synthetic_data_generator.scripts.geometric_primitives.SlantedThroughStep import SlantedThroughStep
from synthetic_data_generator.scripts.geometric_primitives.Chamfer import Chamfer
from synthetic_data_generator.scripts.geometric_primitives.Round import Round
from synthetic_data_generator.scripts.geometric_primitives.VerticalCircularEndBlindSlot import \
    VerticalCircularEndBlindSlot
from synthetic_data_generator.scripts.geometric_primitives.HorizontalCircularEndBlindSlot import \
    HorizontalCircularEndBlindSlot
from synthetic_data_generator.scripts.geometric_primitives.SixSidePassage import SixSidePassage
from synthetic_data_generator.scripts.geometric_primitives.SixSidePocket import SixSidePocket


class MachiningFeature:
    def __init__(self, machining_feature_id, limit):
        self.machining_feature_id = machining_feature_id
        self.limit = limit
        self.machining_feature = [ORing, ThroughHole, BlindHole, TriangularPassage, RectangularPassage,
                                  CircularThroughSlot, TriangularThroughSlot, RectangularTroughSlot,
                                  RectangularBlindSlot, TriangularPocket, RectangularPocket, CircularEndPocket,
                                  TriangularBlindStep, CircularBlindStep, RectangularBlindStep, RectangularTroughStep,
                                  TwoSideThroughStep, SlantedThroughStep, Chamfer, Round, VerticalCircularEndBlindSlot,
                                  HorizontalCircularEndBlindSlot, SixSidePassage, SixSidePocket]

    def create(self):
        return self.machining_feature[self.machining_feature_id](self.limit).transformation()
