import wikipedia

def searcher (question):
  answer = wikipedia.summary(question).split(".")
  for line in answer:
    print(line)
    
if __name__ == "_main__":
  question = "Wikipedia"
  searcher (question)