//Program to Remove Comments
%%
"//".*          ; 
.|\n            { printf("%s", yytext); }
%%
int main() {
    yylex();
    return 0;
}
