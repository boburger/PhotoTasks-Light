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
    st.set_page_config(page_title="Nacht und Farbe",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Nacht und Farbe")
    st.sidebar.header("BNacht und Farbe")
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