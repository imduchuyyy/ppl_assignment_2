import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_declare(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x,y= True;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],BooleanLiteral("true"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_more_complex_program(self):
        input = """
         Function: main
         Body:
             x = 10;
         EndBody.
         """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_declare_var(self):
        input = """
        Var:x = 10;
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_declare_var1(self):
        input = """
        Var:x[3] = 10;
        """
        expect = Program([VarDecl(Id("x"),[3],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_declare_var2(self):
        input = """
        Var:x[3] = 9.3;
        """
        expect = Program([VarDecl(Id("x"),[3],FloatLiteral(9.3))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))


    def test_declare_var5(self):
        input = """
        Var:x[3] = "hello";
        """
        expect = Program([VarDecl(Id("x"),[3],StringLiteral("hello"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_declare_var6(self):
        input = """
        Var:x[3] = "hello", y = 1, z = 2.3;
        
        """
        expect = Program([VarDecl(Id("x"),[3],StringLiteral("hello")),VarDecl(Id("y"),[],IntLiteral(1)), VarDecl(Id("z"),[],FloatLiteral(2.3))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_declare_func(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_declare_func1(self):
        input = """
        Function: main
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_declare_func2(self):
        input = """
        Function: main
        Parameter: s, z
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[VarDecl(Id("s"),[], None), VarDecl(Id("z"),[], None)],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_declare_func2(self):
        input = """
        Function: main
        Parameter: s = 3, z = 4
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[VarDecl(Id("s"),[], IntLiteral(3)), VarDecl(Id("z"),[], IntLiteral(4))],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_simple_func4(self):
        input = """Function: main
                    Parameter: a,b[1][2]
                    Body:
                    EndBody.
                    Function: foo
                    Body:
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[1,2],None)],([],[])),
                            FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_for_in_for(self):
         input = """
         Function: main
         Body:
             For(b = 3, b >= 0, b = b + 1)Do
                For(b = 3, b >= 0, b = b + 1)Do
                    a = 3;
                EndFor.
             EndFor.
         EndBody.
         """
         expect = "Program([FuncDecl(Id(main)[],([][For(Id(b),IntLiteral(3),BinaryOp(>=,Id(b),IntLiteral(0)),BinaryOp(+,Id(b),IntLiteral(1)),[],[For(Id(b),IntLiteral(3),BinaryOp(>=,Id(b),IntLiteral(0)),BinaryOp(+,Id(b),IntLiteral(1)),[],[Assign(Id(a),IntLiteral(3))])])]))])"
         self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_break(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            Break;
            printLn(x);
        EndBody.
        """
        expect = Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                Break(),
                CallStmt(Id("printLn"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))