# -*- coding: utf-8 -*-
"""
*************************************
*       🚀 BOT DIBUAT OLEH: GILANG PORTOFOLIO                   *
*🌟 JOIN CHANNEL TELEGRAM UNTUK MENGETAHUI UPDATE TERBARU 🌟    *
*📢 Disini >> [GPP | CHANNEL](https://t.me/+RGKsWtrOBVE5NGJl)   *
*📧 Email: Gilang.portofolioo@gmail.com                         *
*************************************
Copyright (c) 2024 Gilang Portofolio.
All rights reserved.

This code is licensed under the Gilang Portofolio License.
You may not use, distribute, or modify this code without explicit permission from the copyright holder.
"""

from telethon import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import User, Chat
import config  # Import konfigurasi dari file config.py
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Menggunakan variabel dari config.py
api_id = config.API_ID
api_hash = config.API_HASH
phone_number = config.PHONE_NUMBER
session_name = config.SESSION_NAME

# Membuat client pengguna
client = TelegramClient(session_name, api_id, api_hash)

async def display_and_confirm_chats():
    await client.start(phone_number)
    
    # Menampilkan header
    print(Fore.GREEN + """
    *************************************
    *       🚀 BOT DIBUAT OLEH: GILANG PORTOFOLIO                   *
    *🌟 JOIN CHANNEL TELEGRAM UNTUK MENGETAHUI UPDATE TERBARU 🌟    *
    *📢 Disini >> [GPP | CHANNEL](https://t.me/+RGKsWtrOBVE5NGJl)   *
    *📧 Email: Gilang.portofolioo@gmail.com                         *
    *************************************
    """)
    print(Fore.WHITE + "Bot ini berfungsi untuk menghapus akun Telegram yang sudah menghapus akunnya.")
    
    # Mendapatkan daftar obrolan
    dialogs = await client.get_dialogs()
    
    # Menyaring obrolan tanpa nama
    no_name_chats = [dialog for dialog in dialogs if not dialog.name]
    
    if not no_name_chats:
        print(Fore.WHITE + "Tidak ada obrolan tanpa nama yang ditemukan.")
        print(Fore.WHITE + 'Bot telah berhasil menutup. Cek aplikasi Anda untuk log penghapusan.')
        return

    # Menampilkan semua obrolan tanpa nama
    for dialog in no_name_chats:
        print(Fore.RED + f'ID: {dialog.id}, Nama: {dialog.name or "Tanpa Nama"}, Tipe: {dialog.entity.__class__.__name__}')
    
    # Konfirmasi untuk menghapus semua obrolan tanpa nama
    confirm = input(Fore.WHITE + f'\nTotal {Fore.RED}{len(no_name_chats)} obrolan tanpa nama ditemukan. Apakah Anda ingin menghapus semua obrolan ini? [y/n]: ')
    
    if confirm.lower() == 'y':
        for dialog in no_name_chats:
            try:
                if isinstance(dialog.entity, (User, Chat)):
                    # Menghapus riwayat pesan di obrolan jika jenisnya User atau Chat
                    print(Fore.WHITE + f'Menghapus riwayat pesan di obrolan dengan ID: {dialog.id}, Nama: {dialog.name or "Tanpa Nama"}')
                    await client(DeleteHistoryRequest(peer=dialog.entity, max_id=0))
                    print(Fore.RED + f'Obrolan dengan ID: {dialog.id} telah dihapus.')
                else:
                    print(Fore.WHITE + f'Jenis obrolan dengan ID: {dialog.id} tidak didukung untuk dihapus.')
            except Exception as e:
                print(Fore.RED + f'Gagal menghapus obrolan dengan ID: {dialog.id}, Error: {e}')
        print(Fore.RED + f'Total {len(no_name_chats)} obrolan telah berhasil dihapus.')
    else:
        print(Fore.WHITE + 'Tidak ada obrolan yang dihapus.')

    print(Fore.WHITE + 'Bot telah berhasil menutup. Cek aplikasi Anda untuk log penghapusan.')

# Menjalankan fungsi utama
client.loop.run_until_complete(display_and_confirm_chats())
