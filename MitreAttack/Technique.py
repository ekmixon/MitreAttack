class Technique:
	ID = ""
	displaytitle = ""
	technical_description = ""
	full_url = ""
	data_sources = []

	def __init__(self, ID, displaytitle, technical_description, data_sources, full_url, thetactics):
		self.ID = ID
		self.displaytitle = displaytitle
		self.technical_description = technical_description
		self.full_url = full_url
		self.data_sources = data_sources
		self.groups = {}
		self.software = {}
		self.tactics = {i['fulltext']: i for i in thetactics}

	def __str__(self):
		return f"{self.ID}: {self.displaytitle}"

	def __repr__(self):
		return f"{self.ID}: {self.displaytitle}"

	def search(self):
		pass