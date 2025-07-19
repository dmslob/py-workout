import zlib

phrase = b'witch which has which witches wrist watch'
phrase_len = len(phrase)
print(f'Phrase length: {phrase_len}')

compressed_phrase = zlib.compress(phrase)

print(f'Compressed phrase: {len(compressed_phrase)}')
print(f'Decompressed phrase: {zlib.decompress(compressed_phrase)}')
print(f'CRC-32 checksum of phrase: {zlib.crc32(phrase)}')
