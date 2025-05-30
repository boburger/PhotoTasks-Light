import streamlit as st
import time
from PIL import Image

def display_image_analysis(uploaded_file) -> bool:
    if uploaded_file is None:
        st.info("⚠️ Noch kein Bild hochgeladen.")
        return False
    
    # Bild anzeigen
    try:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📷 Hochgeladenes Bild")
            st.image(image, use_container_width=True)
        
        with col2:
            st.subheader("📊 Bildinfo")
            
            # Grundlegende Bildinformationen
            st.write(f"**Dateiname:** {uploaded_file.name}")
            st.write(f"**Dateigröße:** {uploaded_file.size / 1024:.1f} KB")
            st.write(f"**Bildformat:** {image.format}")
            st.write(f"**Abmessungen:** {image.size[0]} x {image.size[1]} Pixel")
                
        st.success("✅ **Analyse abgeschlossen!** Die Bildanalyse wurde erfolgreich durchgeführt.")
        return True
    except Exception as e:
        st.error(f"Fehler beim Laden des Bildes: {str(e)}")
        return False

def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)
    return st.file_uploader(
            "Wähle ein Bild für die Analyse:",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
            key=key
    )

# Update progress sidebar
def update_progress_sidebar(count: int):
    progress_map = {0: 0, 1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
    target = progress_map.get(count, 0)
    
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    
    for i in range(1, target + 1):
        status_text.text(f"{i}% - {count} Bild(er) hochgeladen")
        progress_bar.progress(i)
        time.sleep(0.01)
    
    if target == 100:
        status_text.text("100% - Aufgabe abgeschlossen!")

        
# Main app
def main():
    st.set_page_config(page_title="Landschaft und Natur",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Landschaft und Natur")
    st.sidebar.header("Landschaft und Natur")
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
    uploaded_files = []
    for task in aufgaben:
        st.markdown("---")
        uploaded_file = create_requirement_section(task["title"],task["description"],task["key"])
        if display_image_analysis(uploaded_file):
            uploaded_files.append(uploaded_file)

    # Update progress sidebar
    update_progress_sidebar(len(uploaded_files))

    # Summary section
    if len(uploaded_files) > 0:
        st.markdown("---")
        st.markdown("## 📊 Zusammenfassung")
        st.success(f"Du hast {len(uploaded_files)} von 4 Anforderungen erfüllt!")
        
        if len(uploaded_files) == 4:
            st.balloons()
            st.markdown("### 🎉 Herzlichen Glückwunsch!")
            st.markdown("Du hast alle Anforderungen erfüllt und die Aufgabe erfolgreich abgeschlossen!")

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


if __name__ == "__main__":
    main()