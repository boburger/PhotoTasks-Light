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
    st.set_page_config(page_title="Still Life",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Still Life")
    st.sidebar.header("Still Life")
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