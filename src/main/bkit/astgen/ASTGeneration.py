from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.many_declare().accept(self))
    
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
        if ctx.array_declare():
            return ctx.array_declare().accept(self)
        elif ctx.type_list():
            return [VarDecl(Id(ctx.ID().getText()), None, ctx.type_list().accept(self))]
        return [VarDecl(Id(ctx.ID().getText()), None, None)]
    
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