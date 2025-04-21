from dataclasses import field
from typing import List, Optional

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
    placeholder: ft.OptionalControl = None
    artboard: Optional[str] = None
    alignment: ft.OptionalAlignment = None
    enable_antialiasing: bool = True
    use_artboard_size: bool = False
    fit: Optional[ft.ImageFit] = None
    speed_multiplier: ft.Number = 1.0
    animations: List[str] = field(default_factory=list)
    state_machines: List[str] = field(default_factory=list)
