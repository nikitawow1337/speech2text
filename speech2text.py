import speech_recognition as sr

import pydub
from pydub import AudioSegment


def convert_to_wav(sound, secs, msecs, num):
    # path to ffmpeg lib
    pydub.AudioSegment.ffmpeg = "C:/ffmpeg-4.0.2-win64-static"

    fragment = sound[secs * (num - 1):msecs]
    print(fragment.duration_seconds)
    savefile = "files/" + str(num) + ".wav"
    fragment.export(savefile, format="wav")
    return savefile
    # sound.export("files/sobstv.wav", format="wav")
    # print(sound.duration_seconds)


def recognize(audio, r, f):
    with sr.AudioFile(audio) as source:
        # print('Say Something')
        audio = r.record(source)
        print('Done recording!')

    try:
        text = r.recognize_google(audio, language="ru")
        f.write(text)
        print("Successfully recognized")

    except Exception as e:
        print(e)

    f.write("\n")


recognizer = sr.Recognizer()
file = open("files/myfile.txt", "a", encoding="cp1251")

minutes = 40

soundw = AudioSegment.from_mp3("C:/mysound.mp3")
print("Loaded")

for x in range(1, minutes):

    # pydub does things in milliseconds, divide by 10 seconds
    seconds = 10 * 1000
    # seconds = x

    audio_file = convert_to_wav(soundw, seconds, seconds * x, x)
    recognize(audio_file, recognizer, file)

    print(x, "done")

file.close()
