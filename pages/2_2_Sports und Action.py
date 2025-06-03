import streamlit as st


def create_requirement_section(title: str, description: str, key: str):
    st.subheader(title)
    st.write(description)

        
# Main app
def main():
    st.set_page_config(page_title="Sports und Action",
                       page_icon="📷",
                       layout="wide"                       
    )
    

    st.markdown("# Sports und Action")
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
    for task in aufgaben:
        st.markdown("---")
        create_requirement_section(task["title"],task["description"],task["key"])




if __name__ == "__main__":
    main()