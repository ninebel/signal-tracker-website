

# ====================================================================================================================================
# APP
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/' # Key used for encrypting cookies in bytes
# ====================================================================================================================================

# ====================================================================================================================================
# FLASK-SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'sqlite:///alerts.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ====================================================================================================================================

# ====================================================================================================================================
# CELERY - format: message_queue_protocol://:password@hostname:port/db_number
CELERY_BROKER_URL = 'redis://:12345@80.208.230.217:6379/0' # For the Celery broker, in this case Redis
CELERY_RESULT_BACKEND = 'redis://:12345@80.208.230.217:6379/0' # For the Celery result
# ====================================================================================================================================

# ====================================================================================================================================
# YAHOO FINANCE DATA

intervals = ['5m', '15m', '60m', '1d', '1wk']

# Brazilian Stock Market - Ibovespa
financeiro = ["BBDC4.SA", "ITUB4.SA", "B3SA3.SA", "BPAC11.SA", "CIEL3.SA", "ITSA4.SA", "SANB11.SA"]
alimentos = ["BEEF3.SA" , "MRFG3.SA", "ABEV3.SA", "BKBR3.SA", "JBSS3.SA", "MEAL3.SA", "MDIA3.SA", "PCAR3.SA"]
seguros = ["IRBR3.SA", "BBSE3.SA"]
aviacao = ["GOLL4.SA", "AZUL4.SA"]
locadoras = ["MOVI3.SA" , "RENT3.SA", "LCAM3.SA"]
etf = ["BOVA11.SA"]
varejo = ["VVAR3.SA", "MGLU3.SA", "LAME4.SA", "BTOW3.SA"]
vestuario = ["ARZZ3.SA", "HGTX3.SA", "LREN3.SA", "GUAR3.SA"]
saude = ["FLRY3.SA", "QUAL3.SA"]
turismo = ["CVCB3.SA", "HYPE3.SA"]
educacao = ["COGN3.SA", "YDUQ3.SA"]
tec_da_info = ["LWSA3.SA", "POSI3.SA"]
telecom = ["OIBR4.SA"]
celulose_oleo_gas = ["KLBN4.SA", "PETR4.SA", "SUZB3.SA"]
combustivel = ["CSAN3.SA", "UGPA3.SA"]
energia = ["CMIG4.SA", "ELET3.SA", "ENGI11.SA", "TAEE11.SA", "EGIE3.SA"]
saneamento = ["CSMG3.SA", "SAPR11.SA", "SBSP3.SA"]
transp_logistica = ["ECOR3.SA", "EMBR3.SA", "POMO4.SA", "RLOG3.SA"]
shoppings = ["BRML3.SA", "IGTA3.SA", "JHSF3.SA"]
imobiliarios = ["CYRE3.SA", "EVEN3.SA", "GFSA3.SA", "MRVE3.SA", "TCSA3.SA"]
ind_min_sid = ["CSNA3.SA", "GGBR3.SA", "GOAU4.SA", "USIM5.SA", "VALE3.SA", "WEGE3.SA"]
ativos = financeiro + alimentos + seguros + aviacao + locadoras + etf + varejo + vestuario + saude + turismo + educacao + tec_da_info + telecom + celulose_oleo_gas + combustivel + energia + saneamento + transp_logistica + shoppings + imobiliarios + ind_min_sid

# ====================================================================================================================================