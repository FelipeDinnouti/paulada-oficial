from fasthtml.common import *

# Functions

def Spacer(height: Int, type: str ="px"):
    return Div(style=f"height: {height}{type}")

# Content: Markdown converted to html, which is in turn converted to FastHTML (using the extension)
home_page_main_content = Div(
    H2("O Esporte de Combate Estratégico que Desafia Corpo e Mente", cls='visible'),
    P(
        "Bem-vindo à",
        Em("Organização de Paulada Oficial (OPO)!"),
        "Aqui, você descobrirá um esporte dinâmico, cheio de adrenalina e estratégia, projetado para testar sua agilidade, precisão e inteligência tática. Conheça as regras, a essência e a emoção da Paulada!",
        cls='visible'
    ),
    Hr(cls='visible'),
    H2("O Que é a Paulada?", cls='visible'),
    P("A Paulada é um esporte de combate um contra um, onde dois adversários se enfrentam usando espadas improvisadas, geralmente feitas de madeira leve ou cabos de vassoura. O objetivo principal é simples, porém desafiador: acertar a parte inferior do corpo do oponente (pernas, joelhos, canelas ou pés) para marcar pontos. A simplicidade das regras esconde uma camada profunda de estratégia, exigindo movimentos rápidos, esquivas precisas e ataques calculados.", cls='visible'),
    P(
        "A parte da explicação técnica, o verdadeiro objetivo da paulada é ser um esporte com uma barreira de entrada baixa, para que qualquer um possa participar e se divertir. De fato o verdadeiro objetivo é a comunhão,",
        Em("e a verdadeira paulada são os amigos que a gente faz no caminho."),
        cls=''
    ),
    H2("Regras Básicas", cls=''),
    P(
        Em(
            "Nota:",
            Strong("A segurança é prioridade."),
            "Recomendamos a supervisão de um árbitro em combates oficiais e o uso de equipamentos adequados."
        ),
        cls=''
    ),
    Ol(
        Li(
            P("Área de Combate:\n O duelo ocorre em um espaço delimitado (como uma quadra ou área circular), garantindo que os jogadores tenham liberdade de movimento, mas também limites estratégicos.")
        ),
        Li(
            P("Pontuação:"),
            Ul(
                Li("Cada acerto válido na parte inferior do corpo (da cintura para baixo) vale 1 ponto.\n Toques na parte superior do corpo, braços ou cabeça não contam e podem resultar em penalidades, dependendo das regras locais.")
            )
        ),
        Li(
            P("Duração da Rodada:"),
            Ul(
                Li(
                    P("Uma rodada termina quando um jogador alcança 5 pontos.")
                ),
                Li(
                    P("Em caso de empate em 4-4, a disputa segue até que um jogador abra 2 pontos de vantagem (exemplo: 6-4).")
                )
            )
        ),
        Li(
            P("Equipamento:"),
            Ul(
                Li(
                    P("Espada de madeira/cabo de vassoura: Leve e segura, sem pontas afiadas ou materiais perigosos.")
                ),
                Li(
                    P(
                        "Proteção opcional:",
                        Strong("É extremamente recomendável o uso de calças que cubram até a canela."),
                        "Também recomenda-se o uso de caneleiras, joelheiras ou calçados fechados para segurança."
                    )
                )
            )
        )
    ),
    H2("A Essência da Paulada"),
    P("A Paulada não é apenas sobre força bruta, mas sobre inteligência em movimento. Os jogadores devem dominar:"),
    Ul(
        Li(
            P(
                Strong("Velocidade"),
                ": Ataques rápidos e surpresas."
            )
        ),
        Li(
            P(
                Strong("Defesa"),
                ": Bloquear golpes com a própria espada ou desviar com passos laterais."
            )
        ),
        Li(
            P(
                Strong("Estratégia"),
                ": Enganar o oponente com fintas e controlar o ritmo do combate."
            )
        )
    ),
    P("É um esporte inclusivo, adaptável a diferentes idades e níveis de condicionamento físico, sempre priorizando o respeito mútuo e a diversão saudável."),
    H2("Por Que Praticar Paulada?"),
    Ul(
        Li(
            P("Acessível: Requer apenas um equipamento simples e espaço aberto.")
        ),
        Li(
            P("Treino completo: Desenvolve coordenação, reflexos e resistência cardiovascular.")
        ),
        Li(
            P("Comunidade: Participe de torneios locais, rankings nacionais e eventos da OPO para se conectar com outros entusiastas.")
        )
    ),
    P("Junte-se à Revolução da Paulada!"),
    P("Seja você um competidor ávido ou um iniciante curioso, a Paulada oferece um desafio único que mistura tradição, criatividade e espírito esportivo. Visite nosso site para conhecer campeonatos, treinadores certificados e o manual completo de regras."),
    P("Prepare sua espada, ajuste sua estratégia e prepare-se para paulada."),
    P(
        Em("Organização de Paulada Oficial (OPO)"),
        Em("- Promovendo comunhão, estratégia e fair play desde 2025.")
    ),
    cls="appearing"
)

