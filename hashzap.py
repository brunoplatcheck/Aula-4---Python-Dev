import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Hashzap"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "stretch"
    page.padding = 0

    # Theme colors
    primary_color = ft.colors.TEAL
    secondary_color = ft.colors.WHITE
    accent_color = ft.colors.TEAL_ACCENT_400

    # Global state
    chats_data = []
    current_user = ft.TextField()
    chat_list_view = ft.Column()

    def create_message(text: str, user: str, is_current_user: bool):
        return ft.Container(
            content=ft.Column([
                ft.Text(user, size=12, weight="bold", color=ft.colors.GREY_600),
                ft.Text(text, size=14),
                ft.Text(
                    datetime.now().strftime("%H:%M"),
                    size=10,
                    color=ft.colors.GREY_500,
                    text_align=ft.TextAlign.END
                )
            ]),
            bgcolor=ft.colors.WHITE if is_current_user else ft.colors.GREY_100,
            border_radius=10,
            padding=10,
            margin=5,
            alignment=ft.alignment.top_left,
            border=ft.border.all(1, ft.colors.GREY_300),
            animate_opacity=300,
            width=300,
            wrap=True
        )

    def build_main_screen():
        page.clean()
        chat_list_view.controls = []

        for chat in chats_data:
            chat_list_view.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(chat["name"]),
                        subtitle=ft.Text(f"{len(chat['messages'])} messages"),
                        on_click=lambda e, chat=chat: open_chat(chat)
                    ),
                    elevation=2,
                    margin=10
                )
            )

        page.add(
            ft.Column(
                [
                    ft.Container(
                        ft.Row(
                            [ft.Text("Hashzap", size=24, weight="bold", color=secondary_color)],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        bgcolor=primary_color,
                        padding=15
                    ),
                    chat_list_view,
                    ft.Container(
                        ft.ElevatedButton(
                            "Create Chat",
                            on_click=open_name_dialog,
                            bgcolor=primary_color,
                            color=secondary_color,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20)
                        ),
                        alignment=ft.alignment.center,
                        padding=20
                    )
                ],
                expand=True
            )
        )
        page.update()

    def open_name_dialog(e):
        name_field.value = ""
        name_dialog.open = True
        page.dialog = name_dialog
        page.update()

    def create_new_chat(e):
        if not name_field.value.strip():
            name_field.error_text = "Please enter your name"
            page.update()
            return
        name_dialog.open = False
        current_user.value = name_field.value
        new_chat = {"name": f"Chat with {current_user.value}", "messages": []}
        chats_data.append(new_chat)
        open_chat(new_chat)

    def open_chat(chat):
        page.clean()

        chat_area = ft.ListView(
            expand=True,
            spacing=8,
            padding=20,
            auto_scroll=True
        )

        for msg in chat["messages"]:
            chat_area.controls.append(
                ft.Row(
                    [create_message(msg["text"], msg["user"], msg["user"] == current_user.value)],
                    alignment=(ft.MainAxisAlignment.END if msg["user"] == current_user.value else ft.MainAxisAlignment.START)
                )
            )

        message_input = ft.TextField(
            hint_text="Type a message...",
            border_radius=20,
            border_color=primary_color,
            focused_border_color=accent_color,
            expand=True,
            multiline=True,
            min_lines=1,
            max_lines=5
        )

        def send_message(e):
            if message_input.value.strip() == "":
                return
            msg = {
                "text": message_input.value,
                "user": current_user.value,
                "time": datetime.now().strftime("%H:%M")
            }
            chat["messages"].append(msg)
            chat_area.controls.append(
                ft.Row(
                    [create_message(msg["text"], msg["user"], True)],
                    alignment=ft.MainAxisAlignment.END
                )
            )
            message_input.value = ""
            page.update()

        page.add(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text(chat["name"], size=20, weight="bold", color=secondary_color),
                        ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color=secondary_color, on_click=lambda _: build_main_screen())
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                bgcolor=primary_color,
                padding=15
            ),
            ft.Container(chat_area, expand=True, bgcolor=ft.colors.GREY_200),
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(ft.icons.ADD, icon_color=primary_color),
                        message_input,
                        ft.IconButton(
                            ft.icons.SEND_ROUNDED,
                            on_click=send_message,
                            icon_color=primary_color,
                            bgcolor=accent_color
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.END
                ),
                bgcolor=secondary_color,
                padding=10
            )
        )

    # Name entry dialog
    name_field = ft.TextField(label="Your name", autofocus=True)
    name_dialog = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Enter your name"),
        content=ft.Column([name_field], tight=True),
        actions=[ft.TextButton("Start Chat", on_click=create_new_chat)],
        actions_alignment="end"
    )

    # Initial screen
    build_main_screen()

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
