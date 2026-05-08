import argparse
from Modules import metadata_extractor, encryptor, obfuscator, sanitizer, steganography

def main():
    parser = argparse.ArgumentParser(description='MetaCrypt - Metadata Protection Tool')
    parser.add_argument('--mode', type=str, required=True, choices=['extract', 'encrypt', 'decrypt', 'obfuscate', 'sanitize', 'steg-hide', 'steg-reveal'])
    parser.add_argument('--file', type=str, required=True, help='Path to the target file')
    parser.add_argument('--key', type=str, help='Encryption key (for encrypt/decrypt)')
    args = parser.parse_args()

    if args.mode == 'extract':
        metadata_extractor.extract_metadata(args.file)
    elif args.mode == 'encrypt':
        encryptor.encrypt_metadata(args.file, args.key)
    elif args.mode == 'decrypt':
        encryptor.decrypt_metadata(args.file, args.key)
    elif args.mode == 'obfuscate':
        obfuscator.obfuscate_metadata(args.file)
    elif args.mode == 'sanitize':
        sanitizer.sanitize_metadata(args.file)
    elif args.mode == 'steg-hide':
        steganography.hide_metadata(args.file, args.key)
    elif args.mode == 'steg-reveal':
        steganography.reveal_metadata(args.file, args.key)

if __name__ == '__main__':
    main()
