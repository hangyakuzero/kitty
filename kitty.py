import argparse
import base64
import urllib.parse

def encrypt_data(data, encoding_type):
    if encoding_type == "base64":
        result = base64.b64encode(data.encode()).decode()
    elif encoding_type == "url":
        result = urllib.parse.quote(data)
    elif encoding_type == "hex":
        result = data.encode().hex()
    elif encoding_type == "octal":
        result = ''.join(f"\t{oct(ord(char))[2:]}" for char in data)
    elif encoding_type=="alt":
        result= ''.join(char.upper() if data.index(char)%2 == 0 else char.lower() for char in data)
     
    else:
        raise ValueError("Invalid encoding type. Supported types: base64, url, hex, octal,alternating")

    return result

def main():
    parser = argparse.ArgumentParser(description="Kitty Encryptor")
    parser.add_argument("action", choices=["encrypt"], help="Specify 'encrypt'")
    parser.add_argument("encoding_type", choices=["all", "base64", "url", "hex", "octal","alt"], help="Specify encoding type")
    parser.add_argument('text', help="Text to encrypt")

    args = parser.parse_args()

    if args.action == "encrypt":
        if args.encoding_type == "all":
            for encoding_type in ["base64", "url", "hex", "octal","alt"]:
                encrypted_data = encrypt_data(args.text, encoding_type)
                print(f"{encoding_type.capitalize()} Encoded Text: {encrypted_data}")
        else:
            encrypted_data = encrypt_data(args.text, args.encoding_type)
            print(f"{args.encoding_type.capitalize()} Encoded Text: {encrypted_data}")

if __name__ == "__main__":
    main()
