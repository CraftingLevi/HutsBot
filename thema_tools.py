import requests
import pandas as pd
import io
import numpy as np

class thema_sheet():

	def __init__(self):
		df = pd.read_csv( \
							io.BytesIO(\
								requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQphpe7xXb0iv7Dgf_nhcMu_givLYW2lriNLM7CLTFbukBh3ZGKvrq7UwvV7E53LLEA68sXFA-jAW5z/pub?gid=0&single=true&output=csv').content)\
								)
		self.content = df.dropna(subset=[df.columns[1]])
		roll = np.random.randint(low=0, high=max(self.content.index)+1)
		thema_content = self.content.iloc[roll]
		self.thema = thema_content[self.content.columns[1]]
		self.dresscode = thema_content[self.content.columns[2]]
		self.muziek_thema= thema_content[self.content.columns[3]]
		self.drank = thema_content[self.content.columns[4]]
		self.voeding = thema_content[self.content.columns[5]]
		self.omschrijving = thema_content[self.content.columns[6]]

	def drawn_thema_to_string(self):
		thema_string = f"Een thema is gerolled! Het aankomende thema is {self.thema}\n"
		if not pd.isna(self.dresscode):
			thema_string += f"Men zal gekleed komen in de stijl '{self.dresscode}'\n"
		if not pd.isna(self.muziek_thema):
			thema_string += f"De deuntjes van de avond zullen klinken naar {self.muziek_thema} \n"
		if not pd.isna(self.drank):
			thema_string += f"Drank zal vloeien! Ditmaal in de vorm van {self.drank} \n"
		if not pd.isna(self.voeding):
			thema_string += f"Mogelijk zijn er ook versnaperingen, zoals {self.voeding} \n"
		if not pd.isna(self.omschrijving):
			thema_string += f"Een korte omschrijving van dit thema: {self.omschrijving} \n"
		return  thema_string

if __name__ == '__main__':
	t = thema_sheet()
	print(t.drawn_thema_to_string())