# Plant identification Anki deck creator 

Script to make flashcards with plant images and latin/English names.

## Requirements

The requirements for this script are simple:
- `pandas` - for wrangling the 
- `genanki` - for generating anki notes and decks and packaging it.

## File format

The script expects the information to be provided in a CSV file with the columns:
- `Images ` 
- `Names `

NOTE: the stupid space.

Also note that the sheet had to be made public for pandas to be able to read it
using a URL.

