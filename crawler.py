from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))          # <-- replace with your api_id
api_hash = os.getenv("API_HASH")  # <-- replace

client = TelegramClient("session", api_id, api_hash)

channels = [
    "ethio_job_vacancy1",
    "Ethiojobshubs",
    "etcareersjobs",
    "FrontierFinTech",
    "geezjobs_ethiopia",
    "ethiojobsofficial",
    "hahujobs",
    "opportunity_alerts",
    "enisrajobmatching",
    "mikijobsmj",
    "KelemTutors",
    "Genuistutors",
    "Derejaofficial",
    "hultprize_aau",
    "ALXFreelancerAcademy",
    "internship_alerts_ethiopia"
    "devWithEyob"
    "Luna_moonmam"
    "Robi_makes_stuff"
    "zulu_tech"
    "selfmadecoder"
    "SoloDevChronicles"
    "gugutlogs"
    "DoughNutDrops"
    "kinfishfarms"
    "Natyiu0"
    "geeztechgroup"
    "Womentechmakersethiopia"
    "birukweb"
    "found_this"
    "chapidevtalks"
    "nahomssandbox"
    "brojects_and_resources"
    "Dagmawi_Babi"
    "eyuelzerostuff"
    "Mi_Ra_Ch"
    "BetaLabET"
    "debuggingepohul"
    "Merrys_Journey"
    "mr_naty"
    "naturaltheology"
    "nirvanaland7"
    "Su_ch_is_life"
    "Meron_Birhanu"
    "awaqiethiopia"
    "the_blogrammer"
    "bekacru_c"
    "KibneshAcademy"
    "Austererie"
    "doniverse"
    "TheKerVerse"
    "student_Union1"
    "insagovet"
]

@client.on(events.NewMessage())
async def handler(event):
    print("\n📩 RAW MESSAGE RECEIVED")
    print("From:", event.chat.username)
    print("Text:", event.message.message)

client.start()
print("🚀 Listening to channels...")
client.run_until_disconnected()