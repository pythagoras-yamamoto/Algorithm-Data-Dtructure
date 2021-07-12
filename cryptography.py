#暗号化のアルゴリズム
import string


#シーザー暗号
def caesr_cipher(text: str, shift: int) -> str:
  result=''
  for char in text:
    if char.isupper():
      alphabet = string.ascii_uppercase
    elif char.islower():
      alphabet = string.ascii_lowercase
    else:
      result += char
      continue

    index = (alphabet.index(char) + shift) % len(alphabet)
    result += alphabet[index]


#エニグマ暗号
#todo



if __name__ == '__main__':
  print(caesr_cipher('zaaa35a', 2))


