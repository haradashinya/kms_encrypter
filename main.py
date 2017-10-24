import boto3

boto3.set_stream_logger(name='botocore')
kms = boto3.client('kms')
AWS_KMS_ID = 'TEST'


def encrypt(text):
    return kms.encrypt(
        KeyId=AWS_KMS_ID,
        Plaintext=text
    )['CiphertextBlob']


def decrypt(encrypted_text):
    return kms.decrypt(
        CiphertextBlob=encrypted_text
    )['Plaintext']


def main():
    if AWS_KMS_ID == 'TEST':
        raise ValueError('Invalid AWS_KMS_ID')
    text = input("""Type text to encrypt \n> """)
    encrypted = encrypt(text)
    decrypted = decrypt(encrypted)
    print(f"""
=== ENCRYPTED TEXT ===
{encrypted}
=== DECRYPTED TEXT === 
{decrypted}
""")


if __name__ == '__main__':
    main()
