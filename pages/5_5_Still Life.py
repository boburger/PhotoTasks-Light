import streamlit as st


def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

        
# Main app
def main():
    st.set_page_config(page_title="Still Life",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Still Life")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Bisher bestanden die meisten deiner Fotos aus einer Art „gefundener Kunst“ – das Bild hält etwas fest, das bereits schön in der Welt existiert. Das heißt nicht, dass dabei keine Kreativität im Spiel war. Deine Interpretation der Szene, ausgedrückt durch Komposition und bewusste Kameraeinstellungen, macht das festgehaltene Motiv erst zur „Kunst“.

    Diese Woche erweiterst du deine kreative Kontrolle – über die Kamera hinaus auf die Szene selbst. In der Stillleben-Fotografie arrangierst du das Motiv, wählst den Hintergrund und gestaltest das Licht nach deinen Vorstellungen. Nimm dir Zeit, jedes Bild genau so einzurichten, wie du es möchtest. Der Vorteil: Du hast unendlich viele Versuche, bis alles perfekt ist.
                
    ## Anleitung

    Der entscheidende Unterschied zu früheren Wochen liegt in der Gestaltung der Szene: Fotografiere ausschließlich Objekte, die du selbst arrangiert und beleuchtet hast. In deinen Bildkommentaren solltest du nicht nur die Kameraeinstellungen (Fokus, Verschlusszeit, Blende etc.) begründen, sondern auch deine Wahl des Hintergrunds, die Anordnung der Objekte und die Beleuchtung.

    Bevor du beginnst, lies dir den Abschnitt „The Case of the Disappearing Glass“ im Kursmaterial durch. Er erklärt, wie Licht mit Glasobjekten interagiert – von Spiegelungen bis Transparenz – und wie du damit dramatische Effekte erzielen kannst.
                
    ## Allgemeine Anforderungen

    Diese beiden Punkte gelten für jedes Foto dieser Woche:
    Allgemeine Anforderung A: Hintergrund

    Wähle für jedes Foto bewusst einen Hintergrund und begründe deine Wahl im Kommentar.

    Experimentiere mit hellen, dunklen oder strukturierten Hintergründen.

    Nutze Materialien wie Stoffe, Bettlaken, Pappe oder Tischdecken, um ansprechende Hintergründe zu gestalten.

    Pflicht: Verwende mindestens zwei unterschiedliche Hintergründe in deiner Serie.

    Allgemeine Anforderung B: Beleuchtung

    Arrangiere die Beleuchtung gezielt und erläutere deine Entscheidung im Kommentar.

    Nutze Schreibtischlampen, Fensterlicht oder andere Lichtquellen, um Richtung und Farbe des Lichts zu steuern.

    Probiere Frontlicht, Seitenlicht oder Gegenlicht aus, um unterschiedliche Stimmungen zu erzeugen.

    Pflicht: Verwende mindestens zwei verschiedene Lichtsituationen in deiner Serie.

    ## Zusätzliche Hinweise

    Stillleben-Fotografie lebt von Geduld und Präzision – nimm dir Zeit für das Arrangement und probiere verschiedene Varianten aus.

    Achte auf Schattenwurf und Reflexionen, besonders bei gläsernen oder glänzenden Objekten.

    Falls du mit künstlichem Licht arbeitest: Positioniere die Quelle seitlich oder schräg, um Tiefe und Textur zu betonen.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Kaustiken",
            "description": "In mindestens einem deiner Fotos soll eine Kaustik zu sehen sein – jenes faszinierende Lichtmuster, das entsteht, wenn Licht durch gekrümmte Glasobjekte wie Weingläser oder Vasen bricht und sich auf Oberflächen abzeichnet. Besonders reizvoll wirken diese Lichtspiele, wenn du das Glas seitlich beleuchtest. Experimentiere mit verschiedenen Lichtquellen und deren Positionierung, um besonders intensive oder filigrane Kaustik-Effekte zu erzeugen.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Thematische Objektsammlung",
            "description": "Wähle eines der vier Themen – Vergänglichkeit, Eitelkeit, Ehrgeiz oder Erneuerung – und inszeniere eine passende Arrangement von Gegenständen. Achte darauf, dass die Auswahl der Objekte und ihre Anordnung das gewählte Thema unmittelbar vermitteln, ohne dass es einer Erklärung bedarf. Die Beleuchtung und etwaige Spiegelungen zwischen den Objekten können dabei helfen, die gewünschte Atmosphäre zu verstärken.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Porträt eines Objekts",
            "description": "Widme dich einem einzelnen Gegenstand, der für dich eine persönliche Bedeutung hat. Überlege, welche Gefühle oder Erinnerungen du mit diesem Objekt verbindest, und versuche, diese Stimmung durch die Bildgestaltung einzufangen. Die Wahl des Blickwinkels, die Schärfeverteilung, die Lichtführung und eventuelle Nachbearbeitungsschritte sollten alle darauf ausgerichtet sein, die emotionale Aussage des Fotos zu unterstützen.",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Schweben lassen",
            "description": "Für diese kreative Aufgabe sollst du die Illusion schwebender Objekte erschaffen. Fixiere dazu deine Kamera auf einem Stativ und fotografiere zunächst den reinen Hintergrund. Anschließend nimmst du das Bild mit dem scheinbar schwebenden Objekt auf, das du mit Hilfsmitteln wie Fäden oder Stützen in Position hältst. In Photoshop setzt du dann beide Aufnahmen zusammen und entfernst alle Spuren der Hilfskonstruktion.",
            "key": "task4_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])


if __name__ == "__main__":
    main()