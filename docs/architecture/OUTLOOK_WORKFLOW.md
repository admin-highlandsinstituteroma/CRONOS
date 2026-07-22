# CRONOS Outlook Workflow

Versione 1.0

## Principio

Microsoft Outlook / Microsoft 365 rappresenta la fonte ufficiale degli eventi.

CRONOS non sostituisce Outlook.

CRONOS governa il processo di programmazione, verifica, approvazione, pubblicazione e protocollazione degli eventi.

---

## Calendari

### Calendario Pianificazione Bozze

Contiene gli eventi in fase di:

- inserimento
- revisione
- correzione
- verifica
- approvazione

Non è condiviso con tutto il personale.

Rappresenta l'ambiente operativo di programmazione.

### Calendario Pianificazione

Contiene esclusivamente gli eventi approvati.

È condiviso con:

- docenti
- personale
- utenti autorizzati

Gestisce:

- partecipanti
- persone
- sale
- attrezzature
- risorse

Rappresenta il calendario istituzionale ufficiale.

---

## Workflow

1. Creazione evento nel Calendario Pianificazione Bozze
2. Selezione di un intervallo temporale
3. Recupero degli eventi in bozza nell'intervallo selezionato
4. Visualizzazione su dashboard HTML
5. Generazione PDF di verifica
6. Eventuale stampa cartacea
7. Revisione degli eventi
8. Approvazione dell'intervallo selezionato
9. Copia degli eventi approvati nel Calendario Pianificazione
10. Conservazione degli eventi originali nel Calendario Pianificazione Bozze
11. Generazione PDF definitivo
12. Invio del PDF al protocollo
13. Registrazione dell'esito della pubblicazione

---

## Dashboard HTML

La dashboard deve consentire:

- selezione data iniziale
- selezione data finale
- visualizzazione eventi in bozza
- anteprima HTML
- generazione PDF di verifica
- approvazione intervallo
- copia eventi nel calendario ufficiale
- generazione PDF definitivo
- visualizzazione esito operazione

---

## Shortcuts

Apple Shortcuts può richiamare le API CRONOS per:

- generare l'anteprima
- generare il PDF di verifica
- approvare un intervallo
- generare il PDF definitivo

Shortcuts non contiene la logica applicativa.

La logica rimane nel backend CRONOS.

---

## Regola di pubblicazione

L'approvazione non sposta gli eventi.

L'approvazione copia gli eventi dal Calendario Pianificazione Bozze al Calendario Pianificazione.

L'evento originale rimane nel calendario Bozze per garantire:

- tracciabilità
- confronto
- audit
- ricostruzione storica

---

## Identificazione degli eventi

Ogni evento pubblicato deve mantenere un riferimento all'evento originale in bozza.

Devono essere registrati almeno:

- ID evento bozza
- ID evento pubblicato
- data approvazione
- utente approvatore
- intervallo approvato
- data generazione PDF
- stato protocollo

---

## Stati operativi

- Draft
- Under Review
- Approved
- Published
- PDF Generated
- Protocol Pending
- Protocolled
- Rejected
- Cancelled

---

## MVP

La prima versione operativa deve permettere:

1. connessione a Microsoft 365
2. lettura del Calendario Pianificazione Bozze
3. selezione di un intervallo temporale
4. anteprima HTML degli eventi
5. generazione PDF di verifica
6. approvazione degli eventi
7. copia nel Calendario Pianificazione
8. generazione PDF definitivo

Funzioni ulteriori saranno sviluppate solo dopo il completamento di questo flusso.
