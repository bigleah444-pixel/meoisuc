from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"7937540559")
ch = "I_I_T10" 
OWNER_USERNAME = "M_R_Q_P"
ST = "M_R_Q_P"
LT = "M_R_Q_P"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "ســـنايبر"

bot_token=os.environ.get("Token", None)
bot_token2="BACTe04AjtvmUj9AyYSCx3YQ77fQ8NCQ6eWJ5-GGlCNgTQH1oycMJqBRM4ju6vIw3_KTwiCcWYzus7QG4ffb2LNCZ5bLHsclgYGIp2JdIvr-OKi3I7RHsM_0j54IdDs45K-d0EQueZq97DP8r4pMIb2TVF7aHGbYLy7LX89CFw0dGy5jqeN3D-QrpPwro1O0QgDqjNYjH-ES6Vg_JnM6OiG4v3l_IXH8THkfViyaZB2JVNPmJlZUgrnKonJgotMFRYUA8Wa1PM45XkEv7dXCtgCcPbLvgdc3sE8vj56mcsuoQlpkzpM2DaCFa4X35ElqwMqZPSXk3G8ODxbBdCO4PLJvFCH7VAAAAAHdw069AQ"


bot = Client("ITA", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
