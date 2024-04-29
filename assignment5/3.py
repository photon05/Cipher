import hashlib
import time


def sha512_hash(message):
    message = message.lower()

    hash_object = hashlib.sha512()

    hash_object.update(message.encode())

    hash_hex_digest = hash_object.hexdigest()

    return hash_hex_digest


input_string = "Hello World"
print("Input string:", input_string)
start_time = time.time()
hash_digest = sha512_hash(input_string)
end_time = time.time()
print("SHA-512 Hash Digest:", hash_digest)
print("Hashing Time:", end_time - start_time, "seconds")
