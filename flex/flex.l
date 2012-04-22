%{

#define T_SOURCE_FILE   "source.out"
#define T_ERR_FILE      "errors.out"
#define T_COM_FILE      "comments.out"
#define T_STAT_FILE     "stat.out"

int g_newline = 0;
int g_linecounter = 0;
int g_charcounter = 0;
int g_multi_comm = 0;

%}

WHITESPACES     [ \t]*
NEWLINES        (\n|$)
TOKEN           ":"|":="|"/*"|"*/"|"//"":"|","|";"|"-"|"_"|"("|")"|"["|"]"|"{"|"}"|"%"|"<"|">"|"&"|"&&"|"||"|"<="|">="|"="|"\""|"\'"|"+"|"/"|"*"|"!="|"."|"#"
KEYWORDS        "auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"swtich"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while"
PREPROCESSOR    "#define"|"#include"|"#if"|"#elif"
DIGIT           [[:digit:]]
LETTER          [[:alpha:]]
ALPHANUM        [[:alphanum:]]
FLOAT           {DIGIT}+"."{DIGIT}+
INT             {DIGIT}+
ID              ({LETTER})({DIGIT}|{LETTER}|_)*
IDERROR         ({DIGIT}|_)+({DIGIT}|{LETTER}|_)+
MULT_COM        "/*"([^*]|("*"+[^*/]))*"*/"
SING_COM        "//"(.*)$

%%

{WHITESPACES} {
        whitespace_handler(yytext);
}

{MULT_COM} {
        multi_comment_handler(yytext);
}

{SING_COM} {
        single_comment_handler(yytext);
}

{NEWLINES} {
        newline_handler(yytext);
}

{TOKEN} {
        token_handler(yytext);
}

{FLOAT} {
        float_handler(yytext);
}

{INT} { int_handler(yytext);
}

{PREPROCESSOR} {
        preprocessor_handler(yytext);
}

{KEYWORDS} {
        keyword_handler(yytext);
}

{ID} {
        identifier_handler(yytext);
}

{IDERROR} {
        iderror_handler(yytext);
}

%%

void count_chars(char *yytext)
{
        g_charcounter = strlen(yytext);
}

int newline_handler(char *newlines)
{
        g_linecounter++;
        g_charcounter = 0;
        return 0;
}

int whitespace_handler(char *whitespaces)
{
        count_chars(whitespaces);
        return 0;
}

int preprocessor_handler(char *preprocessor)
{
        count_chars(preprocessor);
        printf("<keyword, %s>\n", preprocessor);
        return 0;
}

int keyword_handler(char *keywords)
{
        count_chars(keywords);
        printf("<keyword, %s>\n", keywords);
        return 0;
}

int identifier_handler(char *keywords)
{
        count_chars(keywords);
        printf("<id, %s>\n", keywords);
        return 0;
}

int iderror_handler(char *iderror)
{
        count_chars(iderror);
        FILE *fd = fopen(T_ERR_FILE, "w");
        fprintf(fd, "[!!] Wrong identifier in line '%d', column '%d'\n", g_linecounter, g_charcounter);
        return 0;
}

int write_stat()
{
        FILE *fd = fopen(T_STAT_FILE, "w");
        fprintf(fd, "***************************************************\n");
        fprintf(fd, "* Lines\t\t=\t%d\n", g_linecounter);
        fprintf(fd, "***************************************************\n");
        return 0;
}

int multi_comment_handler(char *multicomment)
{
        return 0;
}

int single_comment_handler(char *singlecomment)
{
        return 0;
}

int token_handler(char *token)
{
        g_charcounter = strlen(token);
        printf("<%s>\n", yytext);
        return 0;
}

int float_handler(char *strfloat)
{
        g_charcounter = strlen(strfloat);
        printf("<%s>\n", yytext);
        return 0;
}

int int_handler(char *strint)
{
        g_charcounter = strlen(strint);
        printf("<%s>\n", yytext);
        return 0;
}

int main(int argc, char **argv)
{

        if ( argc > 1 )
                yyin = fopen(argv[1], "r");
        else
                yyin = stdin;
        yylex();

        write_stat();

        fprintf(stderr, "***************************************************\n");
        fprintf(stderr, "* Output source  file:  %s\n", T_SOURCE_FILE);
        fprintf(stderr, "* Output error   file:  %s\n", T_ERR_FILE);
        fprintf(stderr, "* Output stat    file:  %s\n", T_STAT_FILE);
        fprintf(stderr, "* Output comment file:  %s\n", T_COM_FILE);
        fprintf(stderr, "***************************************************\n");
        return 0;
}
