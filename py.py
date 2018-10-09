#Must have Service account keys must have in a key.json in the same folder 
#export GOOGLE_APPLICATION_CREDENTIALS="key.json"
GOOGLE_APPLICATION_CREDENTIALS = "key.json"
from google.cloud import vision
from google.cloud import translate

client = vision.ImageAnnotatorClient()
translate_client = translate.Client()
image = vision.types.Image()

list = [u'Jesper%Holmgren%Sveegaard','060984-2385', 'Jesper', 'Holmgren', 'Sveegaard', 'Jesper%Holmgren%Sveegaard',
        'duelighedsprøve', 'i', 'betjening', 'af', 'redningsbåde','flåder', 'og', 'mand-over-bord', 'både',
        'Bevis', 'som', 'sygdomsbehandler', 'Generelt', 'certifikat', 'som', 'radiooperatør', 'GMDSS', '(GOC)'
        'Equipment', 'specific', 'ECDIS', 'training', 'Course', 'Certificate', 'AIS', 'BEVIS', 'FOR', 'UDDANNELSE', 'ARBEJDSMILJØ',
        '16', 'CURSUS', 'Safety', 'and', 'Health', 'Course', 'Bevis', 'Officer', 'for', 'Maritim', 'Sikring', 'Styrmand', '2.', 'grad' ]
                 

corpusa = []
corpusa2 = []


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """ 
    corpus = []
    part_corpus = []
    
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        
        print('\n"{}"'.format(text.description))# print the hole detected text
        
        if text.description in list:
            corpus.append("{}".format(text.description))#make list of the words that match the list
            for i in corpus:
                if i not in corpusa:# take out words that are the same in the list of matched words
                    corpusa.append(i)
        
            print('--------------------------------------------------------------------------FULL_MATCH/')
        
        elif any(text.description in part for part in list):
            part_corpus.append("{}".format(text.description))#make list of the words that match the list
            for i in part_corpus:
                if i not in corpusa2:# take out words that are the same in the list of matched words
                    corpusa2.append(i)
        
            print('---------------------------------PART MATCH/')
        
                    
        else:
            print('NO MATCH')
            
    print (' ')
    print ('FULL MATCH')        
    print (corpusa) 
    print ('PART MATCH')
    print (corpusa2)
            


'''
some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
for text in some_list:
    if any("abc" in text for text in some_list):
        print (text)
'''  

          
def translate_text(corpusa):
    text = []
    # The text to translate
    corpusat = ' '.join(corpusa)
    text.append(corpusat)
    # The target language
    target = 'en'
    # Translates some text into English
    translation = translate_client.translate(text)
    print(' ')
    print(u'Text: {}'.format(text))
    print(' ')
    print('TRANSLATION TO ENGLISH')
    print(translation)
            
#Input file here
detect_text_uri('gs://ocr_image87/test3.png')
print ('\n', 'DETECTED WORDS')
translate_text(corpusa)




#pid rid for nemid
#track IP address of user if hiden restricts applicaton

#item = someSortOfSelection()
#if item in myList:
#    doMySpecialFunction(item)
''' nemid can we get user name and cpr from it and put it in the database?
(if loged in one it can log in with name and cpr second time option)

finds the name of the user and the cpr and uses the
name as login and the cpr as password if both are in the database 
and match the nemid name and cpr then we have a match

another problem is the name of the certificates for each certifivate 
there must be a function in which all parts of the words must match'''
#-------------------------------------------------------------------------------
'''def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name)) '''




