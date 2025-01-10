import re, os, time
from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID")
    API_HASH  = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN") 

    # database config
    DB_NAME = os.environ.get("DB_NAME")     
    DB_URL  = os.environ.get("DB_URL")
    PORT = os.environ.get("PORT")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5814104129').split(',')]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'hyoshmangavf').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """
<b>ꜱᴀʟᴜᴛ! {}  

ᴊᴇ ꜱᴜɪꜱ ʜɪɴᴀᴛᴀ ʜʏᴜɢᴀ, ᴋᴜɴᴏɪᴄʜɪ ᴅᴜ ᴄʟᴀɴ ʜʏᴜɢᴀ ᴇᴛ, ᴀᴜᴊᴏᴜʀᴅ'ʜᴜɪ, ᴠᴏᴛʀᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛᴇ ᴅéᴠᴏᴜéᴇ. 🌀

» ᴛᴏᴜᴛ ᴄᴏᴍᴍᴇ ᴊᴇ ᴘʀᴏᴛèɢᴇ ᴄᴇᴜx ǫᴜɪ ᴍᴇ ꜱᴏɴᴛ ᴄʜᴇʀꜱ ᴀᴠᴇᴄ ᴍᴏɴ ʙʏᴀᴋᴜɢᴀɴ, ᴊᴇ ᴠᴀɪꜱ ᴍ'ᴀꜱꜱᴜʀᴇʀ ǫᴜᴇ ᴠᴏꜱ ꜰɪᴄʜɪᴇʀꜱ ꜱᴏɪᴇɴᴛ ʀᴇɴᴏᴍᴍéꜱ ᴀᴠᴇᴄ ᴘʀéᴄɪꜱɪᴏɴ ᴇᴛ ꜱᴛʏʟᴇ.  
» ᴀᴊᴏᴜᴛᴇᴢ ᴜɴᴇ ʟéɢᴇɴᴅᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ, ᴜɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ éʟéɢᴀɴᴛᴇ ᴇᴛ ʟᴀɪꜱꜱᴇᴢ-ᴍᴏɪ ꜱéǫᴜᴇɴᴄᴇʀ ᴠᴏꜱ ꜰɪᴄʜɪᴇʀꜱ à ʟᴀ ᴘᴇʀꜰᴇᴄᴛɪᴏɴ.  

ᴊᴇ ꜱᴜɪꜱ ʟà ᴘᴏᴜʀ ᴠᴏᴜꜱ, ᴀᴠᴇᴄ ᴛᴏᴜᴛᴇ ʟᴀ ᴅᴏᴜᴄᴇᴜʀ ᴇᴛ ʟᴀ ᴅéᴛᴇʀᴍɪɴᴀᴛɪᴏɴ ᴅ'ᴜɴᴇ ɴɪɴᴊᴀ ᴘʀêᴛᴇ à ᴀᴄᴄᴏᴍᴘʟɪʀ ꜱᴀ ᴍɪꜱꜱɪᴏɴ. ꜰᴀɪꜱᴏɴꜱ éǫᴜɪᴘᴇ ᴘᴏᴜʀ ᴜɴᴇ ᴇxᴘéʀɪᴇɴᴄᴇ ᴜɴɪǫᴜᴇ !</b>
"""


    FILE_NAME_TXT = """<b>» <u>ᴄᴏɴꜰɪɢᴜʀᴇʀ ʟᴇ ꜰᴏʀᴍᴀᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ</u></b>

<b>ᴠᴀʀɪᴀʙʟᴇs :</b>
➲ episode - ᴘᴏᴜʀ ʀᴇᴍᴘʟᴀᴄᴇʀ ʟᴇ ɴᴜᴍᴇ́ʀᴏ ᴅᴇ ʟ'ᴇᴘɪsᴏᴅᴇ  
➲ quality - ᴘᴏᴜʀ ʀᴇᴍᴘʟᴀᴄᴇʀ ʟᴀ ǫᴜᴀʟɪᴛᴇ́  

