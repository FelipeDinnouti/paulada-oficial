from fasthtml.common import *
from dataclasses import dataclass

# Form
@dataclass
class User: email:str; password:str; gender:bool; # 0 (False) is male, 1 is female 

profile_form = Form(method="post", action="/")  (
        Fieldset(
            Label('Email', Input(name="email")),
            Label("Senha", Input(name="password", type="password")),
            Label("Gênero", Input(name="gender", type = "checkbox")),
        ),
        Button("Cadastro", type="submit"),
    )


# Main app
app, rt = fast_app(debug=True)

@app.get("/")
def home():
    return Titled("Paulada Oficial", P("È hora da paulada"), A("Cadstro", href = "/cadastro"))

@rt("/cadastro")
def get():
    return Titled("Faça seu cadastro", profile_form)

@app.route("/", methods=['post'])
def post(email: str, password: str, gender: bool): # Variable position must match form input index
    print(f"email: {email}\npassword: {password}\ngender: {gender}")
    return home()

@rt("/about")
def get():
    return Titled("De fato, nós exisitimos", P("meu nome é japonês"))

serve()