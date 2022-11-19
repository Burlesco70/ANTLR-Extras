from antlr4 import CommonTokenStream, InputStream, TerminalNode

from entity_parser.AntlrEntityLexer import AntlrEntityLexer
from entity_parser.AntlrEntityParser import AntlrEntityParser

def handle_tree(tree, lvl=0):
    '''
    Funzione ricorsiva che visita l'albero e lo visualizza, stampando i token terminali
    '''
    for child in tree.getChildren():
        if isinstance(child, TerminalNode):
            print(lvl*'│ ' + '└─', child, f'({AntlrEntityParser.symbolicNames[child.getSymbol().type]})')
        else:
            handle_tree(child, lvl+1)

CODE = '''module Insurance {
    entity Vehicle {
        licensePlate: string;
        year: integer;
        owner: Person;
    }

    entity Person {
        name: string;
        address: string;
        age: integer;
    }
}'''
input = InputStream(CODE)
lexer = AntlrEntityLexer(input)
token_stream = CommonTokenStream(lexer)
parser = AntlrEntityParser(token_stream)
tree = parser.module()
handle_tree(tree)