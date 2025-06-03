import streamlit as st

def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

        
# Main app
def main():
    st.set_page_config(page_title="Landschaft und Natur",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Landschaft und Natur")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Was eine gewöhnliche Landschaftsaufnahme von einer großartigen unterscheidet, ist oft die Komposition. Achten Sie bewusst auf Linien, die Bildaufteilung, suggestive Formen, Diagonalen, geschwungene Kurven, den Bildrhythmus und interessante Texturen. Auch das Licht spielt diese Woche eine entscheidende Rolle.

    Sie werden feststellen, dass das Licht in den frühen Morgen- und späten Abendstunden intensive Farben und zarte Schattierungen hervorbringt, während die Mittagssonne meist hart und direkt wirkt. Für besonders dramatische Aufnahmen lohnt es sich, die Sonne seitlich oder sogar als Gegenlicht einzusetzen. 
    Zwar ist die richtige Belichtung in diesen Situationen anspruchsvoller, aber die Ergebnisse entschädigen für den Aufwand.
    Nutzen Sie diese Aufgabe, um sich intensiv mit den Gestaltungsmöglichkeiten der Naturfotografie auseinanderzusetzen. Gehen Sie auf Entdeckungsreise und halten Sie Augenblicke fest, die Ihnen besonders beeindruckend erscheinen.
                
    ## Zusätzliche Hinweise

    Unter jedem Bild sollten Sie Ihre Kameraeinstellungen begründen und die gestalterischen Elemente der Aufnahme kommentieren.

    Bevor Sie beginnen, empfehlen wir Ihnen, die Landschaftsbeispiele im Ansel-Adams-Kapitel "Examples: The Making of 40 Photographs" in Ihrem Kursreader durchzuarbeiten. Adams' Herangehensweise an Komposition und Lichtführung wird Ihnen wertvolle Inspiration für diese Aufgabe bieten.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Die S-Kurve als Gestaltungselement",
            "description": "Mindestens eines Ihrer Fotos soll eine bewusst eingesetzte S-Kurve zeigen. Diese kann verschiedene Funktionen erfüllen: den Blick des Betrachters zum Hauptmotiv führen, räumliche Tiefe suggerieren (wie eine sich schlängelnde Straße) oder als ausgleichendes Bildelement dienen. Erläutern Sie in Ihrem Kommentar, welche gestalterische Rolle die S-Kurve in Ihrer Aufnahme spielt.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Natürliche Motive gekonnt verfeinern",
            "description": "Für mindestens eine Ihrer Landschaftsaufnahmen sollen Sie das Bild in Photoshop gezielt optimieren. Beginnen Sie mit einer lokalen Bearbeitung, etwa indem Sie mit einer fein angepassten Kurvenebene gezielt Dunst in bestimmten Bildbereichen reduzieren oder störende Elemente mit dem Reparaturpinsel entfernen. Ergänzend führen Sie eine globale Anpassung durch, beispielsweise eine ausgewogene Farbkorrektur oder einen sorgfältigen Beschnitt, der die Bildkomposition verbessert. Wichtig ist, dass Sie sowohl das Original als auch die bearbeitete Version einreichen. Die Veränderungen sollten zwar subtil ausfallen, aber dennoch eine erkennbare und sinnvolle Verbesserung darstellen. In Ihrem Kommentar erläutern Sie konkret, welche Optimierungen Sie vorgenommen haben und wie diese zur Wirkung des Fotos beitragen.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Texturen in der Natur",
            "description": "Fotografieren Sie ein Motiv, dessen Hauptaugenmerk auf einer natürlichen Textur liegt (z.B. Felsstrukturen, Sandmuster, Wolkenformationen). Verwenden Sie eine kleine Blende (große Blendenzahl), um maximale Schärfentiefe zu erreichen. Setzen Sie in Photoshop den vollen Tonumfang von tiefem Schwarz bis hellem Weiß ein, um die Textur optimal zur Geltung zu bringen. Streiflicht betont Texturen besonders gut.",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Die magische Stunde",
            "description": "Mindestens eine Aufnahme muss während der goldenen Stunde entstehen - entweder in der Stunde nach Sonnenaufgang oder vor Sonnenuntergang. Das charakteristische, tiefstehende Licht betont Konturen und verleiht der Landschaft eine warme Farbstimmung. Morgens herrscht meist klarere Luft, aber auch Abendaufnahmen sind akzeptabel. Planen Sie Ihre Aufnahmen entsprechend (ca. 6-7 Uhr morgens oder 19-20 Uhr abends).",
            "key": "task4_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])


if __name__ == "__main__":
    main()