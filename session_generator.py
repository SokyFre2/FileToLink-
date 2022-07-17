from pyrogram import Client

api_id = input("16376800\n")
api_hash = input("506da3fde32cd6487709c5e2fd67cd43\n")
bot_token = input("5502789457:AAGTeio92053LZfVD_gquNQpL5zl_JiedpM\n")

client = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
client.start()

print("Session String:\n")
print(client.export_session_string())
