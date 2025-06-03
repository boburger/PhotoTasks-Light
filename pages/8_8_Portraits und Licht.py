import streamlit as st


def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

      
# Main app
def main():
    st.set_page_config(page_title="Portraits und Licht",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Portraits und Licht")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Menschen zählen zweifellos zu den interessantesten und gleichzeitig anspruchsvollsten Motiven in der Fotografie. Für diese abschließende Aufgabe werden Sie alle im Kurs erlernten Fähigkeiten nutzen, um eindrucksvolle Porträtaufnahmen zu erstellen. 
    Dabei gilt es, Aspekte wie Beleuchtung, Hintergrund, Schärfentiefe, Bildkomposition und Farbgestaltung bewusst einzusetzen. Sie haben zudem die Möglichkeit, jede Aufnahme dezent in Photoshop nachzubearbeiten.
    
    Da Ihnen diese Techniken inzwischen vertraut sein sollten, können Sie Ihre gesamte kreative Energie darauf konzentrieren, etwas wirklich Einzigartiges oder Besonderes an Ihrem Porträtmotiv einzufangen. Es geht darum, den Charakter und die Persönlichkeit der abgebildeten Person auf authentische Weise sichtbar werden zu lassen. Nutzen Sie Ihr fotografisches Know-how, um nicht einfach nur ein Abbild, sondern eine aussagekräftige Momentaufnahme zu schaffen, die den Betrachter in ihren Bann zieht.

    ## Anleitung
    Diese Woche gibt es sechs fotografische Anforderungen. Die Anforderungen 1 bis 5 müssen durch Aufnahmen von Menschen erfüllt werden (diesmal leider keine Porträts von Haustieren, Stofftieren etc.!). Anforderung 6 kann mit einem frei gewählten Motiv umgesetzt werden.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Klassisches Studio-Porträt im Innenbereich",
            "description": "Fotografieren Sie eine Person mit klassischer Porträtbeleuchtung (Hauptlicht, Aufhelllicht, optional Hintergrund- und Randlicht). Falls Sie kein professionelles Lichtequipment besitzen, nutzen Sie die Studioausrüstung während des regulären Kurses.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Natürliches Innenlicht-Porträt",
            "description": "Erstellen Sie ein Porträt im Innenraum ausschließlich mit nicht-elektrischen Lichtquellen (Kamin, Kerzen, Tageslicht). Positionieren Sie die Person beispielsweise nahe eines Fensters. Erläutern Sie, wie Sie Haupt- und Aufhelllicht gestaltet haben.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Porträt mit natürlichem Außenlicht",
            "description": "Fotografieren Sie eine Person draußen bei vorhandenem Umgebungslicht. Beschreiben Sie, was als Haupt- und Aufhelllicht dient. Diese Aufnahme kann auch als ungestelltes (Candid-)Porträt entstehen.",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Blitz- und Umgebungslicht-Kombination",
            "description": "Erstellen Sie ein Porträt mit einer Mischung aus Kamerablitz und Umgebungslicht. Erklären Sie die Lichtführung. Der Blitz muss nicht direkt auf das Motiv gerichtet sein - nutzen Sie Reflektoren zum Umlenken des Lichts.",
            "key": "task4_upload"
        },
        {
            "title": "Anforderung 5: Selbstporträt",
            "description": "Erstellen Sie ein Porträt, bei dem Sie sowohl Fotograf als auch Motiv sind. Verwenden Sie ein Stativ und Selbstauslöser. Spiegel sind erlaubt, wenn sie künstlerisch eingesetzt werden. Achten Sie besonders auf Lichtsetzung und Bildaufbau.",
            "key": "task5_upload"
        },
        {
            "title": "Anforderung 6: Nicht-fotorealistisches Bild",
            "description": "Erstellen Sie in Photoshop ein bewusst nicht-realistisches Bild aus einer oder mehreren Aufnahmen. Der Gestaltung sind keine Grenzen gesetzt, das Ergebnis muss aber deutlich vom Fotorealismus abweichen. Inspiration finden Sie etwa im Kubismus oder bei David Hockney. HDR-Aufnahmen erfüllen diese Anforderung nur mit künstlerischer Tonwertkorrektur.",
            "key": "task6_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])



if __name__ == "__main__":
    main()