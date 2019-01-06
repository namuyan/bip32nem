from mnemonic import Mnemonic
from bip32nem import BIP32Key, parse_path
from nem_ed25519 import public_key, get_address

# https://qiita.com/nem_takanobu/items/aa84ed6f4729cbad9fcc
# https://github.com/namuyan/bip32utils
# https://techmedia-think.hatenablog.com/entry/2017/08/31/125000

words = 'news clever spot drama infant detail sword cover color throw foot primary when slender rhythm clog autumn ecology enough bronze math you modify excuse'
xprv = 'xprv9s21ZrQH143K3EGRfjQYhZ6fA3HPPiw6rxopHKXfWTrB66evM4fDRiUScJy5RCCGz98nBaCCtwpwFCTDiFG5tx3mdnyyL1MbHmQQ19BWemo'
xpub = 'xpub661MyMwAqRbcFiLtmkwZ4h3Pi57soBexEBjR5hwH4oP9xtz4tbyTyWnvTb44oGpDbVacdJcga8g26sn7KBYLaerJ54LHqki34DwDq42XRfL'
language = 'english'


def test_with_sec():
    # m / purpose' / coin_type' / account' / change / address_index
    path = "m/44'/0'/0'/0/0"
    m = Mnemonic(language)
    seed = m.to_seed(words)
    print("path", path)
    print("seed", seed.hex())
    key = BIP32Key.fromEntropy(seed)
    m = key
    for n in parse_path(path):
        m = m.ChildKey(n)
    m.dump()
    if m.public is False:
        sk = m.PrivateKey().hex()
        pk = public_key(sk)
        ck = get_address(pk)
        print("sk", sk)
        print("pk", pk)
        print("ck", ck)


def test_with_pub():
    path = "m/0/0/0"
    m = Mnemonic(language)
    seed = m.to_seed(words)
    print("path", path)
    print("seed", seed.hex())
    key = BIP32Key.fromExtendedKey(xpub, public=True)
    m = key
    for n in parse_path(path):
        m = m.ChildKey(n)
    m.dump()
    if m.public is False:
        sk = m.PrivateKey().hex()
        pk = public_key(sk)
        ck = get_address(pk)
        print("sk", sk)
        print("pk", pk)
        print("ck", ck)


if __name__ == '__main__':
    test_with_sec()
    print()
    test_with_pub()
