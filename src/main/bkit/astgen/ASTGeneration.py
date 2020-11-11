from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.many_declare().accept(self))
    
    #-------------------- VARIABLE DECLARE ---------------------
    def visitMany_declare(self,ctx:BKITParser.Many_declareContext):
        if ctx.many_declare():
            return ctx.declare().accept(self) + ctx.many_declare().accept(self)
        else:
            return ctx.declare().accept(self)
    
    def visitDeclare(self, ctx:BKITParser.DeclareContext):
        if ctx.var_declare():
            return ctx.var_declare().accept(self)
        elif ctx.func_declare():
            return ctx.func_declare().accept(self)
    
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return ctx.ids_list().accept(self)
    
    def visitIds_list(self, ctx:BKITParser.Ids_listContext):
        if ctx.ids_list():
            return ctx.id_declare().accept(self) + ctx.ids_list().accept(self)
        elif ctx.id_declare():
            return ctx.id_declare().accept(self)
    
    def visitId_declare(self, ctx:BKITParser.Id_declareContext):
        id = Id(ctx.ID().getText())
        array_declares = self.visit(ctx.array_declares()) if ctx.array_declares() else None
        type_list = self.visit(ctx.type_list()) if ctx.type_list() else None
        return [VarDecl(Id(ctx.ID().getText()), array_declares, type_list)]

    def visitVar_declare_list(self, ctx:BKITParser.Var_declare_listContext):
        if ctx.var_declare_list():
            return self.visit(ctx.var_declare()) + self.visit(ctx.var_declare_list())
        else:
            return self.visit(ctx.var_declare())
        
    def visitId_var(self, ctx:BKITParser.Id_varContext):
        if ctx.ID():
            return [VarDecl(Id(ctx.ID().getText()), None, None)]
        else:
            return [self.visit(ctx.array_id())]

    # --------------------------- ARRAY DECLARE -----------------------------
    def visitArray_declares(self, ctx:BKITParser.Array_declaresContext):
        if ctx.array_declares():
            return self.visit(ctx.array()) + self.visit(ctx.array_declares())
        else:
            return self.visit(ctx.array())
    
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return [ctx.INTLIT().getText()]

    def visitArray_id(self, ctx:BKITParser.Array_idContext):
        return ArrayCell(ctx.ID().getText() ,self.visit(ctx.array_declares()))

    # ------------------------- FUNCTION DECLARE --------------------
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        idFunc = self.visit(ctx.header_stm())
        param = self.visit(ctx.paramater_stm()) if ctx.paramater_stm() else []
        body = self.visit(ctx.body_stm())
        return [FuncDecl(idFunc, param, body)]
    
    def visitHeader_stm(self, ctx:BKITParser.Header_stmContext):
        return Id(ctx.ID().getText())

    # -------------------------- PARAMATER STATEMENT -------------------
    def visitParamater_stm(self, ctx:BKITParser.Paramater_stmContext):
        return self.visit(ctx.paramater_list())
    
    def visitParamater_list(self, ctx:BKITParser.Paramater_listContext):
        if ctx.paramater_list():
            return self.visit(ctx.id_var()) + self.visit(ctx.paramater_list())
        else: 
            return self.visit(ctx.id_var())

    #------------------- BODY STATEMENT -----------------------
    def visitBody_stm(self, ctx:BKITParser.Body_stmContext):
        list_varDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        list_statement = self.visit(ctx.statement_list())
        return (list_varDecl, list_statement) # tuple
    
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        if ctx.statement_list():
            return self.visit(ctx.statement()) + self.visit(ctx.statement_list())
        else:
            return self.visit(ctx.statement())
    
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return [self.visit(ctx.getChild(0))]
    
    #---------------------- FUNCTION DECLARE ----------------
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        lhs = ctx.ID().getText() if ctx.ID() else self.visit(ctx.array_id())
        rhs = self.visit(ctx.expressions())
        return Assign(lhs, rhs)
    
    # ---------------------- IF STATEMENT --------------------
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        ifThenStm = self.visit(ctx.if_then_statement())
        elseIfStm = self.visit(ctx.else_if_statements()) if ctx.else_if_statements() else []
        elseStm  = self.visit(ctx.else_statement())
        return If(ifThenStm + elseIfStm, elseStm)

    def visitIf_then_statement(self, ctx:BKITParser.If_then_statementContext):
        expressions = self.visit(ctx.expressions())
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return [(expressions, varsDecl, statements)] #tuple
    
    def visitElse_if_statements(self, ctx:BKITParser.Else_if_statementsContext):
        if ctx.else_if_statements():
            return self.visit(ctx.else_if_statement()) + self.visit(ctx.else_if_statements())
        else:
            return self.visit(ctx.else_if_statement())
    
    def visitElse_if_statement(self, ctx:BKITParser.Else_if_statementsContext):
        expressions = self.visit(ctx.expressions())
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return [(expressions, varsDecl, statements)] #tuple
    
    def visitElse_statement(self, ctx:BKITParser.Else_statementContext):
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return (varsDecl, statements) #tuple

    #---------------------- FOR STATEMENT ------------------------
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        (id, expr1, expr2, expr3) = self.visit(ctx.for_condition())
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return For(id, expr1, expr2, expr3, (varsDecl, statements))
    
    def visitFor_condition(self, ctx:BKITParser.For_conditionContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expressions(0))
        expr2 = self.visit(ctx.expressions(1))
        expr3 = self.visit(ctx.expressions(2))
        return (id, expr1, expr2, expr3)

    #---------------------- WHILE STATEMENT ----------------------
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        expressons = self.visit(ctx.expressions())
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return While(expressons, (varsDecl, statements))
    
    #---------------------- DO WHILE STATEMENT -------------------
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        expressons = self.visit(ctx.expressions())
        varsDecl = self.visit(ctx.var_declare_list()) if ctx.var_declare_list() else []
        statements = self.visit(ctx.statement_list()) if ctx.statement_list() else []
        return Dowhile((varsDecl, statements), expressons)

    #---------------------- BREAK STATEMENT ----------------------
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()

    #---------------------- CONTINUE STATEMENT -------------------
    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return Continue()

    #---------------------- FUNCTION CALL STATEMENT --------------
    def visitFunction_call_statement(self, ctx: BKITParser.Function_call_statementContext):
        id = Id(ctx.ID().getText())
        list_expr = [self.visit(expressions) for expressions in ctx.expressions()] if ctx.expressions() else []
        return CallStmt(id, list_expr)
    
    #---------------------- RETURN STATEMENT ---------------------
    def visitReturn_statement(self, ctx: BKITParser.Return_statementContext):
        return Return(self.visit(ctx.expressions()))
    
    #---------------------- EXPRESSION ---------------------------
    def visitExpressions(self, ctx: BKITParser.ExpressionsContext):
        


    # --------------------- TYPE LIST ----------------------------
    def visitType_list(self, ctx:BKITParser.Type_listContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(float(ctx.STRINGLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(bool(ctx.TRUE().getText()))
        elif ctx.FALSE():
            return BooleanLiteral(bool(ctx.FALSE().getText()))