<b>‣ ᴘᴀʀ ᴇxᴀᴍᴘʟᴇ :- </b> <code> /autorename Suicide Squad [S02 - EPepisode - [Quality] [Dual] @hyoshmangavf </code>

<b>‣ /Autorename : ʀᴇɴᴏᴍᴍᴇᴢ ᴠᴏs ꜰɪʟᴇs ᴍᴜʟᴛɪᴍᴇᴅɪᴀ ᴇɴ ɪɴᴄʟᴜᴀɴᴛ ʟᴇs ᴠᴀʀɪᴀʙʟᴇs 'ᴇᴘɪsᴏᴅᴇ' ᴇᴛ 'ǫᴜᴀʟɪᴛᴇ́' ᴅᴀɴs vᴏᴛʀᴇ ᴛᴇxᴛᴇ, ᴘᴏᴇᴜʀ ᴇxᴛʀᴀɪʀᴇʀ l'ᴇᴘɪsᴏᴅᴇ ᴇᴛ ʟa ǫᴜᴀʟɪᴛᴇ́ ᴘʀᴇ́sᴇɴᴛs ᴅᴀɴs lᴇ ɴᴏᴍ ᴅᴇ ꜰɪʟᴇ ᴏʀɪɢɪɴᴀʟ.</b>"""


    ABOUT_TXT = f"""<b>❍ ᴍᴏɴ ɴᴏᴍ : <a href="https://t.me/hyoshassistantbot">ɢᴇ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ</a>  
❍ ᴅᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ : <a href="https://t.me/hyoshassistantBot">ᴘʀᴏᴘʀɪᴇ́ᴛᴀɪʀᴇ</a>  
❍ ɢɪᴛʜᴜʙ : <a href="https://github.com/ hyoshassistantBot">ᴘʀᴏᴘʀɪᴇ́ᴛᴀɪʀᴇ</a>  
❍ ʟᴀɴɢᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>  
❍ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇ́ᴇs : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏᴅʙ</a>  
❍ ʜᴇ́ʙᴇʀɢᴇ́ sᴜʀ : <a href="https://t.me/hyoshassistantbot">ᴠᴘs</a>  
❍ ᴄᴀɴᴀʟ ᴘʀɪɴᴄɪᴘᴀʟ : <a href="https://t.me/hyoshmangavf">ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>  

➻ ᴄʟɪǫᴜᴇᴢ sᴜʀ ʟᴇs ʙᴏᴜᴛᴏɴs ᴄɪ-ᴅᴇssᴏᴜs ᴘᴏᴜʀ ᴏʙᴛᴇɴɪʀ ᴅᴇ ʟ'ᴀɪᴅᴇ ᴇᴛ ᴅᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴs ʙᴀsɪǫᴜᴇs sᴜʀ ᴍᴏɪ.</b>"""


    THUMBNAIL_TXT = """<b><u>» ᴘᴏᴜʀ ᴅéꜰɪɴɪʀ ᴜɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ</u></b>
    
➲ /start : ᴇɴᴠᴏʏᴇᴢ ɴ'ɪᴍᴘᴏʀᴛᴇ ǫᴜᴇʟʟᴇ ᴘʜᴏᴛᴏ ᴘᴏᴜʀ ʟᴀ ᴅéꜰɪɴɪʀ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇᴍᴇɴᴛ ᴄᴏᴍᴍᴇ ᴍɪɴɪᴀᴛᴜʀᴇ.
➲ /del_thumb : ᴜᴛɪʟɪꜱᴇᴢ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ ᴘᴏᴜʀ ꜱᴜᴘᴘʀɪᴍᴇʀ ᴠᴏᴛʀᴇ ᴀɴᴄɪᴇɴɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ.
➲ /view_thumb : ᴜᴛɪʟɪꜱᴇᴢ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ ᴘᴏᴜʀ ᴠᴏɪʀ ᴠᴏᴛʀᴇ ᴍɪɴɪᴀᴛᴜʀᴇ ᴀᴄᴛᴜᴇʟʟᴇ.

ɴᴏᴛᴇ : ꜱɪ ᴀᴜᴄᴜɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ ɴ'ᴇꜱᴛ ᴇɴʀᴇɢɪꜱᴛʀéᴇ ᴅᴀɴꜱ ʟᴇ ʙᴏᴛ, ʟᴀ ᴍɪɴɪᴀᴛᴜʀᴇ ᴅᴜ ꜰɪᴄʜɪᴇʀ ᴏʀɪɢɪɴᴀʟ ꜱᴇʀᴀ ᴜᴛɪʟɪꜱéᴇ ᴘᴏᴜʀ ʟᴇ ꜰɪᴄʜɪᴇʀ ʀᴇɴᴏᴍᴍé."""

    CAPTION_TXT = """<b><u>» ᴘᴏᴜʀ ᴅéꜰɪɴɪʀ ᴜɴᴇ ʟéɢᴇɴᴅᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ ᴇᴛ ʟᴇ ᴛʏᴘᴇ ᴅᴇ ᴍéᴅɪᴀ</u></b>
    
<b>ᴠᴀʀɪᴀʙʟᴇs :</b>         
ᴛᴀɪʟʟᴇ: <code>{filesize}</code>  
ᴅᴜʀéᴇ: <code>{duration}</code>  
ɴᴏᴍ_ꜰɪʟᴇ: <code>{filename}</code>

➲ /set_caption : ᴘᴏᴜʀ ᴅéꜰɪɴɪʀ ᴜɴᴇ ʟéɢᴇɴᴅᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ.  
➲ /see_caption : ᴘᴏᴜʀ ᴠᴏɪʀ ᴠᴏᴛʀᴇ ʟéɢᴇɴᴅᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ.  
➲ /del_caption : ᴘᴏᴜʀ sᴜᴘᴘʀɪᴍᴇʀ ᴠᴏᴛʀᴇ ʟéɢᴇɴᴅᴇ ᴘᴇʀꜱᴏɴɴᴀʟɪꜱéᴇ.

» ᴘᴀʀ ᴇxᴀᴍᴘʟᴇ :- /set_caption ɴᴏᴍ ᴅᴇ ꜰɪʟᴇ: {filename}"""


    PROGRESS_BAR = """\n
<b>» ᴛᴀɪʟʟᴇ</b> : {1} | {2}  
<b>» ꜰᴀɪᴛ</b> : {0}%  
<b>» ᴠɪᴛᴇssᴇ</b> : {3}/s  
<b>» ᴇᴛᴀ</b> : {4}"""


    DONATE_TXT = """<blockquote>ᴍᴇʀᴄɪ ᴅᴇ mᴏɴᴛʀᴇʀ ᴅᴇ ʟ'ɪɴtéʀêt pᴏᴜʀ lᴇs dᴏɴs</blockquote>

<b><i>💞 Sɪ vᴏᴜs ᴀᴍᴇᴢ ɴᴏᴛʀᴇ bᴏᴛ, n'ʜéᴄɪtᴇz pᴀs à fᴀɪʀᴇ ᴜɴ dᴏɴ dᴇ n'iᴍᴘᴏʀᴛᴇ qᴜᴇl mᴏɴᴛᴀɴᴛ $10, $20, $50, $100, ᴇᴛᴄ.</i></b>

Lᴇs dᴏɴs sᴏɴt vʀᴀɪᴍᴇɴᴛ ᴀpᴘʀéᴄɪéᴇs ᴇᴛ ᴀɪᴅᴇɴᴛ ᴀᴜ dᴇᴠᴇʟᴏᴘᴘᴇᴍᴇɴᴛ dᴜ bᴏᴛ.

<u>Vᴏᴜs pᴏᴜᴠᴇz ᴀʟᴇʀᴛᴇᴢ ᴜɴ ᴅᴏɴ </u>

Pᴀʏᴇʀ ɪᴄɪ - <code> @hyoshassistantBot </code>

Sɪ vᴏᴜs lᴇ sᴏʏᴇz, vᴏᴜs pᴏᴜᴠᴇz nᴏᴜs ᴇɴᴠᴏʏᴇʀ dᴇs cᴀᴘᴛᴜʀᴇs d'écrᴀɴs
à - @hyoshassistantBot"""


    PREMIUM_TXT = """<b>ᴀᴍéʟɪᴏʀᴇᴢ nᴏᴛʀᴇ sᴇʀᴠɪᴄᴇ ᴘʀᴇᴍɪᴜᴍ et prᴏfɪᴛᴇᴢ de fᴜɴᴄᴛɪᴏɴɴᴀʟɪᴛés ᴇxᴄʟᴜsɪᴠᴇs :
○ Rᴇɴᴏᴍᴍᴀɢᴇ ɪʟʟɪᴍɪᴛé : rᴇɴᴏᴍᴍᴇᴢ ᴀᴜᴛᴀɴᴛ de fɪʟᴇs qᴜᴇ vᴏᴜs lᴇ sᴏʜᴀɪᴛᴇs sᴀɪɴs ᴀᴜcᴜɴᴇ rᴇsᴛʀɪᴄtɪᴏɴ.
○ ᴀᴄᴄèss ᴀɴᴛɪᴄɪᴘé : sᴏʏᴇᴢ le prɪᴍɪᴇʀ à tᴇsᴛᴇʀ et ᴜsᴀɢᴇʀ nᴏᴛʀᴇs dᴇʟᴀᴛᴇs fᴜɴᴄᴛɪᴏɴɴᴀʟɪᴛéᴇs ᴀᴠᴀɴᴄᴇᴇs ᴀᴠᴀɴᴛ tᴏᴜᴛ ʟᴇ mᴏɴᴅᴇ.

• Uᴛɪʟɪsᴇᴢ /plan pᴏᴜʀ vᴏɪʀ tᴏᴜs nᴏᴛʀᴇs pʟᴀɴs ᴇɴ ᴜɴᴇ fᴏɴᴄᴛɪᴏɴ ᴇᴄʜᴇᴍᴇ.

➲ Pʀɪᴇʀᴇ ᴇᴛᴀᴘᴇ : pᴀʏᴇʀ ʟᴇ mᴏɴᴛᴀɴᴛ cᴏʀʀᴇspᴏɴᴅᴀɴᴛ à vᴏᴛʀᴇ pʟᴀɴ pʀéfᴇré à 

➲ Dᴇᴜxɪèmᴇ ᴇᴛᴀᴘᴇ : prᴇɴᴇᴢ ᴜɴᴇ cᴀᴘᴛᴜʀᴇ d'écran de vᴏᴛʀᴇ pᴀʏᴇᴍᴇɴᴛ et ᴘᴀʀᴀɢᴇᴢ-ʟᴀ ᴅɪʀᴇᴄᴛᴇᴍᴇɴᴛ ɪᴄɪ : @hyoshassistantBot 

➲ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ : ᴏᴜ tᴇ́ʟᴇᴄʜᴇʀ ʟᴀ cᴀᴘᴛᴜʀᴇ d'écran ɪᴄɪ et rᴇᴘᴏɴᴅᴇᴢ ᴀᴠᴇᴄ lᴀ cᴏᴍᴍᴀɴᴅᴇ /bought.

Vᴏᴛʀᴇ pʟᴀɴ pʀᴇᴍɪᴜᴍ sᴇʀᴀ ᴀᴄᴛɪᴠé ᴀᴘʀès véʀɪꜰɪᴄᴀᴛɪᴏɴ.</b>"""


    PREPLANS_TXT = """<b>👋 Sᴀʟᴜᴛ,

🎖️ <u>ᴘʟᴀɴs ᴅɪsᴘᴏɴɪʙʟᴇs</u> :

Tᴀʀɪғɪᴄᴀᴛɪᴏɴ :
➜ Pʀᴇᴍɪᴜᴍ mᴇɴsᴜᴇʟ : 3.99$/mᴏɪs
➜ Pʀᴇᴍɪᴜᴍ qᴜᴏᴛɪᴅɪᴇɴ : 0.99/jᴏᴜʀ
➜ Pᴏᴜʀ l'ʜéʙᴇʀɢᴇᴍᴇɴᴛ ᴅᴇ bᴏᴛ : cᴏɴᴛᴀᴄᴛᴇᴢ @hyoshassistantBot

➲ Pᴀʏeʀ ɪᴄɪ - <code> @hyoshassistantBot </code>

‼️Tᴇ́ʟᴇᴄʜargᴇʀ ʟᴀ cᴀᴘᴛᴜʀᴇ ᴅᴇ ʟ'ecrᴀn ᴅᴜ ᴘᴀʏᴇᴍᴇɴᴛ ɪᴄɪ ᴇᴛ ʀᴇᴘᴏɴᴅᴇᴢ ᴀᴠᴇᴄ lᴀ cᴏᴍᴍᴀɴᴅᴇ /bought.</b>"""


    HELP_TXT = """<b>Vᴇᴏɪᴄɪ ʟᴇ ᴍᴇɴᴜ ᴅ'ᴀɪᴅᴇ ᴀᴠᴇᴄ ʟᴇs cᴏᴍᴍᴀɴᴅᴇs ɪᴍᴘᴏʀᴛᴀɴᴛᴇs :

Fᴏɴᴄᴛɪᴏɴɴᴀʟɪᴛᴇs ɪᴍᴘʀᴇssɪᴏɴɴᴀɴᴛᴇs🫧

Lᴇ bᴏᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴇsᴛ ᴜɴ ᴏᴜᴛɪʟ ᴘʀᴀᴛɪqᴜᴇ qᴜɪ vᴏᴜs ᴀɪᴅᴇ ᴀ ʀᴇɴᴏᴍᴍᴇʀ ᴇᴛ ɢᴇʀᴇʀ vᴏᴛʀᴇs fɪʟᴇs ᴇᴀsɪʟʟᴇᴍᴇɴᴛ.

➲ /Autorename : ʀᴇɴᴏᴍᴍᴇʀ ᴀᴜᴛᴏᴍᴀᴛɪqᴜᴇᴍᴇɴᴛ vᴏᴛʀᴇs fɪʟᴇs.
➲ /Metadata : cᴏᴍᴍᴀɴᴅᴇs pᴏᴜʀ ᴀᴄᴛɪᴠᴇʀ/ᴅᴇsᴀᴄᴛɪᴠᴇʀ ʟᴇs métᴀᴅᴀᴛᴀs.
➲ /Help : ᴏʙᴛᴇɴɪʀ ᴅᴇ ʟ'ᴀɪᴅᴇ ʀᴀᴘɪᴅᴇ.</b>"""


    SEND_METADATA = """
<b>--ᴘᴀʀᴀᴍéᴛʀᴇs ᴅᴇs ᴍéᴛᴀᴅᴀᴛᴀ--</b>

➜ /metadata : ᴀᴄᴛɪᴠᴇʀ ᴏᴜ supprimer ʟᴇs ᴍéᴛᴀᴅᴀᴛᴀᴛᴀ.

<b>ᴅéꜱᴄʀɪᴘᴛɪᴏɴ</b> : ʟᴇs ᴍéᴛᴀᴅᴀᴛᴀᴛᴀ ᴠᴏɴᴛ ᴍᴏᴅɪғɪᴇʀ ʟᴇs ꜰɪʟᴇs ᴠɪᴅéᴏ ᴍᴋᴠ, y ᴄᴏᴜᴍᴘʀᴇ ᴛᴏᴜᴛs ʟᴇs ᴛɪᴛʀᴇs ᴀᴜᴅɪᴏ, sᴛʀᴇᴀᴍs ᴇᴛ sᴜʙᴛɪᴛʀᴇs.""" 


    SOURCE_TXT = """
<b>Salut,
  Jᴇ sᴜɪs ᴜɴ bᴏᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ,
ᴜɴ bᴏᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ.</b>

ᴇᴄʀɪᴛ ᴇɴ ᴘʏᴛʜᴏɴ ᴀᴠᴇᴄ ʟ'ᴀɪᴅᴇ ᴅᴇ :
[Pyrogram](https://github.com/pyrogram/pyrogram)
[Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)
ᴇᴛ ᴜᴛɪʟɪsᴀɴᴛ [Mongo](https://cloud.mongodb.com) cᴏᴍᴇ ʙᴀsᴇ ᴅᴇ ᴅᴏɴᴎᴇᴇᴇᴏᴠᴇᴇ

<b>Voici mon cᴏᴅᴇ sᴏᴜʀᴄᴇ :</b> [GitHub](https://github.com/kalebavincent/autorenamebot)

ʟᴇ bᴏᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ ᴇsᴛ sᴏᴜʀ ʟɪᴄᴇɴᴄᴇ [MIT](https://github.com/kalebavincent/autorenamebot/blob/main/LICENSE).
© 2025 | [Support Chat](https://t.me/tout_manga_confondu), ᴛᴏᴜs ᴅʀᴏɪᴛs ʀéserᴠéᴇᴇᴇ
""" 

