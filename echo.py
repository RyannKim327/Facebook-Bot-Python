from fbchat import Client, log
from fbchat.models import *
import re

class _EchoBot(Client):
	selfRead = False
	commands = []

	def selfRead(self, data=False):
		self.selfRead = data

	def addCommand(self, file="", data={}):
		self.commands.append({
			"file": file,
			"data": data
		})
	def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):
		replied_from = None
		replied_text = None
		if message_object.replied_to != None:
			reply = message_object.replied_to
			replied_from = reply.author
			replied_text = reply.text
		print(f"Message come in {message_object.replied_to}")
			
		def send(msg="", mid=""):
			self.send(Message(text = msg, reply_to_id = mid), thread_id=thread_id, thread_type=thread_type)
		
		if self.selfRead or author_id != self.uid:
			for i in self.commands:
				command = "^" + i['data']['command'] + "$"
				if re.search(command, message):
					send(f"Message: {replied_text}", mid)
					send("This may work with no reply")

class Execute:
	def __init__(self, email="", password=""):
		self.c = _EchoBot(email, password)
	
	def setSelfListen(self, isSelfListen=False):
		self.c.selfRead(isSelfListen)

	def addCommand(self, file="", data={}):
		self.c.addCommand(file, data)

	def start(self):
		self.c.listen()