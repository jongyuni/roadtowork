import sys

N = int(input())
answer = []

for _ in range(N):
  sentence = sys.stdin.readline().split()
  reverse_sentence = []
  for word in sentence:
    reverse_word = word[::-1]
    reverse_sentence.append(reverse_word)
  answer.append(' '.join(reverse_sentence))

for sen in answer:
  print(sen)
