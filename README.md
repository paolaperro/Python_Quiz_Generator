# QuizLab

Un generatore di quiz in italiano per ripassare con 10 domande a scelta multipla. Puoi scrivere un argomento, per esempio **Python**, oppure incollare i tuoi appunti.

Alla fine trovi il punteggio, le risposte che hai scelto e la correzione con una breve spiegazione per domanda. Puoi ripetere lo stesso quiz direttamente dalla pagina.

## Avvio

Servono Python 3.14 o successivo, uv e una chiave API OpenAI.

1. Copia `.env.example` in `.env`.
2. Compila `OPENAI_API_KEY` e indica in `OPENAI_MODEL` un modello disponibile nel tuo account che supporti le risposte strutturate.
3. Avvia il progetto con questi comandi.

   ```sh
   uv sync --locked
   uv run python main.py
   ```

Apri [QuizLab in locale](http://127.0.0.1:8001). La [documentazione API](http://127.0.0.1:8001/docs) è disponibile a server avviato.

Il progetto usa FastAPI per la generazione e una pagina HTML con CSS e JavaScript per il quiz. Gli argomenti e gli appunti vengono inviati al servizio AI configurato. Verifica le risposte in caso di dubbi.
