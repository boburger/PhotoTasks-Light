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
    st.set_page_config(page_title="Architecture und Interiors",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Architecture und Interiors")
    st.sidebar.header("Architecture und Interiors")
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