import flet as ft

# ════════════════════════════════════════════════════════════════
#   WEB PORTFOLIO  ·  Computer Programming I  ·  Semester 1 2026
#   Built with Flet Python Framework
# ════════════════════════════════════════════════════════════════

# ── COLOUR PALETTE ──────────────────────────────────────────────
BG_DARK   = "#080B14"
BG_CARD   = "#0F1323"
BG_CARD2  = "#141929"
NAV_BG    = "#05070F"
C_CYAN    = "#00E5FF"
C_PURPLE  = "#A855F7"
C_GOLD    = "#F59E0B"
C_GREEN   = "#10B981"
C_PINK    = "#EC4899"
C_WHITE   = "#F1F5F9"
C_GREY    = "#64748B"
C_BORDER  = "#1E2A4A"


def placeholder_box(label: str):
    return ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.DRIVE_FILE_RENAME_OUTLINE, color=C_GOLD, size=13),
            ft.Text(f"  {label}", color=C_GOLD, size=11, italic=True,
                    weight=ft.FontWeight.W_500, overflow=ft.TextOverflow.VISIBLE),
        ], tight=True),
        bgcolor="#1C1500", border=ft.Border.all(1.5, C_GOLD), border_radius=6,
        padding=ft.Padding.symmetric(horizontal=12, vertical=8),
        margin=ft.Margin.only(top=3, bottom=3),
    )


def section_header(text: str, color: str, icon=None):
    items = []
    if icon:
        items.append(ft.Icon(icon, color=color, size=22))
        items.append(ft.Container(width=10))
    items.append(ft.Text(text, size=18, weight=ft.FontWeight.BOLD, color=color))
    return ft.Column([
        ft.Row(items, tight=True),
        ft.Container(width=56, height=3, bgcolor=color,
                     border_radius=2, margin=ft.Margin.only(top=6, bottom=18)),
    ], spacing=0)


def gcard(content, pad=18, border_color=C_BORDER):
    return ft.Container(
        content=content,
        gradient=ft.LinearGradient(begin=ft.Alignment(-1,-1), end=ft.Alignment(1,1),
                                   colors=[BG_CARD, BG_CARD2]),
        border=ft.Border.all(1, border_color), border_radius=14, padding=pad,
    )


def tag_chip(label: str, bg: str, fg: str = "#080B14"):
    return ft.Container(
        content=ft.Text(label, size=9, color=fg, weight=ft.FontWeight.BOLD),
        bgcolor=bg, border_radius=4,
        padding=ft.Padding.symmetric(horizontal=7, vertical=3),
    )


# ════════════════════════════════════════════════════════════════
#   PAGE 0 — HOME
# ════════════════════════════════════════════════════════════════

