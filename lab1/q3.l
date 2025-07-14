//Program to Count Lines, Words, and Characters
%{
int lines = 0, words = 0, chars = 0;
%}
%%
[^\s\n]+        { words++; chars += yyleng; }
\n              { lines++; chars++; }
.               { chars++; }
%%
int main() {
    yylex();
    printf("Lines: %d\nWords: %d\nCharacters: %d\n", lines, words, chars);
    return 0;
}
