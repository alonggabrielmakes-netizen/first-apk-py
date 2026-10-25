import flet as ft

def main(page: ft.Page):
    page.title = "My First Flet App"
    page.window_width = 400
    page.window_height = 700
    
    txt = ft.Text(value="Hello, Flet! 🎉", size=24, weight=ft.FontWeight.BOLD)
    txt_input = ft.TextField(hint_text="Type something here...", width=300)
    
    def btn_click(e):
        if txt_input.value:
            txt.value = f"You said: {txt_input.value}"
            txt_input.value = ""
            page.update()
    
    btn = ft.ElevatedButton("Click Me!", on_click=btn_click, bgcolor=ft.colors.BLUE_600, color=ft.colors.WHITE)
    
    page.add(
        ft.Column(
            [txt, txt_input, btn],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