def build_home():
    hero = ft.Container(
        content=ft.Column([
            ft.Text("COMPUTER PROGRAMMING I  ·  2026", size=10, color=C_CYAN, weight=ft.FontWeight.W_600),
            ft.Container(height=10),
            ft.Text("Elia Chitunga Ngurare Daniel", size=32, color=C_WHITE, weight=ft.FontWeight.BOLD),
            ft.Container(height=6),
            ft.Row([
                ft.Container(
                    content=ft.Text("Student No: 222126698", color=C_CYAN, size=12, weight=ft.FontWeight.W_500),
                    bgcolor="#041520", border=ft.Border.all(1, C_CYAN),
                    border_radius=20, padding=ft.Padding.symmetric(horizontal=16, vertical=5)),
                ft.Container(
                    content=ft.Text("Group: UNAM-I3691CP-Group7-CorroCheck", color=C_PURPLE, size=12, weight=ft.FontWeight.W_500),
                    bgcolor="#0C0520", border=ft.Border.all(1, C_PURPLE),
                    border_radius=20, padding=ft.Padding.symmetric(horizontal=16, vertical=5)),
            ], wrap=True, spacing=10),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
        gradient=ft.LinearGradient(begin=ft.Alignment(-1,-1), end=ft.Alignment(1,1),
                                   colors=["#040A1E", "#0D1540", "#120C30"]),
        border=ft.Border.all(1, "#1E2A5A"), border_radius=18, padding=30,
        alignment=ft.Alignment(0,0),
    )

    stats = ft.ResponsiveRow([
        ft.Column([ft.Container(
            content=ft.Column([
                ft.Text(num, size=26, weight=ft.FontWeight.BOLD, color=col),
                ft.Text(lbl, size=10, color=C_GREY, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
            bgcolor=bg, border=ft.Border.all(1, C_BORDER),
            border_radius=12, padding=16, alignment=ft.Alignment(0,0),
        )], col={"xs": 6, "md": 3}) for num, lbl, col, bg in [
            ("5",   "MATLAB Courses",  C_GOLD,   "#1A1100"),
            ("15%", "CA Weighting",    C_CYAN,   "#001A1C"),
            ("20+", "Commits Target",  C_GREEN,  "#001510"),
            ("100", "Mark Target",     C_PURPLE, "#100B20"),
        ]
    ], spacing=10)

    about_cards = ft.ResponsiveRow([
        ft.Column([gcard(ft.Column([
            ft.Row([ft.Icon(ft.Icons.PERSON, color=C_PURPLE, size=22),
                    ft.Text("  About Me", size=14, color=C_WHITE, weight=ft.FontWeight.BOLD)], tight=True),
            ft.Container(height=8),
            ft.Container(
                content=ft.Text(
                    "I am Elia Chitunga Ngurare Daniel, a Third-year Extended student studying at UNAM. "
                    "I am part of the CorroCheck group developing an engineering app. "
                    "I am interested in programming because it allows me to solve real-world problems in my field.",
                    size=11, color=C_GOLD, italic=True),
                bgcolor="#1C1500", border=ft.Border.all(1.5, C_GOLD), border_radius=6,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                margin=ft.Margin.only(top=3, bottom=3),
            ),
        ], spacing=4), border_color=f"{C_PURPLE}50")], col={"xs": 12, "md": 6}),

        ft.Column([gcard(ft.Column([
            ft.Row([ft.Icon(ft.Icons.FLAG, color=C_GREEN, size=22),
                    ft.Text("  My Goals", size=14, color=C_WHITE, weight=ft.FontWeight.BOLD)], tight=True),
            ft.Container(height=8),
            ft.Container(
                content=ft.Text("✅ Goal 1: Master Python functions and data structures", size=11, color=C_GOLD, italic=True),
                bgcolor="#1C1500", border=ft.Border.all(1.5, C_GOLD), border_radius=6,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                margin=ft.Margin.only(top=3, bottom=3),
            ),
            ft.Container(
                content=ft.Text("✅ Goal 2: Build a useful tool for my engineering module", size=11, color=C_GOLD, italic=True),
                bgcolor="#1C1500", border=ft.Border.all(1.5, C_GOLD), border_radius=6,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                margin=ft.Margin.only(top=3, bottom=3),
            ),
            ft.Container(
                content=ft.Text("✅ Goal 3: Achieve above 80% for this portfolio", size=11, color=C_GOLD, italic=True),
                bgcolor="#1C1500", border=ft.Border.all(1.5, C_GOLD), border_radius=6,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                margin=ft.Margin.only(top=3, bottom=3),
            ),
        ], spacing=4), border_color=f"{C_GREEN}50")], col={"xs": 12, "md": 6}),
    ], spacing=10)

    return ft.Column([hero, ft.Container(height=16), stats, ft.Container(height=16), about_cards],
                     scroll=ft.ScrollMode.AUTO, spacing=0)


# ════════════════════════════════════════════════════════════════
#   PAGE 1 — PROJECT TIMELINE
# ════════════════════════════════════════════════════════════════

def build_timeline():
    colors = [C_CYAN, C_PURPLE, C_GREEN, C_GOLD, C_PINK,
              C_CYAN, C_PURPLE, C_GREEN, C_GOLD, C_PINK]

    weekly_data = [
        {"text": "Week 1 — Installed GitHub, Flet, and Expo Go. Learned Figma basics for UI design. Set up development environment.", "hours": "6 hrs", "tag": "Setup"},
        {"text": "Week 2 — Designed the CorroCheck logo. Created multiple versions and presented to group. Finalized logo design.", "hours": "8 hrs", "tag": "Design"},
        {"text": "Week 3 — Observed team progress. Learned how backend and camera integration connects with UI design.", "hours": "4 hrs", "tag": "Observing"},
        {"text": "Week 4 — Designed the History Details Screen (Screen 8) in Figma. Created wireframes with photo, severity badge, and action buttons.", "hours": "10 hrs", "tag": "Design"},
        {"text": "Week 5 — Observed group progress. Reviewed team designs and provided UI feedback.", "hours": "4 hrs", "tag": "Review"},
        {"text": "Week 6 — Helped test design integration. Suggested UI improvements for better user experience.", "hours": "5 hrs", "tag": "Testing"},
        {"text": "Week 7 — Updated portfolio with MATLAB certificates and GitHub evidence.", "hours": "6 hrs", "tag": "Docs"},
        {"text": "Week 8 — Prepared final portfolio submission and deployed to web.", "hours": "5 hrs", "tag": "Deploy"},
        {"text": "Week 9 — Final polish and bug fixes.", "hours": "4 hrs", "tag": "Polish"},
        {"text": "Week 10 — Submitted final portfolio.", "hours": "3 hrs", "tag": "Submit"},
    ]

    def week_row(n, color, data):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Column([ft.Text(f"W{n}", size=12, color=BG_DARK, weight=ft.FontWeight.BOLD)],
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=color, border_radius=10, width=46, height=46, alignment=ft.Alignment(0,0)),
                ft.Container(width=14),
                ft.Column([
                    placeholder_box(data["text"]),
                    ft.Row([
                        tag_chip("⏱ Hours:", C_GREY, C_WHITE),
                        ft.Container(
                            content=ft.Text(data["hours"], color=color, size=11, weight=ft.FontWeight.W_600),
                            bgcolor=f"{color}18", border_radius=4,
                            padding=ft.Padding.symmetric(horizontal=8, vertical=3)),
                        ft.Container(content=ft.Text(f"Tag: {data['tag']}", color=C_GREY, size=10, italic=True)),
                    ], tight=True, spacing=6),
                ], expand=True, spacing=6),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=BG_CARD, border=ft.Border.all(1, C_BORDER), border_radius=12, padding=14,
        )

    weeks = [week_row(i + 1, colors[i], weekly_data[i]) for i in range(10)]
    tip = ft.Container(
        content=ft.Text("💡 Weekly log of my contributions to the CorroCheck project", color=C_GOLD, size=11, italic=True),
        padding=ft.Padding.only(top=4, left=4))

    return ft.Column([
        section_header("PROJECT TIMELINE", C_CYAN, ft.Icons.TIMELINE),
        ft.Text("My specific weekly contributions — what I built and designed for the team.", size=13, color=C_GREY),
        ft.Container(height=16),
        *weeks, tip,
    ], scroll=ft.ScrollMode.AUTO, spacing=8)


# ════════════════════════════════════════════════════════════════
#   PAGE 2 — MATLAB ACHIEVEMENT HUB
# ════════════════════════════════════════════════════════════════

def build_matlab():
    courses = [
        ("MATLAB Onramp",
         "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=886f3cd0-3581-4d81-a050-0cc6d5122c90&"),
        ("Simulink Onramp",
         "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=29573ead-2619-408e-bdaa-be64133501e8&"),
        ("Make and Manipulate Matrices",
         "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=63c9495c-8b21-4fef-ab9b-b09435ef591f&"),
        ("Explore Data with MATLAB Plots",
         "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=17457a9c-e900-48c2-86b0-de5cdc64bc92&"),
        ("Calculations with Vectors and Matrices",
         "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=4da1249e-cebc-4d91-8aaf-17c84d6b18aa&"),
    ]

    def cert_card(n, name, url):
        return ft.Column([ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Text(str(n), size=14, color=BG_DARK, weight=ft.FontWeight.BOLD),
                        bgcolor=C_GOLD, border_radius=50, width=30, height=30, alignment=ft.Alignment(0,0)),
                    ft.Container(width=10),
                    ft.Text(name, size=12, color=C_WHITE, weight=ft.FontWeight.W_600, expand=True),
                    ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=C_GOLD, size=18),
                ]),
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.VERIFIED, color=C_GREEN, size=14),
                            ft.Text("  Certificate Verified ✓", color=C_GREEN, size=11,
                                    weight=ft.FontWeight.BOLD)
                        ], tight=True),
                        ft.Container(height=6),
                        ft.Container(
                            content=ft.Text(
                                spans=[ft.TextSpan(
                                    text=url,
                                    style=ft.TextStyle(color=C_CYAN, size=10, weight=ft.FontWeight.W_500),
                                    url=url
                                )],
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            bgcolor="#041520", border=ft.Border.all(1, C_CYAN),
                            border_radius=6, padding=ft.Padding.symmetric(horizontal=10, vertical=6),
                        ),
                    ], spacing=4),
                    bgcolor="#040D00", border=ft.Border.all(1, f"{C_GREEN}50"),
                    border_radius=8, padding=10),
            ], spacing=6),
            gradient=ft.LinearGradient(begin=ft.Alignment(-1,-1), end=ft.Alignment(1,1),
                                       colors=["#0A1200", BG_CARD2]),
            border=ft.Border.all(1, f"{C_GOLD}40"), border_radius=14, padding=14,
        )], col={"xs": 12, "md": 6})

    completed_banner = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.VERIFIED, color=C_GREEN, size=16),
            ft.Text("  5 / 5 Courses Completed", color=C_GREEN, size=13, weight=ft.FontWeight.BOLD),
            ft.Container(width=20),
            ft.Icon(ft.Icons.OPEN_IN_NEW, color=C_CYAN, size=13),
            ft.Text("  matlabacademy.mathworks.com", color=C_CYAN, size=12),
        ], tight=True),
        bgcolor="#041A08", border=ft.Border.all(1, C_GREEN),
        border_radius=8, padding=ft.Padding.symmetric(horizontal=14, vertical=10))

    return ft.Column([
        section_header("MATLAB ACHIEVEMENT HUB", C_GOLD, ft.Icons.WORKSPACE_PREMIUM),
        ft.Text("Completed MathWorks Learning Center courses — certificates verified below.",
                size=13, color=C_GREY),
        ft.Container(height=8),
        completed_banner,
        ft.Container(height=16),
        ft.ResponsiveRow([cert_card(i + 1, name, url) for i, (name, url) in enumerate(courses)],
                         spacing=12),
    ], scroll=ft.ScrollMode.AUTO, spacing=8)


