from dataclasses import field
from typing import Optional, List

import flet as ft

__all__ = ["Rive"]


@ft.control("Rive")
class Rive(ft.ConstrainedControl):
    """
    Displays rive animations.

    -----

    Online docs: https://flet.dev/docs/controls/rive
    """

    src: str
    placeholder: Optional[ft.Control] = None
    artboard: Optional[str] = None
    alignment: Optional[ft.Alignment] = None
    enable_antialiasing: bool = True
    use_artboard_size: bool = False
    fit: Optional[ft.ImageFit] = None
    speed_multiplier: ft.Number = 1.0
    animations: List[str] = field(default_factory=list)
    state_machines: List[str] = field(default_factory=list)
