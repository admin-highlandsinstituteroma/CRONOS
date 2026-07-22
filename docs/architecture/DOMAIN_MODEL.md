# CRONOS Domain Model

Versione: 1.0

## Missione

Il Domain Model definisce il linguaggio comune di CRONOS.

Ogni componente software, API, documento e interfaccia utilizza queste entità come riferimento unico.

---

# Entità principali

## Evento

Rappresenta qualsiasi attività pianificabile.

Esempi:

- Riunione
- Formazione
- Collegio Docenti
- Corso
- Esame
- Evento istituzionale

---

## Calendario

Contiene gli eventi.

Calendari iniziali:

- Pianificazione Bozze
- Pianificazione

---

## Persona

Qualsiasi soggetto coinvolto.

Ruoli possibili:

- Organizzatore
- Partecipante
- Referente
- Approvatore

---

## Risorsa

Ogni elemento prenotabile.

Categorie:

- Sala
- Laboratorio
- Aula
- Attrezzatura

---

## Workflow

Descrive il ciclo di vita dell'evento.

Bozza

↓

Verifica PDF

↓

Approvazione

↓

Pubblicazione

↓

Protocollo

---

## Documento

File prodotti durante il workflow.

Tipologie:

- PDF di verifica
- PDF protocollato
- Allegati

---

## Conflitto

Situazione che impedisce la pubblicazione.

Può riguardare:

- Persone
- Sale
- Attrezzature
- Orari

