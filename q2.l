//Program to Identify Numbers and Words
%%
[0-9]+          { printf("Number: %s\n", yytext); }
[a-zA-Z]+       { printf("Word: %s\n", yytext); }
.|\n            ;
%%
int main() {
    yylex();
    return 0;
}
