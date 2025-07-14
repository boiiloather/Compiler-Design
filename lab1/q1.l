// Program to Count Vowels and Consonants
%{
int vowel = 0, consonant = 0;
%}
%%
[aAeEiIoOuU]     { vowel++; }
[a-zA-Z]         { consonant++; }
.|\n             ;
%%
int main() {
    yylex();
    printf("Vowels: %d\nConsonants: %d\n", vowel, consonant);
    return 0;
}
