# CRONOS Domain Relationships

Versione: 1.0

## Principio

Le entità di CRONOS non sono isolate.

Ogni entità è collegata alle altre attraverso relazioni ben definite.

---

## Evento

Un Evento:

- appartiene ad un Calendario
- ha un Workflow
- può avere uno o più Documenti
- coinvolge una o più Persone
- utilizza zero o più Risorse
- può generare zero o più Conflitti

---

## Calendario

Un Calendario:

- contiene molti Eventi

---

## Persona

Una Persona:

- può partecipare a molti Eventi
- può essere Organizzatore
- può essere Referente
- può essere Approvatore

---

## Risorsa

Una Risorsa:

- può essere assegnata a molti Eventi
- appartiene ad una Categoria

---

## Documento

Un Documento:

- appartiene ad un Evento
- rappresenta uno stato del Workflow

---

## Workflow

Ogni Workflow:

- appartiene ad un Evento
- attraversa gli stati:

Bozza

↓

Verifica

↓

Approvazione

↓

Pianificazione

↓

Protocollo

---

## Conflitto

Un Conflitto:

- appartiene ad un Evento
- può coinvolgere:

    - Persone
    - Risorse
    - Sale
    - Orari

