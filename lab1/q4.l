//Program to Recognize Keywords
%%
"if"|"else"|"while"|"for"|"return" {
    printf("Keyword: %s\n", yytext);
}
[a-zA-Z_][a-zA-Z0-9_]* {
    printf("Identifier: %s\n", yytext);
}
[ \t\n]+        ;
.               ;
%%
int main() {
    yylex();
    return 0;
}