# ════════════════════════════════════════════════════════════════
#   PAGE 3 — TECHNICAL BLOG 
# ════════════════════════════════════════════════════════════════

def build_blog():
    # Blog post content data
    blog_posts = [
        {
            "num": 1,
            "topic": "Variables & Data Types",
            "color": C_CYAN,
            "formula": "Total Cost = Σᵢ₌₁ⁿ (Qᵢ × Pᵢ) + Overheads",
            "date": "20 May 2026",
            "title": "Confidence in Concepts: Understanding Variables in Python",
            "explanation": "A variable is like a labeled container that stores data in a computer's memory. In Python, you don't need to declare what type of data will go in the container — you simply assign a value using the equals sign. For example, 'temperature = 85' stores the number 85 in a variable called 'temperature'. The main data types in Python are integers (whole numbers like 5 or -3), floats (decimal numbers like 3.14 or -0.5), strings (text inside quotes like 'Hello'), and booleans (True or False values). In engineering applications, variables are essential. In my CorroCheck project, variables store important information such as the corrosion severity level ('severity = MODERATE'), the user's name ('user_name = Elia'), the path to an image file ('photo_path = scan_001.jpg'), and calculation results like the percentage of corrosion detected. Without variables, a program cannot remember any data between different operations or functions.",
            "video_url": "https://www.youtube.com/watch?v=LKFrQXaoSMQ"
        },
        {
            "num": 2,
            "topic": "Functions & Return Values",
            "color": C_PURPLE,
            "formula": "f(x) = ax² + bx + c   →   roots at x = (−b ± √(b²−4ac)) / 2a",
            "date": "21 May 2026",
            "title": "Confidence in Concepts: Functions and Return Values",
            "explanation": "A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you write it once inside a function and then 'call' that function whenever you need to use it. Functions can take inputs (called parameters) and can send back outputs (called return values). For example, 'def calculate_stress(force, area): return force / area' defines a function that takes force and area as inputs, calculates stress, and returns the result. This is exactly how structural engineers determine if a material can withstand a given load — stress equals force divided by area. In the CorroCheck app, we could use a function like 'def classify_corrosion(percentage): if percentage < 10: return LOW else: return HIGH' to automate severity classification. Functions make code more organized, easier to debug, and reusable across different parts of an application.",
            "video_url": "https://www.youtube.com/watch?v=89cGQjB5R4M"
        },
        {
            "num": 3,
            "topic": "Loops & Iteration",
            "color": C_GREEN,
            "formula": "σ = √( (1/n) × Σᵢ₌₁ⁿ (xᵢ − μ)² )",
            "date": "22 May 2026",
            "title": "Confidence in Concepts: Loops and Iteration",
            "explanation": "Loops allow a program to repeat a block of code multiple times without writing the same lines over and over. A 'for' loop is used when you know exactly how many times to repeat — for example, going through each item in a list. A 'while' loop continues repeating until a specific condition becomes false. For instance, to analyze 1000 sensor readings, you could write 'for reading in sensor_data: if reading > threshold: alert_count += 1'. This single loop checks every reading without writing 1000 lines of code. In civil engineering, loops are essential for processing large datasets such as strain gauge measurements from a bridge over time. In the CorroCheck app, a loop could iterate through a list of saved scans to display them in the history screen, or repeatedly check camera input for corrosion detection. Loops save time, reduce errors, and make programs more efficient.",
            "video_url": "https://www.youtube.com/watch?v=94UHCEmprCY"
        },
        {
            "num": 4,
            "topic": "Object-Oriented Programming",
            "color": C_PINK,
            "formula": "Stress σ = F / A   [Pa]      Strain ε = ΔL / L₀",
            "date": "23 May 2026",
            "title": "Confidence in Concepts: Object-Oriented Programming (OOP)",
            "explanation": "Object-Oriented Programming (OOP) is a way of organizing code by creating 'objects' that contain both data (called attributes) and actions (called methods). A 'class' is the blueprint or template, and an 'object' is an actual instance created from that blueprint. For example, a 'Beam' class might have attributes like 'length', 'material', and 'load_capacity', and methods like 'calculate_deflection()' or 'check_safety()'. You could then create multiple beam objects, each with its own specific values. In the CorroCheck app, we could have a 'Scan' class where each scan object stores its own photo, severity level, date, GPS location, and inspector notes. The class could also have methods like 'save_to_history()' or 'share_report()'. OOP makes code more intuitive, reusable, and easier to maintain, especially for large applications like CorroCheck that manage many similar items.",
            "video_url": "https://www.youtube.com/watch?v=JeznW_7DlB0"
        },
        {
            "num": 5,
            "topic": "Data Structures",
            "color": C_GOLD,
            "formula": "Density ρ = m / V   [kg/m³]",
            "date": "24 May 2026",
            "title": "Confidence in Concepts: Data Structures in Python",
            "explanation": "Data structures are ways to organize and store multiple pieces of data together in a single variable. A 'list' stores items in a specific order, like 'sensor_readings = [23.5, 24.1, 22.8, 25.0]' — you can access items by their position (index). A 'dictionary' stores key-value pairs, like 'material = {name: Steel, density: 7850, cost_per_kg: 2.5}' — you look up values by their unique key. A 'set' stores unique values with no duplicates, useful for removing repeated entries. In mining engineering, dictionaries are perfect for storing material properties where the material name is the key and its properties (density, hardness, cost) are the values. In CorroCheck, a list could store multiple scan records, and each scan could be a dictionary containing all its details (photo path, severity, date, location). Choosing the right data structure makes your code faster, cleaner, and more logical.",
            "video_url": "https://www.youtube.com/watch?v=MZZSMaEAC2g"
        }
    ]

    def blog_post(post):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    tag_chip(f"POST {post['num']:02d}", post['color']),
                    ft.Container(width=8),
                    ft.Container(
                        content=ft.Text(f"📅 {post['date']}", color=C_GREY, size=11, italic=True),
                        bgcolor=BG_DARK, border_radius=4, padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                    ),
                ], wrap=True),
                ft.Container(height=8),
                ft.Container(
                    content=ft.Text(f"📖 {post['title']}", color=C_WHITE, size=14, weight=ft.FontWeight.BOLD),
                    bgcolor=BG_DARK, border_radius=6, padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                ),
                ft.Container(height=12),

                # Written Explanation
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Icon(ft.Icons.ARTICLE, color=post['color'], size=14),
                                ft.Text("  Written Explanation", color=post['color'], size=12, weight=ft.FontWeight.W_600)], tight=True),
                        ft.Container(height=6),
                        ft.Container(
                            content=ft.Text(post['explanation'], color=C_WHITE, size=11, selectable=True),
                            bgcolor=BG_DARK, border_radius=8, padding=12,
                        ),
                    ], spacing=0),
                    bgcolor=BG_DARK, border_radius=8, padding=12),
                ft.Container(height=8),

                # Mathematical Notation
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Icon(ft.Icons.FUNCTIONS, color=C_GREEN, size=14),
                                ft.Text("  Mathematical Notation", color=C_GREEN, size=12, weight=ft.FontWeight.W_600)], tight=True),
                        ft.Container(height=6),
                        ft.Container(
                            content=ft.Text(post['formula'], color=C_WHITE, size=13, font_family="Courier New"),
                            bgcolor="#041008", border_radius=6,
                            padding=ft.Padding.symmetric(horizontal=14, vertical=10)),
                        ft.Container(height=6),
                        ft.Container(
                            content=ft.Text("This formula is directly applicable to engineering calculations — for example, calculating total material costs, solving quadratic equations for structural analysis, or computing standard deviation for quality control.", color=C_GREY, size=10, italic=True),
                            bgcolor="#040D08", border_radius=6, padding=10,
                        ),
                    ], spacing=0),
                    bgcolor="#040D08", border=ft.Border.all(1, f"{C_GREEN}40"), border_radius=8, padding=12),
                ft.Container(height=8),

                # Video Link (clickable)
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Icon(ft.Icons.SMART_DISPLAY, color=C_PINK, size=14),
                                ft.Text("  Video Explanation", color=C_PINK, size=12, weight=ft.FontWeight.W_600)], tight=True),
                        ft.Container(height=6),
                        ft.Text(
                            spans=[ft.TextSpan(
                                text="🎬 Click here to watch the video on YouTube",
                                style=ft.TextStyle(color=C_CYAN, size=11, weight=ft.FontWeight.W_500),
                                url=post['video_url']
                            )],
                        ),
                    ], spacing=0),
                    bgcolor="#0D0008", border_radius=8, padding=12),
            ], spacing=0),
            bgcolor=BG_CARD, border=ft.Border.all(1, f"{post['color']}35"), border_radius=16, padding=18,
        )

    return ft.Column([
        section_header("TECHNICAL BLOG", C_PURPLE, ft.Icons.MENU_BOOK),
        ft.Text("Confidence in Concepts — explaining core programming topics in my own words with engineering applications.", size=13, color=C_GREY),
        ft.Container(height=16),
        *[blog_post(post) for post in blog_posts],
    ], scroll=ft.ScrollMode.AUTO, spacing=16)


