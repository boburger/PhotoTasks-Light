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
    st.set_page_config(page_title="Bad Photos",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Bad Photos")
    st.sidebar.header("Bad Photos")
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