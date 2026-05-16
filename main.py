import flet as ft

def main(page: ft.Page):
    # --- [1] إعدادات اللعبة ---
    page.title = "Future Doctor Adventure"
    page.theme_mode = ft.ThemeMode.DARK  
    page.window_width = 400
    page.window_height = 800
    page.padding = 20

    # --- [2] الموسيقى (رابط تجريبي يعمل مباشرة) ---
    audio1 = ft.Audio(
        src="https://luan72.github.io/files/audio/ambient_c_motion.mp3",
        autoplay=False,
    )
    page.overlay.append(audio1)

    # --- [3] منطق اللعبة والتنقل ---
    score = 0
    level = 1

    def start_game(e):
        name = name_input.value.strip()
        if not name:
            name_input.error_text = "اكتب اسمك يا بطل!"
            page.update()
            return

        # مسح الشاشة وبناء واجهة اللعبة
        page.controls.clear()
        page.snack_bar = ft.SnackBar(ft.Text(f"مرحباً دكتور {name}! استعد للمغامرة"), open=True)

        def play_action(e_action):
            nonlocal score, level
            score += 10
            if score % 100 == 0: 
                level += 1
            score_text.value = f"Score: {score}"
            level_text.value = f"Level: {level}"
            page.update()

        score_text = ft.Text("Score: 0", size=30, weight="bold", color="yellow")
        level_text = ft.Text("Level: 1", size=20, color="white")

        # واجهة اللعبة داخل حاوية بالخلفية الجديدة
        game_ui = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.PERSON_OUTLINED, color="blue", size=20), # تم تصحيح الأيقونة هنا
                    ft.Text(f"اللاعب: {name}", size=16, color="blue", weight="bold"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                score_text,
                level_text,
                ft.Divider(),
                # تم تصحيح طريقة كتابة ElevatedButton هنا في كل الأزرار
                ft.ElevatedButton("War Section", on_click=play_action, width=250, bgcolor="red", color="white"),
                ft.ElevatedButton("Doctor Section", on_click=play_action, width=250, bgcolor="blue", color="white"),
                ft.ElevatedButton("Care Section", on_click=play_action, width=250, bgcolor="green", color="white"),
                ft.ElevatedButton("Race Section", on_click=play_action, width=250, bgcolor="orange", color="white"),
                ft.Divider(),
                ft.Row([
                    ft.IconButton(ft.icons.MUSIC_NOTE, on_click=lambda _: audio1.play()),
                    ft.IconButton(ft.icons.MUSIC_OFF, on_click=lambda _: audio1.pause()),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment="center"),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center, 
                end=ft.alignment.bottom_center, 
                colors=["#1a1a2e", "#16213e"]
            ),
            padding=30,
            border_radius=20,
        )
        
        page.add(game_ui)
        page.update()

    # --- [4] شاشة التسجيل الأولى ---
    name_input = ft.TextField(label="اسم اللاعب", width=300, border_radius=10)
    phone_input = ft.TextField(label="رقم الهاتف (اختياري)", width=300, border_radius=10)
    
    page.add(
        ft.Column([
            ft.Icon(ft.icons.LOCAL_HOSPITAL, size=100, color="blue"),
            ft.Text("Future Doctor Registration", size=25, weight="bold"),
            ft.Divider(),
            name_input,
            phone_input,
            ft.ElevatedButton("بدء المغامرة الآن", on_click=start_game, width=250, height=50), # تم تصحيحها هنا أيضاً
        ], horizontal_alignment="center")
    )

# تشغيل التطبيق (استخدمنا flet.app العادية لأنها الأفضل لتجربتك الحالية)
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")