# ════════════════════════════════════════════════════════════════
#   PAGE 4 — GITHUB EVIDENCE
# ════════════════════════════════════════════════════════════════

def build_github():
    def section_box(title, icon, color, rows):
        return ft.Container(
            content=ft.Column([
                ft.Row([ft.Icon(icon, color=color, size=18),
                        ft.Text(f"  {title}", size=15, color=color, weight=ft.FontWeight.BOLD)], tight=True),
                ft.Container(width=44, height=2, bgcolor=color, margin=ft.Margin.only(top=6, bottom=12)),
                *rows,
            ], spacing=6),
            bgcolor=BG_CARD, border=ft.Border.all(1, f"{color}35"), border_radius=14, padding=16)

    # ── Role badge ───────────────────────────────────────────────
    role_badge = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.PALETTE, color=C_PINK, size=16),
            ft.Text(
                "  Role: UI/UX Designer — Figma  |  "
                "Design assets committed to the group repo",
                color=C_PINK, size=12, weight=ft.FontWeight.W_600),
        ], tight=True),
        bgcolor="#1A0010", border=ft.Border.all(1, C_PINK),
        border_radius=8, padding=ft.Padding.symmetric(horizontal=14, vertical=10))

    # ── Commit History (1 real commit with clickable SHA) ────────
    def info_row(label, value, color, is_link=False, link_url=""):
        if is_link:
            content = ft.Text(
                spans=[ft.TextSpan(
                    text=value,
                    style=ft.TextStyle(color=color, size=11, weight=ft.FontWeight.W_500, font_family="Courier New"),
                    url=link_url
                )],
            )
        else:
            content = ft.Text(value, size=11, color=color, font_family="Courier New")
        
        return ft.Row([
            ft.Container(
                content=ft.Text(label, size=10, color=C_GREY, weight=ft.FontWeight.W_600),
                width=90),
            ft.Container(
                content=content,
                bgcolor=f"{color}12", border=ft.Border.all(1, f"{color}40"),
                border_radius=5, padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                expand=True),
        ], tight=True)

    commit_card = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Icon(ft.Icons.COMMIT, color=C_GREEN, size=14),
                    bgcolor=f"{C_GREEN}20", border_radius=8, width=34, height=34,
                    alignment=ft.Alignment(0, 0)),
                ft.Container(width=10),
                ft.Column([
                    ft.Text("Commit #1  —  Design Assets", color=C_WHITE,
                            size=12, weight=ft.FontWeight.W_600),
                    ft.Text("Only commit · main branch (#3)", color=C_GREY, size=10),
                ], spacing=2, expand=True),
                tag_chip("DESIGN", C_PINK),
            ]),
            ft.Divider(height=12, color=C_BORDER),
            info_row("SHA", "4080b00 (click to view)", C_GREEN, is_link=True, 
                     link_url="https://github.com/CorroCheck-team/UNAM-I3691CP-Group7-CorroCheck/commit/4080b006dbb8966b2d0c8224cee1f6f67f6028e6"),
            ft.Container(height=4),
            info_row("Message", "Add design photos", C_CYAN),
            ft.Container(height=4),
            info_row("Date", "~12 May 2026  ·  2 weeks ago", C_GOLD),
            ft.Container(height=4),
            info_row("Files", "2 files changed", C_WHITE),
            ft.Container(height=8),
            ft.Container(
                content=ft.Column([
                    ft.Row([ft.Icon(ft.Icons.INSERT_DRIVE_FILE, color=C_CYAN, size=12),
                            ft.Text("  docs/designs/logo's/elija's-logo.png.png",
                                    color=C_CYAN, size=11, font_family="Courier New")], tight=True),
                    ft.Row([ft.Icon(ft.Icons.INSERT_DRIVE_FILE, color=C_PURPLE, size=12),
                            ft.Text("  docs/designs/screens/HistoryDetailsScreen.png.png",
                                    color=C_PURPLE, size=11, font_family="Courier New")], tight=True),
                ], spacing=5),
                bgcolor=BG_DARK, border=ft.Border.all(1, C_BORDER),
                border_radius=6, padding=ft.Padding.symmetric(horizontal=12, vertical=8)),
        ], spacing=4),
        bgcolor=BG_DARK, border=ft.Border.all(1, C_BORDER), border_radius=10, padding=14)

    commit_section = section_box(
        "Commit History", ft.Icons.HISTORY, C_GREEN,
        [ft.Text("Design assets committed directly to the group's main branch.",
                 color=C_GREY, size=12),
         ft.Container(height=6),
         commit_card])

    # ── No Pull Requests note ────────────────────────────────────
    pr_note = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.INFO_OUTLINE, color=C_GREY, size=16),
            ft.Text(
                "  No Pull Requests opened — design contribution was submitted via "
                "a direct commit to the main branch.",
                color=C_GREY, size=12, italic=True, expand=True),
        ], tight=True),
        bgcolor=BG_CARD, border=ft.Border.all(1, C_BORDER),
        border_radius=10, padding=ft.Padding.symmetric(horizontal=14, vertical=14))

    # ── Design Impact Summary ────────────────────────────────────
    def impact_card(title, subtitle, color, icon, body):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Icon(icon, color=color, size=16),
                        bgcolor=f"{color}20", border_radius=8, width=34, height=34,
                        alignment=ft.Alignment(0, 0)),
                    ft.Container(width=10),
                    ft.Column([
                        ft.Text(title, color=color, size=12, weight=ft.FontWeight.BOLD),
                        ft.Text(subtitle, color=C_GREY, size=10),
                    ], spacing=1, expand=True),
                ]),
                ft.Container(height=8),
                ft.Container(
                    content=ft.Text(body, color=C_WHITE, size=11, selectable=True),
                    bgcolor=BG_DARK, border=ft.Border.all(1, f"{color}35"),
                    border_radius=6, padding=ft.Padding.symmetric(horizontal=12, vertical=10)),
            ], spacing=0),
            bgcolor=BG_DARK, border=ft.Border.all(1, C_BORDER),
            border_radius=10, padding=14, margin=ft.Margin.only(top=6))

    impact_section = section_box(
        "Design Impact Summary", ft.Icons.PALETTE, C_GOLD,
        [ft.Text("How your Figma designs contributed to the CorroCheck application.",
                 color=C_GREY, size=12),
         impact_card(
             "CorroCheck App Logo", "Used in production · Splash Screen & branding",
             C_GOLD, ft.Icons.STAR,
             "Designed the official CorroCheck logo featuring a corroded metallic droplet "
             "that visually communicates the app's core purpose — corrosion detection. "
             "The logo is currently live in the app's Splash Screen and serves as the "
             "brand identity across the entire application, used by engineers, inspectors, "
             "and maintenance personnel in the field."
         ),
         impact_card(
             "History Details Screen", "UI design · Figma prototype",
             C_CYAN, ft.Icons.HISTORY,
             "Designed the History Details screen in Figma, displaying a full saved "
             "inspection report — including the scanned image, corrosion type "
             "(uniform, galvanic, pitting, or crevice), severity level (Low/Medium/High), "
             "GPS location, date, and inspector notes. Although the final development team "
             "implemented a different version, this Figma screen contributed to the team's "
             "understanding of the report layout and user flow for the history feature."
         ),
        ])

    return ft.Column([
        section_header("GITHUB EVIDENCE", C_GREEN, ft.Icons.CODE),
        ft.Text(
            "Individual contribution to the CorroCheck group project — UI/UX Design role.",
            size=13, color=C_GREY),
        ft.Container(height=16),
        role_badge,
        ft.Container(height=16),
        commit_section,
        ft.Container(height=16),
        pr_note,
        ft.Container(height=16),
        impact_section,
    ], scroll=ft.ScrollMode.AUTO, spacing=0)


