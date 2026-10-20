import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# MongoDB URI & Database Name
MONGO_URI = os.environ.get("MONGO_URI", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "FileStoreBot")

# Channel ID where source files are stored permanently
DB_CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", ""))

# Owner/Admin Telegram Numeric IDs (comma-separated if multiple)
ADMINS = [int(x) for x in os.environ.get("ADMINS", "7284759394").split()]

# Image URLs matching your design layouts
FORCE_SUB_IMAGE = os.environ.get("FORCE_SUB_IMAGE", "https://files.catbox.moe/jg30k8.jpg")  # Images 1 & 2[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
ABOUT_IMAGE = os.environ.get("ABOUT_IMAGE", "https://files.catbox.moe/5ho5yp.jpg")          # Image 3[span_5](start_span)[span_5](end_span)

# File Auto Delete Time in Seconds (5 minutes = 300 seconds)
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "300"))
