import unittest
from TestUtils import TestAST
from AST import *

#Program([ FuncDecl(Id("main"),[],([],[]))])

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

    def test_declare_func5(self):
        input = """
        Function: main
        Parameter: s = 3, z = 4
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[VarDecl(Id("s"),[], IntLiteral(3)), VarDecl(Id("z"),[], IntLiteral(4))],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_declare_func4(self):
        input = """
        Function: main
        Parameter: s = 3, z = 4
        Body:
            print(x);
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[VarDecl(Id("s"),[], IntLiteral(3)), VarDecl(Id("z"),[], IntLiteral(4))],([],[CallStmt(Id("print"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    
    def test_declare_var7(self):
        input = """
        Var:x = "hello", z = 10, y = 1.1 ;
        """
        expect = Program([VarDecl(Id("x"),[],StringLiteral("hello")), VarDecl(Id("z"),[],IntLiteral(10)), VarDecl(Id("y"),[],FloatLiteral(1.1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_declare_var8(self):
        input = """
        Var:x, z[3] = 10, y = 1.1 ;
        """
        expect = Program([VarDecl(Id("x"),[],None), VarDecl(Id("z"),[3],IntLiteral(10)), VarDecl(Id("y"),[],FloatLiteral(1.1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_declare_var9(self):
        input = """
        Function: main
        Body:
            Var:x, z[3] = 10, y = 1.1 ;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None), VarDecl(Id("z"),[3],IntLiteral(10)), VarDecl(Id("y"),[],FloatLiteral(1.1))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_simple_func5(self):
        input = """Function: main
                    Parameter: a,b[1][2]
                    Body:
                    EndBody.
                    Function: foo
                    Body:
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[1,2],None)],([],[])),
                            FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    def test_var_declare10(self):
        input = """ Var:x={3,{3.5},7};"""
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(3),ArrayLiteral([FloatLiteral(3.5)]),IntLiteral(7)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_declare_func1(self):
        input = """
        Function: main
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_declare_func3(self):
        input = """
        Function: main
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[], None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    def test_assign_statement(self):
        input = """
        Function: main
        Body:
            x = 10;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_assign_statement1(self):
        input = """
        Function: main
        Body:
            x = "hello";
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),StringLiteral("hello"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_assign_statement2(self):
        input = """
        Function: main
        Body:
            x = 1.3;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),FloatLiteral(1.3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_assign_statement3(self):
        input = """
        Function: main
        Body:
            x = {1,3,4 };
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),ArrayLiteral([IntLiteral(1), IntLiteral(3), IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    
    def test_if_statement(self):
        input = """
        Function: main
        Body:
            If (a > b)
               Then a = 1.3;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[If([(BinaryOp('>', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.3))])], [])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_if_statement1(self):
        input = """
        Function: main
        Body:
            If (a > b)
               Then a = 1.3;
            Else a = 1.1;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[If([(BinaryOp('>', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.3))])], ([], [Assign(Id('a'), FloatLiteral(1.1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_if_statement2(self):
        input = """
        Function: main
        Body:
            If (a > b)
                Then a = 1.3;
            ElseIf (a == b)
                Then a = 1.1;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[If([(BinaryOp('>', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.3))]), (BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.1))]) ], None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_if_statement3(self):
        input = """
        Function: main
        Body:
            If (a > b)
                Then a = 1.3;
            ElseIf (a == b)
                Then a = 1.1;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[If([(BinaryOp('>', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.3))]), (BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.1))]) ], None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    
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
         self.assertTrue(TestAST.checkASTGen(input,expect,327))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    def test_return(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            Return x + 10;
        EndBody.
        """
        expect = Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                Return(BinaryOp('+', Id('x'), IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    
    def test_return1(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            Return x;
        EndBody.
        """
        expect = Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                Return(Id("x"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_if_statement4(self):
        input = """
        Function: main
        Body:
            If (a > b)
                Then a = 1.3;
            ElseIf (a == b)
                Then a = 1.1;
            Else a = 2.1;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[If([(BinaryOp('>', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.3))]), (BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), FloatLiteral(1.1))]) ], ([], [Assign(Id('a'), FloatLiteral(2.1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_for_statement(self):
        input = """
        Function: main
        Body:
            For(b = 3, b >= 0, b = b + 1)Do
                a = 1;
            EndFor.
        EndBody.
        """
        expect = Program([
        FuncDecl(Id("main"),[],([],[For(Id('b'), IntLiteral(3),BinaryOp('>=', Id('b'), IntLiteral(0)), BinaryOp('+', Id('b'), IntLiteral(1)), ([], [Assign(Id('a'), IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_for_statement2(self):
        input = """
        Function: main
        Body:
            For(b = 3, b >= 0, b = b + 1)Do
                If (b >= 0) Then b = 0;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([
        FuncDecl(Id("main"),[],([],[For(Id('b'), IntLiteral(3),BinaryOp('>=', Id('b'), IntLiteral(0)), BinaryOp('+', Id('b'), IntLiteral(1)), ([], [If([(BinaryOp('>=', Id('b'), IntLiteral(0)),[], [Assign(Id('b'), IntLiteral(0))])], ())]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_for_statement3(self):
        input = """
        Function: main
        Body:
            For(b = 3, b >= 0, b = b + 1)Do
                b = b + 1;
            EndFor.
        EndBody.
        """
        expect = Program([
        FuncDecl(Id("main"),[],([],[For(Id('b'), IntLiteral(3),BinaryOp('>=', Id('b'), IntLiteral(0)), BinaryOp('+', Id('b'), IntLiteral(1)), ([], [Assign(Id('b'), BinaryOp('+', Id('b'), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_while_statement(self):
        input = """
        Function: main
        Body:
            While(b <= 3)Do
                b = 1;
            EndWhile.
        EndBody.
        """
        expect = Program([
        FuncDecl(Id("main"),[],([],[While(BinaryOp('<=', Id('b'), IntLiteral(3)), ([], [Assign(Id('b'), IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_while_statement_1(self):
        input = """
        Function: main
        Body:
            While(b <= 3)Do
                For(b = 3, b >= 0, b = b + 1)Do
                    b = b + 1;
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = Program([
        FuncDecl(Id("main"),[],([],[While(BinaryOp('<=', Id('b'), IntLiteral(3)), ([], [For(Id('b'), IntLiteral(3),BinaryOp('>=', Id('b'), IntLiteral(0)), BinaryOp('+', Id('b'), IntLiteral(1)), ([], [Assign(Id('b'), BinaryOp('+', Id('b'), IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_do_while_statement(self):
        input = """
        Function: main
        Body:
            Do
                b = 1;
            While (b <= 3) EndDo.
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[Dowhile(([] ,[Assign(Id('b'), IntLiteral(1))]), BinaryOp('<=', Id('b'), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_do_while_statement2(self):
        input = """
        Function: main
        Body:
            Do
                If a == b Then a = 1;
                EndIf.
            While (b <= 3) EndDo.
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[Dowhile(([] ,[If([(BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), IntLiteral(1))])], None)]), BinaryOp('<=', Id('b'), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_continue_statement(self):
        input = """
        Function: main
        Body:
            Continue;
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_function_call_statement(self):
        input = """
        Function: main
        Body:
            check(a);
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[CallStmt(Id('check'), [Id('a')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_expression_statement(self):
        input = """
        Function: main
        Body:
            b = b + 1;
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[Assign(Id('b'), BinaryOp('+', Id('b'), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_expression_statement1(self):
        input = """
        Function: main
        Body:
            b = b > 1;
        EndBody.
        """
        expect = Program([ FuncDecl(Id("main"),[],([],[Assign(Id('b'), BinaryOp('>', Id('b'), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_function_call1(self):
        input = """Var: x = 5;
             Function: main
             Body:
                 printLn(x);
                 printLn(x, y);
             EndBody.
             """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printLn"), [Id("x")]),
                CallStmt(Id("printLn"), [Id("x"),Id("y")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    
    def test_return_statement1(self):
        input = """Var: x = 5;
             Function: main
             Body:
                Return;
             EndBody.
             """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([
                
            ], [
                Return(None)
            ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    
    def test_call_exp(self):
        input = """Var: x = 5;
             Function: main
             Body:
                a = valueOf(x);
             EndBody.
             """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([
                
            ], [
                Assign(Id('a'), CallExpr(Id('valueOf'), [Id('x')]))
            ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_index_operator(self):
        input = """Var: x = 5;
             Function: main
             Body:
                a = array[x];
             EndBody.
             """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([
                
            ], [
                Assign(Id('a'), ArrayCell(Id('array'), [Id("x")]))
            ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    
    def test_decale_array(self):
        input = """Var: x = 5;
             Function: main
             Body:
                array = {1,2,3};
             EndBody.
             """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([
                
            ], [
                Assign(Id('array'), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
            ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_for_statement4(self):
         input = """
         Function: main
         Body:
            For(b = 3, b >= 0, b = b + 1)Do
                var = a * (b - 10);
            EndFor.
         EndBody.
         """
         expect = Program([
             FuncDecl(Id("main"),[],([],
                 [For(Id("b"), IntLiteral(3),
                      BinaryOp( ">=", Id("b"), IntLiteral(0)), BinaryOp("+", Id("b"), IntLiteral(1)),
                      [[], [Assign(Id("var"), BinaryOp("*", Id("a") ,BinaryOp("-",Id("b"), IntLiteral(10))))]])]))])
         self.assertTrue(TestAST.checkASTGen(input,expect,348))