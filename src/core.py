from fbchat import Client, log
from fbchat.models import *
import getpass

class __actions__(Client):
	selfRead = False
	
	def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):

		def __msg__(text: str = "", isReply: bool = False):
			if isReply:
				self.send(Message(text = text, reply_to_id = mid), thread_id = thread_id, thread_type = thread_type)
			else:
				self.send(Message(text = text), thread_id = thread_id, thread_type = thread_type)

		if author_id != self.uid or self.selfRead:
			if(message == "test mode"):
				__msg__("Hello World")


class login:
	def __init__(self, username: str = "", password: str = ""):
		self.username = username
		self.password = password
		if(username == "" or password == ""):
			self.username = input("Enter your username: ")
			self.password = getpass.getpass("Enter your password: ")

		act = __actions__(self.username, self.password)
		act.listen()
