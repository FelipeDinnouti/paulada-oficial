from fasthtml.common import *
from dataclasses import dataclass
import pages
import bcrypt

# Form dataclass, basically the object that is used as standard for the database
@dataclass
class User: name: str; email:str; password:str; gender:bool; # 0 (False) is male, 1 is female 

# Database
db = database("staging-users.db")
users = db.create(User, pk="email")

for u in users():
    print(u)

GENDER_MEN_STR = "men"
GENDER_WOMAN_STR = "woman"
GENDER_MEN = False
GENDER_WOMAN = True

MAX_NAME_LENGTH = 254
MAX_PASSWORD_LENGTH = 32
MAX_EMAIL_LENGTH = 254

# User register handling
def register_user(name: str, email: str, password: str, gender: bool):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    user = User(name, email, hashed_password, gender) 
    users.insert(user)

def fetch_user(email: str, input_password: str):
    if not email in users:
        return -2 # User has not been registered, does not exist

    user = users[email] # Email is the primary key

    result = bcrypt.checkpw(input_password.encode(), user.password)

    if result == False: # Very secure password
        return -1 # User exists but wrong password
    
    return user

# Redirects, 303 prevents POST (fixes 405 error i think)
login_redirect = RedirectResponse('/login', status_code=303)
profile_redirect = RedirectResponse('/perfil', status_code=303)
home_redirect = RedirectResponse('/', status_code=303)

# Checks if the user is authenticated by checking the session information
def user_auth_before(request, session):
    auth = request.scope['auth'] = session.get('auth', None)
    if not auth: return login_redirect

# Runs right before changing pages
beforeware = Beforeware(
    user_auth_before,
    skip=[r'.*\.png',r'/favicon\.ico', r'/static/.*', r'.*\.css', r'.*\.js', '/login', '/', '/about', '/cadastro', '/regras']
)

hdrs = (MarkdownJS(), 
        Link(rel="stylesheet", 
        href="assets/css/mystyle.css"),
        Link(rel="stylesheet", href="assets/css/pico-main/css/pico.css",), 
        Script(src="assets/scripts/jquery-3_7_1_min.js"),
        Script(src="assets/scripts/visible.js"), 
        Script(src="assets/scripts/title.js"),) 

# FastAPI app
app, rt = fast_app( 
    pico=False,
    debug=True,
    before=beforeware,
    hdrs=hdrs
    )

@app.get("/")
def home():
    pages.home_page_main_text_file = open("assets/texts/MainPage.md", "r")
    pages.home_page_main_text = pages.home_page_main_text_file.read() # Hot update the markdown (for live editing)
    return pages.home

@rt("/regras")
def get():
    pages.rules_main_text_file = open("assets/texts/OfficialRegulamentation.md", "r")
    pages.rules_main_text = pages.home_page_main_text_file.read()

    return pages.rules


@rt("/cadastro")
def get():
    return pages.register

@rt("/login")
def get():
    print("Login GET request")
    return pages.login


# Receives the login information and sets the auth variable in the session
@app.route("/login", methods=['post'])
def post(email: str, password: str, session):
    user = fetch_user(email, password)
    if user == -1:
        return Titled("Senha errada irmao")
    if user == -2:
        return Titled("Esse email nao foi cadastrado nao")

    session["auth"] = (email, password)
    return profile_redirect


@rt("/perfil")
def get(session):
    email, password = session.get("auth")

    user = fetch_user(email, password)

    if type(user) == int: # Any error
        return home_redirect

    gender_string = ""
    gender_string = "Mulher" if user.gender == GENDER_WOMAN else "Homem"
    

    return Div(
        pages.header,
        Div(
        H2(f"Perfil de {user.name}"),
        Br(),
        P(f"Gênero: {gender_string}"),
        P(f"E-mail: {user.email}"),
        pages.logout_form,
        id="main_section",
        ),
        cls="container",
    )

# Receives the register information and creates an entry in the database
@app.route("/cadastro", methods=['post'])
def post(name: str, email: str, password: str, gender: str, session): # Variable position must match form input index
    if len(name) > MAX_NAME_LENGTH:
        return Titled("Nome grande demais") 
    
    if len(email) > MAX_EMAIL_LENGTH:
        return Titled("Ninguém tem um email desse tamanho")
    
    if len(password) > MAX_PASSWORD_LENGTH:
        return Titled("Você não precisa de mais de 32 caracteres na sua senha")
    
    user = fetch_user(email, password)
    if user != -2: # User DOES exist
        return Titled("Já existe esse usuário ai meu")

    print(f"REGISTERING: email: {email}\npassword: {password}\ngender: {gender}")

    gender_value = False
    if gender == GENDER_WOMAN_STR:
        gender_value = GENDER_WOMAN
    elif gender == GENDER_MEN_STR:
        gender_value = GENDER_MEN

    register_user(name, email, password, gender_value)
    session["auth"] = (email, password)

    return profile_redirect

@app.route("/perfil", methods=['post'])
def logout(session):
    session["auth"] = None
    return home_redirect


@rt("/about")
def get():
    return pages.about

serve(port=5001)