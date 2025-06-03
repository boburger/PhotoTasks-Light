import streamlit as st


def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

        
# Main app
def main():
    st.set_page_config(page_title="Architecture und Interiors",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Architecture und Interiors")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Gute Fotografie zeigt uns oft das Vertraute auf ungewohnte Weise. 
    Diese Woche werdet ihr die Räume betrachten, in denen Menschen leben und arbeiten, und versuchen, sie in einem Bild festzuhalten.

    Architektur ist in der Regel geometrischer als natürliche Szenen. Achtet auf sich wiederholende Elemente, Größenverhältnisse, die sich durch die Perspektive verändern, die Linien, die durch Fluchtpunkte entstehen, sowie auf die Textur und Patina von menschengemachten Objekten. 
    Eine Möglichkeit, Menschen mit Architektur- und Innenraumfotografie zu überraschen, besteht darin, durch clevere Komposition die geometrischen Aspekte von Strukturen hervorzuheben, die oft unterbewusst wahrgenommen oder sogar übersehen werden. Die Anforderungen dieser Woche werden euch helfen, mit Geometrie zu spielen und über die praktischen Überlegungen derer nachzudenken, die einen Innenraum fotografisch darstellen müssen.

    Inzwischen solltet ihr die Kontrolle über eure Kamera gut beherrschen, also verwendet diese Woche eure zusätzliche Energie darauf, eure Fotos visuell ansprechend zu gestalten. Geht über das bloße Erfüllen der Vorgaben hinaus und probiert einige der Gestaltungsregeln aus.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Fluchtpunkt für vertikale Linien",
            "description": "In mindestens einem deiner Fotos müssen vertikale Linien in der Umgebung (z. B. Gebäudekanten) sichtbar in einem Fluchtpunkt zusammenlaufen – entweder innerhalb oder knapp außerhalb des Bildausschnitts. Nutze dafür eine Weitwinkelperspektive (kurze Brennweite) und richte die Kamera nach oben.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Kein vertikaler Fluchtpunkt",
            "description": "In mindestens einem Foto müssen vertikale Linien parallel erscheinen. Dafür kannst du die Kamera geradeaus ausrichten und später den Ausschnitt zuschneiden. Alternativ kannst du in Photoshop das Perspektiv-Werkzeug (Bearbeiten > Transformieren > Perspektivisch) oder die Objektivkorrektur (Filter > Verzerrungsfilter) nutzen, um die Linien anzupassen.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Rahmen im Bild",
            "description": "Mindestens ein Foto soll durch einen Türrahmen, ein Fenster, einen Bogendurchgang oder einen anderen physischen, menschengemachten Rahmen aufgenommen werden. Der Rahmen muss sichtbar sein, steht aber nicht zwingend im Mittelpunkt. Er kann auch nicht-rechteckig sein.",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Sich wiederholende Muster",
            "description": "Finde ein interessantes, sich wiederholendes Muster in einem Gebäude oder einem anderen architektonischen Objekt und mache es zum zentralen Thema eines Fotos. Sei kreativ – das Muster sollte so offensichtlich sein, dass der Betrachter es auch ohne Erklärung erkennt. Hinweis: Fenster oder Hauptquad-Bögen sind für diese Aufgabe nicht erlaubt!",
            "key": "task4_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])



if __name__ == "__main__":
    main()