class Software:
	ID = ""
	displaytitle = ""
	description = ""
	fullurl = ""
	aliases = []

	def __init__(self, ID, displaytitle, description, fullurl, aliases, techniques):
		self.ID = ID
		self.displaytitle = displaytitle
		self.description = description
		self.fullurl = fullurl
		self.aliases = aliases
		self.groups = {}
		self.techniques = {tech['fulltext'].split('/')[1]: tech for tech in techniques}

	def __str__(self):
		return f"{self.ID}: {self.displaytitle}"

	def __repr__(self):
		return f"{self.ID}: {self.displaytitle}"

	def search(self,query):
		pass