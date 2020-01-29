#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[100] = {0};
    int shift_number, i, h;
    char ch;
    for (i = 0; i <= 100; i++) {
        if ((ch = getchar())== '\n')
            break;
        a[i] = ch;
    }
    h = i;
    scanf("%d", &shift_number);
    for (i = 0; a[i]; i++) {
        if (a[i] >= 'A' || a[i] <= 'Z'){
            if (a[i] >= 'a')
                a[i] = 'a' + (a[i] - 'a' + shift_number) % 26;
                else if (a[i] >= 'A')
                    a[i] = 'A' + (a[i] - 'A' + shift_number) % 26;
        }
    }
    for (i = 0;i < h; i++)
        printf("%c", a[i]);
    return 0;
}
