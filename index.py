from echo import Execute

# sample: a = Execute("09123456789", "HelloWorld")
# sample: a = Execute()
a = Execute()

a.setSelfListen(True)

a.setPrefix('!')

a.addCommand("a", {
	"title": "Test",
	"description": "Test Mode",
	"command": "test"
})

a.addCommand("gender", {
	"title": "Add gender",
	"description": "This is to identify if someone is male or female.",
	"command": "gender ([\w\S\D]+) as ([m|f]+)",
	"type": [
		"message",
		"message_reply"
	]
})

a.start()