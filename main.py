from fasthtml.common import *
from dataclasses import dataclass
import pages

# Form dataclass, basically the object that is used as standard for the database
@dataclass
class User: email:str; password:str; gender:bool; # 0 (False) is male, 1 is female 

# Database
db = database("users.db")
users = db.create(User, pk="email")

# User register handling
def register_user(email: str, password: str, gender: bool):
    user = User(email, password, gender)
    users.insert(user)

def fetch_user(email: str, password: str):
    if not email in users:
        return -2 # User has not been registered, does not exist

    user = users[email] # Email is the primary key

    if user.password != password: # Very secure password
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
    skip=[r'/favicon\.ico', r'/static/.*', r'.*\.css', r'.*\.js', '/login', '/', '/about', '/cadastro']
)

hdrs = (MarkdownJS(), Link(rel="stylesheet", href="assets/css/mystyle.css"))

# FastAPI app
app, rt = fast_app(
    debug=True,
    before=beforeware,
    hdrs=hdrs
    )

@app.get("/")
def home():
    pages.home_page_main_text = pages.home_page_main_text_file.read() # Hot update the markdown (for live editing)
    print("Reloaded -------------------------------")

    return pages.home

@rt("/cadastro")
def get():
    return pages.register

@rt("/login")
def get():
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

    return Div(
        pages.header,
        H2(f"Perfil de {email}"),
        P(f"Gênero: {user.gender}"),
        cls="container"
    )

# Receives the register information and creates an entry in the database
@app.route("/cadastro", methods=['post'])
def post(email: str, password: str, gender: bool): # Variable position must match form input index
    user = fetch_user(email, password)
    if user != -2: # User DOES exist
        return Titled("Já existe esse usuário ai meu")

    print(f"email: {email}\npassword: {password}\ngender: {gender}")
    register_user(email, password, gender)
     
    return home_redirect

@rt("/about")
def get():
    return pages.about

serve()