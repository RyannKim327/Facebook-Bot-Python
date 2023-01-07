from echo import Execute

# sample: a = Execute("09123456789", "Hello world")
a = Execute("<email>", "<password>")

a.setSelfListen(True)
a.addCommand("a", {
	"title": "Test",
	"description": "Test Mode",
	"command": "/test"
})
a.start()