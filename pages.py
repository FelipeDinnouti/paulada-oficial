from fasthtml.common import *

# Text Importing
home_page_main_text_file = open("assets/texts/MainPage.md", "r")
home_page_main_text = home_page_main_text_file.read()

register_form = Form(method="post")  (
        Fieldset(
            Label('Email', Input(name="email")),
            Label("Senha", Input(name="password", type="password")),
            Label("Gênero", Input(name="gender", type = "checkbox")),
        ),
        Button("Cadastro", type="submit"),
    )
login_form = Form(method="post")(
    Fieldset(
        Label("Email", Input(name="email")),
        Label("Senha", Input(name="password", type="password"))
    ),
    Button("Login", type="submit"),
)

navigation = Div(
    A("Cadastro", href = "/cadastro"), 
    A("Login", href="/login"), 
    A("Perfil", href="/perfil"),
    style="display: flex; justify-content: space-evenly; width: 40%",
)

header = Div(
        H1("Paulada Oficial", style="padding: 24px 0px; display: inline-block; margin: 0px"),    
        navigation,
        A(id="logo_link", href="/"),
        id="header_div",
        )


home = Div(
            header,
            Div(home_page_main_text,cls="marked"),
            cls="container",
        )

about = Div(
        header,
        P("meu nome é japonês"),
        cls="container"
    )

login = Div(
        header,
        H2("Faça seu login"),
        login_form,
        cls="container"
    )

register = Div(
        header,
        H2("Faça seu cadstro"),
        register_form,
        cls="container"
    )