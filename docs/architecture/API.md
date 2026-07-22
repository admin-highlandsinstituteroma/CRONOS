# 📅 CRONOS

# REST API Specification

Version 1.0

---

# Principi

- API First
- RESTful
- JSON come formato standard
- Versionamento tramite `/api/v1`
- Tutte le risposte utilizzano codici HTTP standard

---

# Base URL

/api/v1

---

# Health

GET /health

Risposta:

200 OK

```json
{
  "status": "ok"
}
```

---

# Version

GET /version

Restituisce:

- nome servizio
- versione
- build
- data build

---

# Calendars

GET /calendars

Elenco calendari.

POST /calendars

Crea calendario.

GET /calendars/{id}

Dettaglio.

PUT /calendars/{id}

Aggiornamento.

DELETE /calendars/{id}

Eliminazione.

---

# Events

GET /events

POST /events

GET /events/{id}

PUT /events/{id}

DELETE /events/{id}

---

# Planning

GET /planning

Restituisce il planning completo.

POST /planning/generate

Genera il planning.

GET /planning/pdf

Genera PDF.

---

# Resources

GET /resources

POST /resources

GET /resources/{id}

PUT /resources/{id}

DELETE /resources/{id}

---

# Locations

GET /locations

POST /locations

GET /locations/{id}

---

# People

GET /people

POST /people

GET /people/{id}

---

# Organizations

GET /organizations

POST /organizations

GET /organizations/{id}

---

# Workflows

GET /workflows

POST /workflows

PUT /workflows/{id}

---

# Notifications

GET /notifications

POST /notifications

---

# Error Format

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Resource not found"
  }
}
```

---

# Versioning

Le modifiche incompatibili saranno pubblicate come:

- /api/v1
- /api/v2

Le modifiche retrocompatibili non cambiano la versione principale.
