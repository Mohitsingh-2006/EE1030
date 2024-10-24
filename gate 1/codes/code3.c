#include <stdio.h>
#include <string.h>

void main()
{
    char s[80], *p;
    int sum = 0;
    p = s;
    gets(s);
    while (*p)
    {
        if (*p == '1')
            sum = 2*sum + 1;
        else if (*p == '0')
            sum = sum * 2;
        else
            printf("invalid string");
        p++;
    }
    printf("%d", sum);
}
