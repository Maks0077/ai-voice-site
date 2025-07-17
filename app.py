import streamlit as st
import time
from io import BytesIO

def fake_tts(text):
    dummy_audio = BytesIO()
    dummy_audio.write(b'RIFF....WAVEfmt ')  # Заглушка
    dummy_audio.seek(0)
    return dummy_audio

st.title("🎙️ AI Voice Озвучка")
st.markdown("Введи текст — і почуй свій AI голос.")

user_text = st.text_area("Введи текст", placeholder="Наприклад: Привіт, я Шарік, і я озвучений ШІ")

if st.button("🔊 Озвучити"):
    if not user_text.strip():
        st.warning("Спочатку введи текст!")
    else:
        with st.spinner("Генеруємо..."):
            time.sleep(2)
            audio = fake_tts(user_text)
        st.success("Готово!")
        st.audio(audio, format="audio/wav")
        st.download_button("⬇️ Завантажити .wav", audio, file_name="voice.wav")
