from cutting import cutter
from speech_rec import transcribe_gs
import os
import sys
import argparse
reload(sys)

sys.setdefaultencoding('utf-8')

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

recordingfiles = current_dir + '/recordingfiles'

def main(speech_file,text_file):

        print("Extracting text from the speech file...")

        name = os.path.splitext("speech_file")[0]
        vc_dirname = current_dir + '/voicechunks/' + name #This is the folder where the small speech files will be stored

        if not os.path.exists(vc_dirname):
            os.makedirs(vc_dirname)
        cutter(0,speech_file,vc_dirname)# This cuts the speech file into smaller parts
        #This creates the output text files folder if not existing
        if not os.path.exists('text_files'):
            os.makedirs('text_files')

        output_text = " "

        for i,chunk_file in enumerate(os.listdir(vc_dirname)):
            if(i == 0):
                continue
            complete_chunk_file = vc_dirname+ "/" + chunk_file

            output_text = output_text+ " " + transcribe_gs(complete_chunk_file,text_file)

        print("Done! Here is the extracted text :")
        print(output_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('speech_file' , help = 'Path of speech file')
    parser.add_argument('text_file', help = 'Path of recognized text')

    args = parser.parse_args()

    sf = args.speech_file
    tf = args.text_file
    main(sf,tf)
