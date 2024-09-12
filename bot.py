import json
from telethon import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.sessions import StringSession
from telethon.tl.types import User, Chat

# Membaca file konfigurasi
with open('config.json') as f:
    config = json.load(f)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']

session_name = 'user_session'
client = TelegramClient(session_name, api_id, api_hash)

async def display_and_confirm_chats():
    await client.start(phone_number)
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        if not dialog.name:
            print(f'ID: {dialog.id}, Nama: {dialog.name or "Tanpa Nama"}, Tipe: {dialog.entity.__class__.__name__}')
            confirm = input(f'Apakah Anda ingin menghapus obrolan ini? (ID: {dialog.id}, Nama: {dialog.name or "Tanpa Nama"}) [y/n]: ')
            if confirm.lower() == 'y':
                try:
                    if isinstance(dialog.entity, (User, Chat)):
                        print(f'Menghapus riwayat pesan di obrolan dengan ID: {dialog.id}, Nama: {dialog.name or "Tanpa Nama"}')
                        await client(DeleteHistoryRequest(peer=dialog.entity, max_id=0))
                        print('Obrolan telah dihapus.')
                    else:
                        print(f'Jenis obrolan dengan ID: {dialog.id} tidak didukung untuk dihapus.')
                except Exception as e:
                    print(f'Gagal menghapus obrolan dengan ID: {dialog.id}, Error: {e}')
            else:
                print('Obrolan tidak dihapus.')

    print('Selesai memproses obrolan.')

client.loop.run_until_complete(display_and_confirm_chats())
