import speech_recognition as sr


# Use SpeechRecognition to record

def my_record(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("./test.wav", "wb") as f:
        f.write(audio.get_wav_data())
    print("录音完成！")