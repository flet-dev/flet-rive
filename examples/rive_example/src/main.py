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
