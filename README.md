# ANTLR-Extras

Esperimenti seguendo il tutorial ANTLR4 di Python Biella Group & Strumenta

## Per generare i parsers

### Entity language
java org.antlr.v4.Tool -Dlanguage=Python3 AntlrEntityLexer.g4 -o ../entity_parser

java org.antlr.v4.Tool -Dlanguage=Python3 AntlrEntityParser.g4 -o ../entity_parser

### XML
java org.antlr.v4.Tool -Dlanguage=Python3 XMLLexer.g4 -o ../xml_parser

java org.antlr.v4.Tool -Dlanguage=Python3 XMLParser.g4 -o ../xml_parser

## Custom "visitors"

- visualizza_albero_entity.py

Il codice in input è inserito nello script

- visualizza_albero_xml.py NOMEFILE.XML

XML in input da file; esempi nella cartella xml_examples

