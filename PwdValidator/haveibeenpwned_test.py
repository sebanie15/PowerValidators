

from .haveibeenpwned import haveibeenpwned


def test_haveibeenpwned_at_least_one(requests_mock):
    data = '1692067afd8bd5522a15b912826268e5a53:1\n38ab81692067afd8bd5522a15b912826268e5a52:2'
    requests_mock.get("https://api.pwnedpasswords.com/range/38ab8", text=data)
    assert haveibeenpwned('aB5hJ#$1kk09023#%#hjadADS') == True
    # 38ab8

def test_haveibeenpwned_zero(requests_mock):
    data = '1692067afd8bd5522a15b912826268e5a52:0'
    requests_mock.get("https://api.pwnedpasswords.com/range/38ab8", text=data)
    assert haveibeenpwned('aB5hJ#$1kk09023#%#hjadADS') == False
