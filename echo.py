from fbchat import Client, log
import re

class EchoBot(Client):
	selfRead = False
	commands = []

	def selfRead(self, data=False):
		self.selfRead = data

	def addCommand(self, file="", data={}):
		self.commands.append({
			"file": file,
			"data": data
		})
	
	def onMessage(self, mid, author_id, message, thread_id, thread_type, **kwargs):
		print(f"Message come in {message}")

		def send(msg=""):
			self.sendMessage(msg, thread_id=thread_id, thread_type=thread_type)

		if self.selfRead or author_id != self.uid:
			for i in self.commands:
				command = "^" + i['data']['command'] + "$"
				if re.search(command, message):
					send("This is an auto send message from fbchat")



class Execute:
	def __init__(self, email="", password=""):
		self.c = EchoBot(email, password)
	
	def setSelfListen(self, isSelfListen=False):
		self.c.selfRead(isSelfListen)

	def addCommand(self, file="", data={}):
		self.c.addCommand(file, data)

	def start(self):
		self.c.listen()