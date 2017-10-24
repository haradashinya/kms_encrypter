#kms_encrypter

Encrypt using AWS KMS

## Install

    $ cd kms_encrypter
    $ python3.6 -m venv venv
    $ pip install -r requirements.txt

## Getting Started


Register AWS KMS Key From AWS Console refer to <a href="http://docs.aws.amazon.com/kms/latest/developerguide/overview.html" target="_blank">this site</a>.

Next, replace AWS_KMS_ID Value with created value at main.py.

    AWS_KMS_ID = 'xxx'

That's all. You can get encrypted text by run command and enter question.

    $ cd kms_encrypter
    $ source venv/bin/activate
    $ python main.py
    
    Type text to encrypt 
    > abc
    
    === ENCRYPTED TEXT ===
    b'xxxxxxxxxxENCRYPTED_TEXTxxxxxxxxxx'
    === DECRYPTED TEXT === 
    b'abc'











