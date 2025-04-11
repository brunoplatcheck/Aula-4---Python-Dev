import flet as ft

def main(page):
    title = ft.Text("Hashzap")

    chat = ft.Column()

    user_name = ft.TextField(label="Enter your name")

    def receive_message_tunnel(message):
        message_type = message["type"]
        if message_type == "message":
            message_text = message["text"]
            message_user = message["user"]
            chat.controls.append(ft.Text(f"{message_user}: {message_text}"))
        else:
            message_user = message["user"]
            chat.controls.append(ft.Text(f"{message_user} joined the chat",
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        page.update()

    page.pubsub.subscribe(receive_message_tunnel)

    def send_message(event):
        page.pubsub.send_all({
            "text": message_field.value,
            "user": user_name.value,
            "type": "message"
        })
        message_field.value = ""
        page.update()

    message_field = ft.TextField(label="Type a message", on_submit=send_message)
    send_button = ft.ElevatedButton("Send", on_click=send_message)

    def enter_popup(event):
        page.pubsub.send_all({"user": user_name.value, "type": "join"})
        page.add(chat)
        popup.open = False
        page.remove(start_button)
        page.remove(title)
        page.add(ft.Row([message_field, send_button]))
        page.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Welcome to Hashzap"),
        content=user_name,
        actions=[ft.ElevatedButton("Join", on_click=enter_popup)],
    )

    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Start chat", on_click=start_chat)

    page.add(title)
    page.add(start_button)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

