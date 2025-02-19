from fasthtml.common import *

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

home_page = (Titled("Paulada Oficial", 
                    P("È hora da paulada"), 
                    A("Cadastro", href = "/cadastro"), 
                    Br(), 
                    A("Login", href="/login"), 
                    Br(), 
                    A("Perfil", href="/perfil"),
                    )        
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
        A(style="height: 65px; width: 105px; display: inline-block;  background-image: url('assets/icons/logo.svg'); background-size: cover", href="/"),
        style="display: flex; justify-content: space-between; align-items: center;"
        )


home = Div(
            header,
            P("""De fato, um esporte completamente verídico."""),
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