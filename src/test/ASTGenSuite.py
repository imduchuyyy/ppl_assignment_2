import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x,y= True;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],BooleanLiteral("true"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

   