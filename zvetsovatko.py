def zvetsi_pismena(soubor):
    with open(soubor, 'r') as f:
        text = f.read()
    text = text.upper()
    with open(soubor, 'w') as f:
        f.write(text)


import pytest

TEST_DATA = [
    ('Ahoj', 'AHOJ'),
    ('Nazdar Světe', 'NAZDAR SVĚTE'),
]


@pytest.fixture
def in_tmp_path(tmp_path, monkeypatch):
    print(tmp_path)
    monkeypatch.chdir(tmp_path)

    
@pytest.mark.parametrize(('text', 'text_upper'),
                         TEST_DATA)
def test_zvetsi_pozdrav(in_tmp_path, text, text_upper):
    with open('pozdrav.txt', 'w') as f:
        f.write(f'{text}\n')
    zvetsi_pismena('pozdrav.txt')
    with open('pozdrav.txt', 'r') as f:
        assert f.read() == f'{text_upper}\n'
   