%{
#define T_COM_FILE      "comments.txt"

int g_comment = 0;
%}

%x     MUL_COM

START           "/*"
END             "*/"
SIMPLE          [^*\n]*
COMPLEX         "*"[^/\n]
NEWLINE         \n
WHITESPACE      [ \t]+

%%

{START} {
        g_comment = 1;
        BEGIN MUL_COM;
}
<MUL_COM>{SIMPLE}|{COMPLEX} {
        mul_com_handler(yytext);
}
<MUL_COM>{NEWLINE} {
        newline_handler();
}
<MUL_COM>{END}  {
        g_comment = 0;
        BEGIN 0;
}

.*|{NEWLINE} {}

%%

int newline_handler()
{
        if ( g_comment )
                printf("\n");
        return 0;
}

int mul_com_handler(char *comment_line)
{
        printf("Comment Line: %s", yytext);
        return 0;
}

int main(int argc, char **argv)
{

        if ( argc > 1 )
                yyin = fopen(argv[1], "r");
        else
                yyin = stdin;
        yylex();
        return 0;
}
