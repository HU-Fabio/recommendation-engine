# Bussiness rules voor Recommendation Engine

Dit is de repository voor mijn opdracht Structured Programming.

# Configuratie
In `database/connection.py` moet de database connection gemaakt worden dus
vul daar je gegevens in.

# Libraries
Ik gebruik TQDM om progress te zien van hoe lang het nog duurt om alles
te importeren naar de table.
Om het te installeren run de volgende command:

`pip install tqdm`

`pip install csv`

Ik gebruik ook de database van Nick en gebruik MySQL als driver

# Hoe het programma starten
1. Start `main.py`
2. kies `1. Maak recommendation data klaar`
3. importeer de csvs uit `engines/csv/` in de database met de volgende tabelnamen:
`recommendations_collaboritive`
`recommendations_content_based`
4. Daarna werkt het programma.
