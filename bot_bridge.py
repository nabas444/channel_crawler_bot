from telethon import TelegramClient, events
from engine import is_relevant, format_job

seen_jobs = set()

# ----------------------------
# TELETHON SETUP
# ----------------------------
api_id = 39750632
api_hash = "7d6ce24ee258d5a8a1176168dc305c2a"

client = TelegramClient("session", api_id, api_hash)

# ----------------------------
# CHANNELS TO SCRAPE
# ----------------------------
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
    "internship_alerts_ethiopia",
    "devWithEyob",
    "Luna_moonmam",
    "Robi_makes_stuff",
    "zulu_tech",
    "selfmadecoder",
    "SoloDevChronicles",
    "gugutlogs",
    "DoughNutDrops",
    "kinfishfarms",
    "Natyiu0",
    "geeztechgroup",
    "Womentechmakersethiopia",
    "birukweb",
    "found_this",
    "chapidevtalks",
    "nahomssandbox",
    "brojects_and_resources",
    "Dagmawi_Babi",
    "eyuelzerostuff",
    "Mi_Ra_Ch",
    "BetaLabET",
    "debuggingepohul",
    "Merrys_Journey",
    "mr_naty",
    "naturaltheology",
    "nirvanaland7",
    "Su_ch_is_life",
    "Meron_Birhanu",
    "awaqiethiopia",
    "the_blogrammer",
    "bekacru_c",
    "KibneshAcademy",
    "Austererie",
    "doniverse",
    "TheKerVerse",
    "student_Union1",
    "insagovet",
]

# ----------------------------
# TARGET CHANNEL (YOUR OUTPUT)
# ----------------------------
TARGET_CHANNEL = "AT_Tech_stream"  # بدون @ is also fine in Telethon

# ----------------------------
# CORE PIPELINE
# ----------------------------
@client.on(events.NewMessage(chats=channels))
async def handler(event):
    print("📩 HANDLER TRIGGERED")

    try:
        message = event.message.message

        if not message or len(message) < 10:
            return

        job_id = hash(message)

        if job_id in seen_jobs:
            return

        seen_jobs.add(job_id)

        if is_relevant(message):
            formatted = format_job(message)

            print("\n" + "="*40)
            print("🚀 NEW POSTING")
            print("="*40)
            print(formatted)
            print("="*40)

            # ----------------------------
            # TELETHON SENDING (FIXED PART)
            # ----------------------------
            print("📤 Sending message...")

            entity = await client.get_entity("@AT_Tech_stream")

            await client.send_message(
                entity,
                formatted
            )

            print("✅ Message posted to channel!")

            print("✅ Posted successfully!")

        else:
            print("❌ ignored")

    except Exception as e:
        print("⚠️ Error:", e)


# ----------------------------
# START BOT
# ----------------------------
client.start()
print("🚀 Bot system running...")
client.run_until_disconnected()