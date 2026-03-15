#projekt8
PostgreSQL /Alembic /FastAPI/ Docker Compose

# Klinikum-Backend-API

Bei diesem Projekt handelt es sich um eine Backend-REST-API zur Verwaltung eines kleinen klinischen Systems.
Es wurde entwickelt, um Backend-Entwicklungskonzepte wie Datenbankdesign, Authentifizierung und Containerumgebungen zu üben.

## Technologien

* Python
* FastAPI
* PostgreSQL
* Docker und Docker Compose
* JWT-Authentifizierung
* Alembic (Datenbankmigrationen)

## Funktionen

* Patientenmanagement
* Ärztemanagement
* Terminvereinbarung
* Benutzerauthentifizierung mit JWT
* Rollenbasierte Zugriffskontrolle (Administrator / Benutzer)
* Paginierung für API-Endpunkte
* Datenbankindizierung für mehr Leistung
* Datenbankmigrationen mit Alembic

## Projektstruktur

„
App/
  API/
      patienten.py
      Ärzte.py
      Termine.py
      auth.py

  Schemata/
      patient.py
      doctor.py
      Termin.py
      user.py

  Dienstleistungen/
      auth_services.py

  Datenbank.py

Destillierkolben/
  Versionen/

main.py
docker-compose.yml
Anforderungen.txt
„

## Das Projekt ausführen

### Starten Sie die Container

„
Docker komponieren --build
„

Die API wird verfügbar sein unter:

„
http://localhost:8000
„

API-Dokumentation:

„
http://localhost:8000/docs
„

## Datenbank

Das Projekt verwendet PostgreSQL in Docker.

Table:

* Benutzer
* Patienten
* Ärzte
* Termine

## Authentifizierung

Die Authentifizierung erfolgt mit JWT-Tokens.

Durchfluss:

1. Registrieren Sie einen Benutzer
2. Anmelden
3. JWT-Token empfangen
4. Verwenden Sie das Token, um auf geschützte Endpunkte zuzugreifen


---

Dieses Projekt wurde im Rahmen des Backend-Lernens und der Vorbereitung auf die berufliche Weiterentwicklung erstellt.
