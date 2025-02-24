from fasthtml.common import *

# Text Importing
home_page_main_text_file = open("assets/texts/MainPage.md", "r")
home_page_main_text = home_page_main_text_file.read()

rules_main_text_file = open("assets/texts/OfficialRegulamentation.md", "r")
rules_main_text = rules_main_text_file.read()

INVALID_EMAIL_ERROR = "E-mail inválido"
ALREADY_USED_EMAIL_ERROR = "E-mail já foi cadastrado"
ALREADY_USED_NAME_ERROR = "Nome já está em uso"

register_form = Form(method="post")  ( 
        Fieldset(
            Label("Nome", Input(name="name", placeholder="bota seu nome aqui", id="input_field"), id="input_label"),
            Label("", cls="form_error_message", id="name_error"),

            Label('E-mail', Input(name="email", placeholder="exemplodaora@gmail.com", id="input_field"), id="input_label"),
            Label("", cls="form_error_message", id="email_error"),

            Label("Senha", Input(name="password", type="password", placeholder="nao vou contar pra ninguem", id="input_field"), id="input_label"),
            Label("Gênero"),
            Select(Option("Homem", value="men"), Option("Mulher", value="woman"),name="gender", type = "checkbox", style="width: 12em; height: 2em"),
        ),
        Button("Cadastro", type="submit"),
    ) 
login_form = Form(method="post",)(
    Fieldset(
        Label("Email", Input(name="email", placeholder="E-mail", id="input_field"), id="input_label" ),
        Label("Senha", Input(name="password", type="password", placeholder="Senha", id="input_field"), id="input_label")
    ),
    Button("Login", type="submit", href="/"),
)
logout_form = Form(method="post",)(
    Button("Logout", type="submit", href="/", style="width: 20%; background-color: #c2042f; border-color: #970222")
)

navigation = Div(
     
    A("Login", href="/login", cls="navlink"), 
    A("Perfil", href="/perfil", cls="navlink"),
    A("Regras", href="/regras", cls="navlink"),
    A("Home", href="/", cls="navlink"),
    id="navigation",
)

header = Div(Div(
        H1("Paulada Oficial", id="main_title"),    
        A(id="logo_link", href="/"),
        id="header_div",
        ), navigation)

home = Div(
            header,
            Div(home_page_main_text,cls="marked", id="main_section"),Titled(""),
            cls="container",
)

forum = Div(
    header,
    H2("Paulada Forum"),
)

rules = Div(
    header,
    Div(rules_main_text, cls="marked", id="main_section"),
    cls="container",
)

login = Div(
        header,
        Div(
        login_form,
            Div(
                A("Cadastro", href = "/cadastro"),
                style="text-align: center",
            ),
            id="main_section",
        ),
        cls="container"
)

register = Div(
        header,
        Div(
        H2("Faça seu cadastro"),
        register_form,
        id="main_section",
        ),
        cls="container",
    )