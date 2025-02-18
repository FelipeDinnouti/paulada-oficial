from fasthtml.common import *
from dataclasses import dataclass

# Form dataclass, basically the object that is used as standard for the database
@dataclass
class User: email:str; password:str; gender:bool; # 0 (False) is male, 1 is female 

profile_form = Form(method="post")  (
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

# Database
db = database("users.db")
users = db.create(User, pk="email")

# User register handling
def register_user(email: str, password: str, gender: bool):
    user = User(email, password, gender)
    users.insert(user)

def fetch_user(email: str, password: str):
    user = users[email] # Email is the primary key
    if not user:
        return -2 # User doesn't exist
    if user.password != password: # Very secure password
        return -1 # User exists but wrong password
    
    return user

# User authentication
login_redirect = RedirectResponse('/login', status_code=303)

# Checks if the user is authenticated by checking the session information
def user_auth_before(request, session):
    auth = request.scope['auth'] = session.get('auth', None)
    if not auth: return login_redirect

# Runs right before changing pages
beforeware = Beforeware(
    user_auth_before,
    skip=[r'/favicon\.ico', r'/static/.*', r'.*\.css', r'.*\.js', '/login', '/', '/about', '/cadastro']
)

# FastAPI app
app, rt = fast_app(debug=True, before=beforeware)

@app.get("/")
def home():
    return Titled("Paulada Oficial", P("È hora da paulada"), A("Cadastro", href = "/cadastro"), Br(), A("Login", href="/login"), Br(), A("Perfil", href="/perfil"))

@rt("/cadastro")
def get():
    return Titled("Faça seu cadastro", profile_form)

@rt("/login")
def get():
    return Titled(f"Faça seu login", login_form)

# Receives the login information and sets the auth variable in the session
@app.route("/login", methods=['post'])
def post(email: str, password: str, session):
    user = fetch_user(email, password)
    if user == -1:
        return Titled("Senha errada irmao")
    if user == -2:
        return Titled("Esse email nao foi cadastrado nao")

    session.setdefault("auth",email)
    return Titled(f"Gênero: {user.gender}")


@rt("/perfil")
def get(session):
    email = session.get("auth")

    return Titled(f"Perfil de {email}")

# Receives the register information and creates an entry in the database
@app.route("/cadastro", methods=['post'])
def post(email: str, password: str, gender: bool): # Variable position must match form input index
    user = fetch_user(email, password)
    if user != -2: # User DOES exist
        return Titled("Já existe esse usuário ai meu")

    print(f"email: {email}\npassword: {password}\ngender: {gender}")
    register_user(email, password, gender)
     
    return home() # Go to home page

@rt("/about")
def get():
    return Titled("De fato, nós exisitimos", P("meu nome é japonês"))

serve()