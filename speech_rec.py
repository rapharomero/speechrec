import speech_recognition as sr
import argparse
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def transcribe_gs(speech_file,file_name):
    r = sr.Recognizer()
    with sr.AudioFile(speech_file) as source:
        audio = r.record(source)
    with open('text_files/'+ file_name,'a+') as outfile:
        try:
            transc = r.recognize_google(audio,language="fr-FR").decode('utf-8')
        except sr.UnknownValueError:
            transc = ""
            pass
        outfile.write(' ')
        outfile.write(transc)
        outfile.close()
    return transc

##The code below can be used to try the recongnition on a small speech file.
##Usage in terminal:
##python speech_rec.py <path of speech_file><path of output text file>
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('speech_file', help = 'Full path of audio file to be recognized')
    parser.add_argument('file_name', help = 'Name of output text file')
    args = parser.parse_args()
    sf = args.speech_file
    fname = args.file_name
    transcribe_gs(sf,fname)
