# Rive control for Flet

`Rive` control for Flet.

## Usage

Add `flet-rive` as dependency (`pyproject.toml` or `requirements.txt`) to your Flet project.

## Example

```py

import flet as ft

import flet_rive as fr

def main(page):
    page.add(
        fr.Rive(
            "https://cdn.rive.app/animations/vehicles.riv",
            placeholder=ft.ProgressBar(),
            width=300,
            height=200,
        )
    )

ft.app(main)
```