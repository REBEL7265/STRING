from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""ππ΄π»π²πΎπΌπ΄ ππ΄π±π΄π»π±πΎπ ππΎ πΊπ°π π·π°π° π°πΏ π»πΎπΆ @REBELBOT_SUPPORT""")
print("""KΙͺΙ΄α΄ΚΚ α΄Ι΄α΄α΄α΄Κ Κα΄α΄Κ α΄α΄α΄α΄ΙͺΚs α΄α΄ α΄α΄Ι΄α΄ΙͺΙ΄α΄α΄ ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here Is Your String Session For Using REBEL Userbot\n(**Tap to copy it**)π \n\n `{session}` \n\n And Visit @REBELBOT_SUPPORT For Any Help !"
   )

   print(
       "Thanks for Choosing REBELBOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
   )
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry"
  )
  print("")
  continue
 break
