"""全局配置文件"""
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# Telegram Bot 配置
BOT_TOKEN = os.getenv("BOT_TOKEN", "8575952388:AAHW6OVzp7TVZKiDxiE-03_ymld6UE63ZqQ")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "Sheeridverify7_bot")
CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/Sheeridverify7_bot")

# 管理员配置
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "7029370127"))

# 积分配置
VERIFY_COST = 1  # 验证消耗的积分
CHECKIN_REWARD = 1  # 签到奖励积分
INVITE_REWARD = 2  # 邀请奖励积分
REGISTER_REWARD = 1  # 注册奖励积分

# 帮助链接
HELP_NOTION_URL = "https://rhetorical-era-3f3.notion.site/dd78531dbac745af9bbac156b51da9cc"
