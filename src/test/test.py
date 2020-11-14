from AST import *

expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10))])),
            FuncDecl(Id("sub"), [], ([], [
                Assign(Id("y"), IntLiteral(20))]))])

print(str(expect))
