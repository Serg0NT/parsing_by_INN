import flet as ft


def main(page: ft.Page):
    page.title = "Сбор ифномрации о компаниях по ИНН"
    page.appbar = ft.AppBar(title=ft.Text(value="Выбор файла",
                                          color="red",
                                          weight=ft.FontWeight.BOLD,
                                          italic=True
                                          ),
                            bgcolor="blue",
                            )

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Ничего не выбрано"
        )
        selected_files.update()
        pth = ", ".join(map(lambda f: f.path, e.files)) if e.files else "Ничего не выбрано"
        print(pth)
        print(selected_files.value, type(selected_files.value))

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text(weight=ft.FontWeight.BOLD)

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Выберите файл с ИНН",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        dialog_title="Выбор файла",
                        # allow_multiple=True,
                    ),
                ),
                selected_files,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # page.title = "Flet counter example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #
    # txt_number = ft.TextField(text_align=ft.TextAlign.RIGHT, width=100)
    #
    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()
    #
    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()
    #
    # page.add(
    #     ft.Row(
    #         [
    #             ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             ft.IconButton(ft.Icons.ADD, on_click=plus_click),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )


ft.app(main)
