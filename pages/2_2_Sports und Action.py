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
    st.set_page_config(page_title="Sports und Action",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Bad Photos")
    st.sidebar.header("Bad Photos")
    # Introduction
    st.markdown("""
    ## Motivation
    
    Als Fotograf wirst du schnell merken: Die Welt wartet nicht auf dein Foto. Viele Motive sind flüchtig, sodass oft nur wenige gute Aufnahmen aus vielen Versuchen gelingen.
    Diese Woche geht es um Bewegung. Haustiere bieten spannende Motive, zum Beispiel beim Rennen, Springen oder Spielen.
    Die größte Schwierigkeit beim Fotografieren bewegter Objekte besteht darin, genügend Licht einzufangen. Die Belichtungszeit muss kurz genug sein, um Bewegungsunschärfe zu vermeiden. Das wird in der Regel durch eine große Blendenöffnung und eine höhere ISO-Einstellung ausgeglichen. Dabei stößt man jedoch schnell auf verschiedene Kompromisse. Zum Beispiel verkürzt eine größere Blendenöffnung die Schärfentiefe, wodurch präzises Fokussieren wichtiger – und schwieriger – wird. 
    Autofokus benötigt Zeit, und ein langsames Autofokussystem kann mit der Bewegung eventuell nicht Schritt halten, was zu einem verpassten Schnappschuss führt. 
    
    ## Hinweis
    
    Wenn du die Aufnahme im Voraus planen kannst, ist ein guter Trick, vorab auf die erwartete Entfernung scharfzustellen, sodass das Foto im entscheidenden Moment ausgelöst werden kann, wenn das Objekt den Schärfepunkt durchquert. Wie du siehst, erfordert das Festhalten eines einzigartigen Moments oft die gleichzeitige Steuerung mehrerer Kamerafunktionen!
    """)

    # aufgaben data
    aufgaben = [
        {
            "title": "Anforderung 1: Aktion einfrieren",
            "description": "Mache ein Foto mit sehr kurzer Belichtungszeit, um dein Motiv in einem Bruchteil einer Sekunde festzuhalten. Dafür brauchst du viel Licht – am besten versuchst du es draußen bei Tageslicht. ",
            "key": "task1_upload"
        },
        {
            "title": "Anforderung 2: Bewegung durch verwischtes Motiv zeigen",
            "description": "Mache mindestens ein Foto, bei dem Bewegungsunschärfe gezielt eingesetzt wird, um die Dynamik deines Motivs zu zeigen. Das Hauptmotiv sollte verwischt sein, der Hintergrund hingegen scharf",
            "key": "task2_upload"
        },
        {
            "title": "Anforderung 3: Bewegung durch verwischten Hintergrund zeigen",
            "description": "Mache mindestens ein Foto, bei dem das Motiv scharf ist und der Hintergrund durch Mitziehen der Kamera verwischt wurde. Notiere in deinen Kommentaren, wie sich diese Wirkung von Anforderung 2 unterscheidet. (Ein häufiger Trick: Verfolge ein bewegtes Objekt mit der Kamera, sodass es im Sucher zentriert bleibt – das erfordert Übung, lohnt sich aber.)",
            "key": "task3_upload"
        },
        {
            "title": "Anforderung 4: Bewegung mit einer Bildserie zeigen",
            "description": "Mache eine Bildserie (mindestens 3 Fotos in schneller Folge), um eine Bewegung schrittweise festzuhalten und so eine kleine Geschichte zu erzählen. Viele Kameras bieten dafür einen Serienbildmodus. Kombiniere die Fotos anschließend zu einem einzigen Bild – zum Beispiel nebeneinander, überlagert oder auf kreative Weise. Wie du sie zusammenstellst, bleibt dir überlassen!",
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