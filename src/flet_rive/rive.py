from dataclasses import field
from typing import Dict, List, Optional

import flet as ft

__all__ = ["Rive"]


@ft.control("Rive")
class Rive(ft.ConstrainedControl):
    """
    Displays rive animations.
    """

    src: str
    """
    The source of your rive animation. 
    Can either be a URL or a path to a local asset file.
    """

    placeholder: Optional[ft.Control] = None
    """
    Control displayed while the Rive is loading.
    """

    artboard: Optional[str] = None
    """
    The name of the artboard to use. 
    If not specified, the default artboard of the provided `src` is used.
    """

    alignment: Optional[ft.Alignment] = None
    """
    Alignment for the animation in the Rive control.
    """

    enable_antialiasing: bool = True
    """
    Whether to enable anti-aliasing when rendering.
    
    Defaults to `True`.
    """

    use_artboard_size: bool = False
    """
    Determines whether to use the inherent size of the artboard, 
    i.e. the absolute size defined by the artboard, 
    or size the control based on the available constraints only (sized by parent).
    
    Defaults to `False`.
    """

    fit: Optional[ft.BoxFit] = None
    """
    The animation's fit.
    """

    speed_multiplier: ft.Number = 1.0
    """
    A multiplier for controlling the speed of the Rive animation playback.
    
    Defaults to `1.0`.
    """

    animations: List[str] = field(default_factory=list)
    """
    List of animations to play; default animation is played if empty.
    
    Defaults to `[]`.
    """

    state_machines: List[str] = field(default_factory=list)
    """
    List of state machines to play; none will play if empty.
    
    Defaults to `[]`.
    """

    headers: Optional[Dict[str, str]] = None
    """
    Headers for network requests.
    """

    clip_rect: Optional[ft.Rect] = None
    """
    Clip the artboard to this rect.
    
    If not supplied it'll default to the constraint size provided by the parent widget. 
    Unless the Artboard has clipping disabled, then no clip will be applied.
    """
