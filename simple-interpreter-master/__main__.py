from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser

slexer = SimpleLexer('text.txt')
sparser = SimpleParser(slexer)

sparser.prog()

