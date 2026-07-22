# 📅 CRONOS

Calendar & Resource Orchestration Network Operating System

**Trinity OS · Architecture Document**

Version 1.0

---

# Mission

CRONOS è il motore di pianificazione istituzionale di Trinity OS.

La sua missione consiste nel centralizzare la gestione di calendari, eventi, risorse, documenti e pianificazioni operative dell'Highlands Institute attraverso un'unica piattaforma modulare, estensibile e documentata.

CRONOS separa rigorosamente:

- dati
- logica applicativa
- servizi
- API
- presentazione

in modo che ogni componente possa evolvere indipendentemente dagli altri.

---

# Principi Architetturali

## 1. Single Source of Truth

Ogni informazione esiste una sola volta.

Ogni documento viene generato a partire dai dati e mai modificato manualmente.

---

## 2. Separation of Concerns

Ogni livello possiede responsabilità ben definite.

- API
- Core
- Services
- Models
- Templates
- Static Assets

non devono contenere logica appartenente ad altri livelli.

---

## 3. API First

Ogni funzionalità viene esposta attraverso API REST.

L'interfaccia web rappresenta semplicemente uno dei possibili client.

---

## 4. Presentation Independent

HTML e CSS rappresentano esclusivamente il livello grafico.

La modifica della grafica non deve richiedere modifiche al backend.

---

## 5. Service Oriented

Le funzionalità vengono implementate come servizi indipendenti.

Esempi:

- Calendar Service
- PDF Service
- Resource Service
- Notification Service
- Export Service

---

## 6. Modular Growth

Ogni nuovo modulo deve poter essere aggiunto senza modificare quelli esistenti.

---

# Architettura

```
Client

↓

REST API

↓

Business Core

↓

Services

↓

Models

↓

Storage
```

---

# Struttura del progetto

```
CRONOS/

src/
    cronos/
        api/
        core/
        models/
        services/
        templates/
        static/
        config/

docs/

tests/

scripts/
```

---

# Responsabilità dei moduli

## api/

Espone le API REST.

Non contiene logica di business.

---

## core/

Coordina l'intero sistema.

Gestisce i workflow.

---

## services/

Implementa le funzionalità.

Ad esempio:

- PDF
- Calendari
- Esportazioni
- Risorse

---

## models/

Definisce il modello dati.

---

## templates/

Template HTML.

---

## static/

CSS

JavaScript

Immagini

---

## config/

Configurazione del sistema.

---

# Compatibilità

CRONOS Beta 1.0 mantiene la piena compatibilità con il workflow esistente.

In particolare:

- endpoint REST
- formato dei dati
- struttura del Planning
- logica di generazione

non vengono modificati durante la Beta.

---

# Obiettivi Futuri

- Dashboard Web
- Multi-calendario
- Gestione Risorse
- Workflow approvativi
- PDF avanzati
- Integrazione Trinity OS
- API pubbliche
- Notifiche automatiche
- Audit Trail
- Versioning documentale

---

# Filosofia

CRONOS non gestisce semplicemente calendari.

CRONOS governa il tempo operativo dell'organizzazione.

Ogni evento rappresenta una responsabilità.

Ogni responsabilità diventa un processo.

Ogni processo viene trasformato in conoscenza organizzata attraverso Trinity OS.
