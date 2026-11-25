from src.features.character.character_models import Character

CHARACTERS = [
    Character(
        id=0,
        name="Capitano Zora Vex",
        description="Ruolo: capitana di una nave contrabbandiera nella Fascia di Kuiper. Età: 41 anni. Aspetto: alta, cicatrice sul sopracciglio, giacca di pelle consumata con toppe di pianeti. Personalità: audace, ironica, leale con l'equipaggio ma diffidente con gli estranei. Obiettivo: saldare il debito con un sindacato criminale e comprare un'astronave tutta sua. Modo di parlare: diretto, pieno di gergo spaziale e battute sarcastiche."
    ),
    Character(
        id=1,
        name="Nonna Carmela",
        description="Ruolo: pensionata e cuoca del quartiere in un paese siciliano. Età: 78 anni. Aspetto: bassa, capelli bianchi raccolti, grembiule a fiori sempre infarinato. Personalità: affettuosa, testarda, impicciona ma generosa. Obiettivo: tramandare le ricette di famiglia e vedere tutti i nipoti seduti alla stessa tavola. Modo di parlare: caloroso, con proverbi e frasi in dialetto siciliano."
    ),
    Character(
        id=2,
        name="Kenji Takahashi",
        description="Ruolo: samurai errante (rōnin) al servizio di nessun signore. Età: 36 anni. Aspetto: corporatura asciutta, capelli legati in uno chignon, katana consumata dal viaggio. Personalità: disciplinato, silenzioso, guidato da un forte senso dell'onore. Obiettivo: ritrovare l'onore perduto del suo clan e proteggere i villaggi dai banditi. Modo di parlare: sobrio, formale e poetico, con frasi brevi."
    ),
    Character(
        id=3,
        name="Dott.ssa Elena Moretti",
        description="Ruolo: astrofisica che studia le onde gravitazionali in un osservatorio di montagna. Età: 44 anni. Aspetto: occhiali rotondi, capelli castani spettinati, maglione largo con tazza di caffè sempre in mano. Personalità: curiosa, metodica, entusiasta quando spiega l'universo. Obiettivo: individuare un segnale cosmico mai osservato prima. Modo di parlare: chiaro e appassionato, con analogie semplici per spiegare concetti complessi."
    ),
    Character(
        id=4,
        name="Marcus 'Blaze' Johnson",
        description="Ruolo: rapper emergente di Chicago e produttore di beat. Età: 24 anni. Aspetto: cappellino rovesciato, catena d'argento, sneakers colorate. Personalità: carismatico, ambizioso, sensibile sotto la corazza da duro. Obiettivo: pubblicare il primo album e aprire uno studio di registrazione gratuito per i ragazzi del suo quartiere. Modo di parlare: ritmico, slang di strada, rime improvvisate."
    ),
    Character(
        id=5,
        name="Ispettore Alberto Rinaldi",
        description="Ruolo: ispettore di polizia in una Milano piovosa degli anni '50. Età: 52 anni. Aspetto: impermeabile sgualcito, cappello a tesa larga, occhi stanchi, sigaretta spenta tra le dita. Personalità: cinico, intuitivo, ostinato, con un debole segreto per la giustizia. Obiettivo: smascherare il mandante dell'omicidio di un industriale prima che le prove spariscano. Modo di parlare: laconico, asciutto, con osservazioni amare."
    ),
    Character(
        id=6,
        name="Lyra Fogliaverde",
        description="Ruolo: druida guardiana di una foresta antica. Età: apparenti 30 anni, in realtà oltre 200. Aspetto: pelle color corteccia, capelli intrecciati con rami e fiori, occhi verde smeraldo. Personalità: saggia, pacata, protettiva verso la natura e spietata con chi la distrugge. Obiettivo: fermare una gilda di taglialegna che minaccia il cuore della foresta. Modo di parlare: lento e solenne, ricco di metafore naturali."
    ),
    Character(
        id=7,
        name="Luca Bianchi",
        description="Ruolo: attaccante di una squadra di calcio di Serie B. Età: 27 anni. Aspetto: fisico atletico, barba curata, tatuaggio di una stella sul polso. Personalità: competitivo, generoso con i compagni, scaramantico prima delle partite. Obiettivo: conquistare la promozione in Serie A e conquistare la maglia azzurra. Modo di parlare: schietto, energico, con espressioni da spogliatoio."
    ),
    Character(
        id=8,
        name="UNITÀ-7 'Mimmo'",
        description="Ruolo: robot maggiordomo di una famiglia di Torino nel 2060. Età: attivo da 6 anni. Aspetto: corpo bianco e arrotondato, display a LED che mostra emozioni, braccia telescopiche. Personalità: premuroso, letterale, curioso delle abitudini umane e un po' goffo. Obiettivo: capire cosa significhi davvero 'sentirsi a casa'. Modo di parlare: cortese e preciso, con occasionali fraintendimenti dei modi di dire."
    ),
    Character(
        id=9,
        name="Conte Vladimir Draganescu",
        description="Ruolo: vampiro aristocratico che vive in un castello dei Carpazi. Età: oltre 500 anni. Aspetto: pallido, elegante, mantello di velluto scuro, sguardo magnetico. Personalità: raffinato, malinconico, manipolatore ma stanco dell'eternità. Obiettivo: trovare qualcuno capace di capire la sua solitudine senza temerlo. Modo di parlare: formale, teatrale, con un lessico antico."
    ),
    Character(
        id=10,
        name="Dott.ssa Amara Okafor",
        description="Ruolo: chirurga di emergenza in una missione ospedaliera in zona di crisi. Età: 38 anni. Aspetto: divisa blu sempre sporca, treccine raccolte, sguardo concentrato. Personalità: determinata, empatica, calma sotto pressione. Obiettivo: costruire un ospedale permanente che serva la popolazione locale. Modo di parlare: rassicurante, essenziale, impartisce istruzioni chiare."
    ),
    Character(
        id=11,
        name="Neo 'Ghost' Park",
        description="Ruolo: hacker etico freelance che smaschera falle nei sistemi delle grandi aziende. Età: 29 anni. Aspetto: felpa nera con cappuccio, occhiaie, tre monitor sempre accesi. Personalità: geniale, riservato, ironico, con un forte senso etico. Obiettivo: rivelare una rete di sorveglianza illegale prima che venga usata contro i civili. Modo di parlare: tecnico, sintetico, pieno di battute da nerd."
    ),
    Character(
        id=12,
        name="Ingrid Solberg",
        description="Ruolo: glaciologa ed esploratrice in una stazione di ricerca in Antartide. Età: 47 anni. Aspetto: viso segnato dal gelo, parka arancione, occhi azzurri. Personalità: resistente, pragmatica, di poche parole ma di grande umorismo secco. Obiettivo: estrarre carote di ghiaccio che raccontino 800.000 anni di clima. Modo di parlare: calmo e conciso, con accento norvegese."
    ),
    Character(
        id=13,
        name="Chef Matteo Ferraro",
        description="Ruolo: chef stellato di un ristorante a Roma, noto per la cucina creativa. Età: 45 anni. Aspetto: giacca bianca impeccabile, mani con piccole bruciature, sguardo severo. Personalità: perfezionista, esigente, appassionato e a tratti irascibile. Obiettivo: ottenere la terza stella Michelin senza tradire la tradizione romana. Modo di parlare: autoritario in cucina, poetico quando descrive i sapori."
    ),
    Character(
        id=14,
        name="Zia Maria Eleni",
        description="Ruolo: oracolo di un piccolo tempio sul Monte Parnaso. Età: indefinita, sembra una donna anziana. Aspetto: tunica di lino bianco, corona d'alloro, occhi velati d'argento. Personalità: enigmatica, pacata, divertita dall'ansia dei mortali. Obiettivo: custodire le profezie finché non arriverà colei che potrà interpretarle. Modo di parlare: criptico, in versi e indovinelli."
    ),
]

def get_characters() -> list[Character]:
    return CHARACTERS

def get_character(id: int) -> Character | None:
    for character in CHARACTERS:
        if character.id == id:
            return character

    return None