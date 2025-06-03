import streamlit as st


def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

      
# Main app
def main():
    st.set_page_config(page_title="Nacht und Farbe",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Nacht und Farbe")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Nachtfotografie stellt besondere Herausforderungen dar. Die Belichtungszeiten müssen sehr lang sein, daher ist Freihandaufnahmen nicht möglich. Doch mit einer stabilen Unterlage für die Kamera (die kein Stativ sein muss) und einer Langzeitbelichtung kann die Lichtsammelfähigkeit Ihrer Kamera das menschliche Auge weit übertreffen. 
    Dadurch können Sie Motive einfangen, die normalerweise unsichtbar wären - wie ein nächtlicher Wald, eine ferne Galaxie oder sogar ein Regenbogen im Mondlicht.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Naturnachtaufnahme im Freien",
            "description": "Gehen Sie nach draußen, suchen Sie einen stabilen Platz für Ihre Kamera und fotografieren Sie eine malerische Naturszene bei Nacht. Die Aufnahme darf keinerlei Verwacklungen aufweisen. Nutzen Sie gegebenenfalls den Selbstauslöser Ihrer Kamera, um Erschütterungen beim Auslösen zu vermeiden. Die Belichtungszeit sollte mindestens ein bis zwei Sekunden betragen. Das Motiv sollte die Natur sein (keine künstlichen Objekte), wobei minimales menschengemachtes Beiwerk akzeptabel ist. Mögliche Motive sind mondbeschienene Landschaften oder natürlich wirkende Szenerien mit indirekter künstlicher Beleuchtung.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Architekturaufnahme bei Nacht",
            "description": "Erstellen Sie eine mindestens ein bis zwei Sekunden belichtete Nachtaufnahme ohne Verwacklungen, diesmal mit architektonischem Motiv wie Brücken, Straßenzügen oder Gebäuden. Achten Sie auf eine ausgewogene Belichtung, die sowohl Lichtquellen als auch Details der Bauwerke zeigt – die Aufnahme sollte nicht so dunkel sein, dass nur Lichter erkennbar sind.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Lichtmalerei",
            "description": "Erstellen Sie eine Langzeitbelichtung, bei der Sie eine Lichtquelle wie einen Malerpinsel bewegen. Entweder zeichnen Sie mit der bewegten Lichtquelle Muster in die Szene oder beleuchten gezielt bestimmte Bereiche während der Belichtung. Nutzen Sie kreative Lichtquellen wie Taschenlampen, LED-Leuchten oder Blitzgeräte. Beispielsweise können Sie während der Belichtung mit einem Handblitz durch das Bild gehen und Objekte gezielt ausleuchten.",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Licht und Farbe",
            "description": "Demonstrieren Sie den Farbstich-Effekt: Fotografieren Sie ein farbiges Objekt einmal unter normalem Licht und einmal unter stark farbigem Licht (z.B. LED), sodass die Farbwiedergabe dramatisch unterschiedlich ausfällt. Fügen Sie jeweils ein weißes Referenzobjekt ins Bild. Deaktivieren Sie den automatischen Weißabgleich. Im Kommentar beschreiben Sie Objekt und Lichtquelle. Der Effekt ist besonders stark bei Lichtquellen mit schmalem Spektrum (z.B. Natriumdampflampen).",
            "key": "task4_upload"
        },
        {
            "title": "Anforderung 5: Farbakzent in monochromer Szene",
            "description": "Erstellen Sie ein überwiegend monochromes (graustufiges oder einfarbig entsättigtes) Foto mit einem oder mehreren farbigen Akzenten (z.B. schwarz-weißes Bild mit roten Äpfeln). Der Effekt kann durch geschickte Aufnahme oder nachträgliche Bearbeitung in Photoshop erreicht werden, indem Sie alle nicht-akzentfarbigen Bereiche entsättigen. Erläutern Sie im Kommentar Ihre Vorgehensweise. Kreative Lösungen ohne Photoshop sind ebenfalls zulässig.",
            "key": "task5_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])


if __name__ == "__main__":
    main()