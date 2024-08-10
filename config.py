import pandas, re, string

def opener(sentence : str):
  outlist = [r'[^\w\s]', r'\d+|\n']
  outlist.append(r'\n|RT|USER|URL|Retweeted|(http|https)://\S+')
  for out in outlist:
    sentence = re.sub(out, "", sentence)
  return result

def stopper(sentence):
  stopwords = pandas.read_csv("./document/stopwordbahasa.csv", encoding='ISO-8859-1')
  stopwords = stopwords.stopword.values
  inlist = sentence.split(" ")
  text = ' '.join([i if i not in stopwords for i in inlist])
  text = re.sub('  +', ' ', text)
  text = text.strip()
  return text

def charlean(sentence):
  inlist = sentence.split(' ')
  text = ' '.join([i if i not in special_char for i in inlist])
  st = re.sub('  +', ' ', text)
  result = st.strip()
  return result

def almopal(text):
  inlist = text.split(" ")
  result = [alaytable[i] if word in alaytable else i for i in inlist]
  return ' '.join(result)

def runner(sentence : str) -> str:
  sentence = sentence.lower()
  sentence = opener(sentence)
  locklist = [stopper, charlean, almopal]
  for lock in locklist:
    sentence = lock(sentence)
  return sentence

def unlock():
  return result