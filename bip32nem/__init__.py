from bip32nem.BIP32Key import BIP32Key, BIP32_HARDEN


def parse_path(nstr):
    """"""
    r = list()
    for s in nstr.split('/'):
        if s == 'm':
            continue
        elif s.endswith("'") or s.endswith('h'):
            r.append(int(s[:-1]) + BIP32_HARDEN)
        else:
            r.append(int(s))
    return r


__all__ = [
    "BIP32Key",
    "BIP32_HARDEN",
    "parse_path",
]