# ════════════════════════════════════════════════════════════════
#   NAVIGATION + APP ENTRY POINT
# ════════════════════════════════════════════════════════════════

PAGES = [
    ("HOME",     ft.Icons.HOME,               C_CYAN,   build_home),
    ("TIMELINE", ft.Icons.TIMELINE,           C_PURPLE, build_timeline),
    ("MATLAB",   ft.Icons.WORKSPACE_PREMIUM,  C_GOLD,   build_matlab),
    ("BLOG",     ft.Icons.MENU_BOOK,          C_PINK,   build_blog),
    ("GITHUB",   ft.Icons.CODE,               C_GREEN,  build_github),
]


def main(page: ft.Page):
    page.title      = "Web Portfolio 2026"
    page.bgcolor    = BG_DARK
    page.padding    = 0
    page.spacing    = 0
    page.theme      = ft.Theme(color_scheme_seed=C_CYAN)
    page.theme_mode = ft.ThemeMode.DARK

    current = [0]

    content_area = ft.Container(
        content=build_home(), expand=True, bgcolor=BG_DARK,
        padding=ft.Padding.all(20),
    )

    def make_nav_btn(index, label, icon, color):
        active = index == current[0]
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(icon, color=color if active else C_GREY, size=20),
                    bgcolor=f"{color}22" if active else "transparent",
                    border_radius=10, width=42, height=42, alignment=ft.Alignment(0,0)),
                ft.Text(label, size=8, color=color if active else C_GREY,
                        weight=ft.FontWeight.BOLD if active else ft.FontWeight.NORMAL),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
            padding=ft.Padding.symmetric(vertical=8, horizontal=4),
            border_radius=10,
            bgcolor=f"{color}12" if active else "transparent",
            on_click=lambda e, i=index: navigate(i),
        )

    sidebar_col = ft.Column([], spacing=2)

    def build_sidebar():
        sidebar_col.controls = [
            ft.Container(content=ft.Text("◈", size=22, color=C_CYAN),
                         alignment=ft.Alignment(0,0),
                         padding=ft.Padding.symmetric(vertical=14)),
            ft.Divider(height=1, color=C_BORDER),
            ft.Container(height=6),
            *[make_nav_btn(i, lbl, ico, col) for i, (lbl, ico, col, _) in enumerate(PAGES)],
        ]

    build_sidebar()

    sidebar = ft.Container(
        content=ft.Column([sidebar_col], scroll=ft.ScrollMode.AUTO),
        bgcolor=NAV_BG,
        border=ft.Border.only(right=ft.BorderSide(1, C_BORDER)),
        width=70,
    )

    def navigate(index):
        current[0] = index
        _, _, _, builder = PAGES[index]
        content_area.content = builder()
        build_sidebar()
        page.update()

    page.add(ft.Row([sidebar, content_area], expand=True, spacing=0))


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)