home_page_main_text_file = open("assets/texts/MainPage.md", "r")
home_page_main_text = home_page_main_text_file.read()

rules_main_text_file = open("assets/texts/OfficialRegulamentation.md", "r")
rules_main_text = rules_main_text_file.read()

INVALID_EMAIL_ERROR = "E-mail inválido"
ALREADY_USED_EMAIL_ERROR = "E-mail já foi cadastrado"
ALREADY_USED_NAME_ERROR = "Nome já está em uso"

# ----------------- COMPONENTS ---------------------
 
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
    cls="generic_form"
) 
login_form = Form(method="post",)(
    Fieldset(
        Label("Email", Input(name="email", placeholder="E-mail", id="input_field"), id="input_label" ),
        Label("Senha", Input(name="password", type="password", placeholder="Senha", id="input_field"), id="input_label")
    ),
    Button("Login", type="submit", href="/"),
    cls="generic_form",
)
logout_form = Form(method="post",)(
    Button("Logout", type="submit", href="/", style="width: 20%; background-color: #c2042f; border-color: #970222; min-width: 90px")
)

hamburger_button = Button(
    "☰",
    cls="hamburger_button",
    aria_label="Menu",
)

navigation = Div(
    hamburger_button,
    A(id="logo_link", href="/"),

    A("Home", href="/", cls="desktop_navlink"),
    A("Regras", href="/regras", cls="desktop_navlink"),
    A("Novidades", href="/novidades", cls="desktop_navlink"),
    A("Fórum", href="forum", cls="desktop_navlink"),

    id="navigation"
)


header_login = Div(
    A("Login", href="/login", cls="fixed_navlink"),
    A("Cadastro", href="/cadastro", cls="fixed_navlink", id="register_navlink"),
    id="header_login"
)

navigation_header = Div( 
    navigation,
    header_login,
    id="navigation_header",
)

header = Div(Div(
        H1("Paulada Oficial", id="main_title"),    
        A(id="logo_link", href="/"),
        id="header_div",
), navigation)

##  ------------------- PAGES 

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
        navigation_header,
        Spacer(4, "em"),
        Div(
            H1("Faça seu Login", cls="main_title"),
            H3("Bem vindo de volta!", cls="main_title"),
            
            login_form,
                Div(
                    A("Cadastro", href = "/cadastro"),
                    style="text-align: center",
                ),
                id="main_section",
        ),
        cls="container",
)

register = Div(
        navigation_header,
        Spacer(4, "em"),
        Div(
        H1("Faça seu cadastro", cls="main_title"),
        H3("Entre no mundo da Paulada!", cls="main_title"),
        register_form,
        id="main_section",
        ),
        cls="container",
    )

# Design V2

home = Div(
    navigation_header,
    Div(
        Img(src="assets/icons/logo.png", id="main_page_logo_svg"),
        H1("PAULADA", id="main_page_logo_text"),
        id="main_page_logo",
    ),
    Div(home_page_main_content, id="main_section"),
    cls="container",
)