from pathlib import Path


path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
contents = contents.rstrip()
print(contents)