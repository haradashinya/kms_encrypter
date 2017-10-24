# kms_encrypter

Encrypt using AWS KMS

## Install

    $ cd kms_encrypter
    $ python3.6 -m venv venv
    $ pip install -r requirements.txt

## Getting Started


Create AWS KMS Key at <a href="https://aws.amazon.com/jp/iam/" target="_blank">this</a>.

Next, replace AWS_KMS_ID Value with created it at main.py.

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











