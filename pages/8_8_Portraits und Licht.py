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
    st.set_page_config(page_title="Portraits und Licht",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Portraits und Licht")
    st.sidebar.header("Portraits und Licht")
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
        st.success(f"Du hast {len(uploaded_files)} von 5 Anforderungen erfüllt!")
        
        if len(uploaded_files) == 5:
            st.balloons()
            st.markdown("### 🎉 Herzlichen Glückwunsch!")
            st.markdown("Du hast alle Anforderungen erfüllt und die Aufgabe erfolgreich abgeschlossen!")

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


if __name__ == "__main__":
    main()