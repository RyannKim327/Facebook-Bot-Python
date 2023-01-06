from fbchat import Client, log

class EchoBot(Client):
	selfRead = False
	def onMessage(self, mid, author_id, message, thread_id, thread_type, **kwargs):
		print(f"Message come in {message}")

		if self.selfRead or author_id != self.uid:
				self.sendMessage("This is an auto send message from fbchat", thread_id=thread_id, thread_type=thread_type)



class Execute:
	def __init__(self, email, password):
		c = EchoBot(email, password)
		c.listen()