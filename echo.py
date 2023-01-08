from fbchat import Client, log
from fbchat.models import *
import getpass
import re

class regex:
	def __init__(self, str=""):
		self.reg = "^" + str + "$"
	
	def search(self, str=""):
		return re.search(self.reg, str, re.IGNORECASE)
	
	def find(self, str=""):
		return re.findall(self.reg, str, re.IGNORECASE)

class _EchoBot(Client):
	selfRead = False
	commands = []
	prefix = "/"

	def regex(self, str=""):
		return "^" + str + "$"

	def selfRead(self, data=False):
		self.selfRead = data

	def setPrefix(self, data='/'):
		self.prefix = data

	def addCommand(self, file="", data={}):
		self.commands.append({
			"file": file,
			"data": data
		})
	def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):
		def send(msg="", mid=""):
			self.send(Message(text = msg, reply_to_id = mid), thread_id=thread_id, thread_type=thread_type)
		
		if author_id != self.uid or self.selfRead:
			for i in self.commands:
				data = i['data']
				command = regex(self.prefix + data['command'])
				type = ["message"]
				if(data.get('type')):
					type = data['type']
				
				if "message_reply" in type:
					replied_from = None
					replied_text = None
					if message_object.replied_to != None:
						reply = message_object.replied_to
						replied_from = reply.author
						replied_text = reply.text
					if replied_from == self.uid:
						if command.search(message):
							try:
								script = __import__("script/" + i['file'])
								script.Execution(mid, author_id, message, message_object, thread_id, thread_type)
							except:
								print("hello")
				elif "message" in type:
					if re.search(f"^{self.prefix}help$", message):
						msg = ""
						for j in self.commands:
							_data = j['data']
							title = _data['title']
							description = _data['description']
							command = _data['command']
							msg += f"{title} - [ {self.prefix}{command} ]\n    {description}\n\n"
						send(msg)
					

class Execute:
	def __init__(self, email="", password=""):
		if email == "" or password == "":
			email = input("Please enter your email/phone number/username: ")
			password = getpass.getpass("Enter your password: ")
		
		self.c = _EchoBot(email, password)
	
	def setSelfListen(self, isSelfListen=False):
		self.c.selfRead(isSelfListen)

	def addCommand(self, file="", data={}):
		self.c.addCommand(file, data)

	def setPrefix(self, data='/'):
		self.c.setPrefix(data)

	def start(self):
		self.c.listen()