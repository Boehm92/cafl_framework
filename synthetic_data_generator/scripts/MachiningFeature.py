from machining_feature_primitives.ORing import ORing
from machining_feature_primitives.ThroughHole import ThroughHole
from machining_feature_primitives.BlindHole import BlindHole
from machining_feature_primitives.TriangularPassage import TriangularPassage
from machining_feature_primitives.RectangularPassage import RectangularPassage
from machining_feature_primitives.TriangularPocket import TriangularPocket
from machining_feature_primitives.RectangularPocket import RectangularPocket
from machining_feature_primitives.CircularThroughSlot import CircularThroughSlot
from machining_feature_primitives.TriangularThroughSlot import TriangularThroughSlot
from machining_feature_primitives.RectangularTroughSlot import RectangularTroughSlot
from machining_feature_primitives.RectangularBlindSlot import RectangularBlindSlot
from machining_feature_primitives.CircularEndPocket import CircularEndPocket
from machining_feature_primitives.TriangularBlindStep import TriangularBlindStep
from machining_feature_primitives.CircularBlindStep import CircularBlindStep
from machining_feature_primitives.RectangularBlindStep import RectangularBlindStep
from machining_feature_primitives.RectangularTroughStep import RectangularTroughStep
from machining_feature_primitives.TwoSideThroughStep import TwoSideThroughStep
from machining_feature_primitives.SlantedThroughStep import SlantedThroughStep
from machining_feature_primitives.Chamfer import Chamfer
from machining_feature_primitives.Round import Round
from machining_feature_primitives.VerticalCircularEndBlindSlot import VerticalCircularEndBlindSlot
from machining_feature_primitives.HorizontalCircularEndBlindSlot import HorizontalCircularEndBlindSlot
from machining_feature_primitives.SixSidePassage import SixSidePassage
from machining_feature_primitives.SixSidePocket import SixSidePocket


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
