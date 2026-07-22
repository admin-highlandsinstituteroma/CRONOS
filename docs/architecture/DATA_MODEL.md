# 📅 CRONOS

# Domain Model

Version 1.0

---

# Filosofia

CRONOS non gestisce calendari.

Gestisce entità organizzative che evolvono nel tempo.

Ogni oggetto del sistema possiede:

- un'identità
- uno stato
- relazioni con altre entità
- una cronologia

---

# Entità principali

## Organization

Rappresenta un'organizzazione.

Esempi:

- Highlands Institute
- Dipartimento IT
- Direzione
- Segreteria

---

## Person

Qualsiasi persona coinvolta.

Può assumere uno o più ruoli.

---

## Role

Definisce le responsabilità.

Esempi:

- IT Coordinator
- Teacher
- Student
- Parent
- Administrator

---

## Calendar

Contenitore logico di eventi.

Tipologie:

- Academic
- Operational
- Training
- Personal
- Resource

---

## Event

Elemento fondamentale del sistema.

Ogni evento possiede almeno:

- titolo
- descrizione
- data
- durata
- organizzatore
- partecipanti
- stato
- priorità

---

## Resource

Qualsiasi risorsa prenotabile.

Ad esempio:

- Aula
- Laboratorio
- Apple TV
- Carrello iPad
- Sala Riunioni

---

## Location

Luogo fisico.

---

## Attachment

Documenti collegati.

---

## Workflow

Descrive il ciclo di vita operativo.

Esempio:

Bozza

↓

Revisione

↓

Approvazione

↓

Pubblicazione

↓

Archiviazione

---

## Notification

Messaggi generati automaticamente.

---

## Planning

Rappresenta un insieme coerente di eventi.

Può produrre:

- PDF
- Calendario
- Dashboard
- Report

---

# Relazioni

Organization

↓

Person

↓

Role

↓

Calendar

↓

Event

↓

Resource

↓

Attachment

---

# Principio fondamentale

Tutto deriva dall'Event.

Le altre entità descrivono:

- chi
- dove
- quando
- con cosa
- perché
- in quale stato
