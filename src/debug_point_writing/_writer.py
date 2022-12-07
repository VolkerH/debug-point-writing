"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/stable/plugins/guides.html?#writers

Replace code below according to your needs.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Sequence, Tuple, Union

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def write_single_points_layer(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single image layer"""

    # Pretend we're writing something but just print to console
    print("In point writer, trying to write ", path)

    # return path to any file(s) that were successfully written
    return [path]
