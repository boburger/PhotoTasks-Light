import streamlit as st

def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

        
# Main app
def main():
    st.set_page_config(page_title="Bad Photos",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Bad Photos")
    
    # Introduction
    st.markdown("""
    ## Motivation
    
    Kameras im Automatikmodus kümmern sich um technische Einstellungen wie Belichtung und Schärfe – oft aber ohne Rücksicht auf die kreative Absicht der Fotografierenden. 
    In dieser ersten Aufgabe sollst du bewusst mit den Kameraeinstellungen experimentieren und Bilder erzeugen, die im Automatikmodus kaum möglich wären.
    
    ## Hinweis
    
    Die Fotos sollen zwar technisch „fehlerhaft" sein, aber dennoch bewusst gestaltet, visuell interessant und künstlerisch ansprechend wirken.
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Falsche Belichtung",
            "description": "Mindestens ein Foto muss falsch belichtet sein. Das bedeutet, dass der Großteil des Bildes entweder nahezu schwarz (unterbelichtet) oder nahezu flächig weiß durch Überbelichtung sein sollte.",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Bewegungsunschärfe",
            "description": "Das Hauptmotiv von mindestens einem Foto soll durch Bewegungsunschärfe verwischt sein – entweder durch Bewegung des Motivs oder der Kamera.",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Keine Schärfe",
            "description": "Auf mindestens einem Foto sollte überhaupt nichts scharfgestellt sein. Es ist nicht einfach, ein ansprechendes Bild ohne jegliche Schärfe aufzunehmen – sei kreativ!",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Falscher Weißabgleich",
            "description": "In mindestens einem Foto soll absichtlich der falsche Weißabgleich verwendet werden, um einen bestimmten Effekt zu erzielen. Der Weißabgleich der Kamera legt fest, welche Lichtfarbe sie erwartet – z. B. Tageslicht (bläulich) oder Glühlampenlicht (rötlich). Die meisten Kameras haben eine Einstellung für \"automatischen Weißabgleich (AWB)\" sowie manuelle Optionen für verschiedene Lichtquellen.",
            "key": "task4_upload"
        },
        {
            "title": "Anforderung 5: Schlechte Komposition",
            "description": "Mindestens ein Foto soll bewusst schlecht komponiert sein. **Hinweis:** Wenn du unsicher bist, könntest du z. B. ein exakt mittig platziertes Motiv wählen, das ein ungewöhnlich symmetrisches Bild ergibt, eine Verwechslung von Motiv und Hintergrund erzeugen oder einen schiefen Horizont einbauen.",
            "key": "task5_upload"
        }
    ]


    # Process each requirement
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])




if __name__ == "__main__":
    main()