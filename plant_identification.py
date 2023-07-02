# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd 
import genanki
#%%

## file = "/Users/alexandralazar/Downloads/plant_data.csv"

## sheet_url = "https://docs.google.com/spreadsheets/d/1pqHX1_9qDMt50_idd367C6yx5HIbrOKBMuySZIvt5ok/export?format=csv&gid=0"

sheet_id = "1rUoi-5WyhQChJxctmCVQriK2jj_4u3cLpp6VmQXQkpE"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

#%%

model = genanki.Model(
  1,
  'Simple Model',
  fields=[
    {'name': 'Plant image'},
    {'name': 'Plant name'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<img src="{{Plant image}}" />',
      'afmt': '{{FrontSide}}<hr id="answer">{{Plant name}}',
    },
  ],
  css = ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n}\n",
)

deck = genanki.Deck(
  2059400110,
  'Plant Identification'
)


#%%

for index, row in df.iterrows():
    note = genanki.Note(
      model=model,
      fields=[row["Images "], row["Names "]]
    )
    deck.add_note(note)


#%%

genanki.Package(deck).write_to_file('/Users/alexandralazar/Downloads/output.apkg')