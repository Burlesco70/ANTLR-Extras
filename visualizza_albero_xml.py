import sys
from antlr4 import CommonTokenStream, FileStream, TerminalNode

from xml_parser.XMLLexer import XMLLexer
from xml_parser.XMLParser import XMLParser

def handle_xml_tree(tree, lvl=0, chiave='', valore='', diz={}) -> dict:
    '''
    Funzione ricorsiva che visita l'albero costruendo il dizionario tag:valore
    Ad ogni ricorsione ripasso chiave e valore temporanei e dizionario in costruzione
    '''
    for child in tree.getChildren():
        if isinstance(child, TerminalNode):
            if XMLParser.symbolicNames[child.getSymbol().type] == 'Name':
                # Compongo la chiave in base agli annidamenti
                chiave +=  str(child) + "|"
                #print(f'Chiave: {chiave}')
            elif XMLParser.symbolicNames[child.getSymbol().type] == 'TEXT':
                # Se trovo il valore XML
                valore += str(child)
                # Creo la chiave
                diz[chiave] = valore
                #print(diz)                
                #print(f'Valore: {valore}')
                # Ripulisco chiave e valore
                chiave = ''
                valore = ''
            # Uscita ricorsione valorizzando output
            elif XMLParser.symbolicNames[child.getSymbol().type] == 'PI':
                if str(child) == '<EOF>':
                    #print('Ho finito')
                    # Rimuovo chiavi senza valore (ovvero le chiavi che si sono
                    # create in corrispondenza ai tag di chiusura
                    return {k: v for k, v in diz.items() if v}
        else:
            handle_xml_tree(child, lvl+1, chiave, valore, diz)

# Input da file
input = FileStream(sys.argv[1])
lexer = XMLLexer(input)
token_stream = CommonTokenStream(lexer)
parser = XMLParser(token_stream)
tree = parser.document()
diz_html = handle_xml_tree(tree)
# Mostro risultato
print(diz_html)