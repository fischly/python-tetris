from tetris.engine.abcs import RotationSystem
from tetris.types import KickTable
from tetris.types import PieceType


class SRS(RotationSystem):
    shapes = {
        PieceType.I: [
            ((1, 0), (1, 1), (1, 2), (1, 3)),
            ((0, 2), (1, 2), (2, 2), (3, 2)),
            ((2, 0), (2, 1), (2, 2), (2, 3)),
            ((0, 1), (1, 1), (2, 1), (3, 1)),
        ],
        PieceType.L: [
            ((0, 2), (1, 0), (1, 1), (1, 2)),
            ((0, 1), (1, 1), (2, 1), (2, 2)),
            ((1, 0), (1, 1), (1, 2), (2, 0)),
            ((0, 0), (0, 1), (1, 1), (2, 1)),
        ],
        PieceType.J: [
            ((0, 0), (1, 0), (1, 1), (1, 2)),
            ((0, 1), (0, 2), (1, 1), (2, 1)),
            ((1, 0), (1, 1), (1, 2), (2, 2)),
            ((0, 1), (1, 1), (2, 0), (2, 1)),
        ],
        PieceType.S: [
            ((0, 1), (0, 2), (1, 0), (1, 1)),
            ((0, 1), (1, 1), (1, 2), (2, 2)),
            ((1, 1), (1, 2), (2, 0), (2, 1)),
            ((0, 0), (1, 0), (1, 1), (2, 1)),
        ],
        PieceType.Z: [
            ((0, 0), (0, 1), (1, 1), (1, 2)),
            ((0, 2), (1, 1), (1, 2), (2, 1)),
            ((1, 0), (1, 1), (2, 1), (2, 2)),
            ((0, 1), (1, 0), (1, 1), (2, 0)),
        ],
        PieceType.T: [
            ((0, 1), (1, 0), (1, 1), (1, 2)),
            ((0, 1), (1, 1), (1, 2), (2, 1)),
            ((1, 0), (1, 1), (1, 2), (2, 1)),
            ((0, 1), (1, 0), (1, 1), (2, 1)),
        ],
        PieceType.O: [
            ((0, 1), (0, 2), (1, 1), (1, 2)),
            ((0, 1), (0, 2), (1, 1), (1, 2)),
            ((0, 1), (0, 2), (1, 1), (1, 2)),
            ((0, 1), (0, 2), (1, 1), (1, 2)),
        ],
    }

    @property
    def kicks(self) -> KickTable:
        default = {
            (0, 1): ((+0, -1), (-1, -1), (+2, +0), (+2, -1)),
            (0, 3): ((+0, +1), (-1, +1), (+2, +0), (+2, +1)),
            (1, 0): ((+0, +1), (+1, +1), (-2, +0), (-2, +1)),
            (1, 2): ((+0, +1), (+1, +1), (-2, +0), (-2, +1)),
            (2, 1): ((+0, -1), (-1, -1), (+2, +0), (+2, -1)),
            (2, 3): ((+0, +1), (-1, +1), (+2, +0), (+2, +1)),
            (3, 0): ((+0, -1), (+1, -1), (-2, +0), (-2, -1)),
            (3, 2): ((+0, -1), (+1, -1), (-2, +0), (-2, -1)),
            # 180 kicks
            (0, 2): (),
            (1, 3): (),
            (2, 0): (),
            (3, 1): (),
        }

        i_kicks = {
            (0, 1): ((+0, -1), (+0, +1), (+1, -2), (-2, +1)),
            (0, 3): ((+0, -1), (+0, +2), (-2, -1), (+1, +2)),
            (1, 0): ((+0, +2), (+0, -1), (-1, +2), (+2, -1)),
            (1, 2): ((+0, -1), (+0, +2), (-2, -1), (+1, +2)),
            (2, 1): ((+0, +1), (+0, -2), (+2, +1), (-1, +2)),
            (2, 3): ((+0, +2), (+0, -1), (-1, +2), (+2, -1)),
            (3, 0): ((+0, +1), (+0, -2), (+2, +1), (-1, -2)),
            (3, 2): ((+0, -2), (+0, +1), (+1, -2), (-2, +1)),
        }

        return {
            PieceType.I: default | i_kicks,
            PieceType.L: default,
            PieceType.J: default,
            PieceType.S: default,
            PieceType.Z: default,
            PieceType.T: default,
            PieceType.O: default,
        }


class TetrioSRS(SRS):
    @property
    def kicks(self) -> KickTable:
        override = {
            (0, 2): ((-1, +0), (-1, +1), (-1, -1), (+0, +1), (+0, -1)),
            (1, 3): ((+0, +1), (-2, +1), (-1, +1), (-2, +0), (-1, +0)),
            (2, 0): ((+1, +0), (+1, -1), (+1, +1), (+0, -1), (+0, +1)),
            (3, 1): ((+0, -1), (-2, -1), (-1, -1), (-2, +0), (-1, +0)),
        }

        return {k: v | override for k, v in super().kicks.items()}


class NoKicks(RotationSystem):
    kicks: KickTable = {
        i: {(i, j): tuple() for i in range(4) for j in range(4) if i != j}
        for i in PieceType
    }
