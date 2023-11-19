#include <string.h>
#include <stdio.h>
#include <stdlib.h>



int main()
{
    int key[] = {74, 109, 112, 77, 52, 0, 110};

    char flag[28];
    int numbers[28] = {44, 75, 54, 125, 85, 113, 52, 51, 31, 52, 113, 45, 115, 31, 52, 112, 31, 39, 115, 52, 31, 38, 21, 100, 12, 114, 63, 19};
    for(int i = 0 ; i < 28 ; i++)
    {
        flag[i] = numbers[i];
    }

    char* output = malloc(sizeof(flag) + 1);
    strncpy(output, flag, sizeof(flag));
    output[28] = '\0';

    int output_len = 28;
    int key_len = 7;

    for(int k = 0 ; k < 128 ;k++)
    {
        key[5] = k;
        for(int i = 0; i < output_len - key_len + 1; i++) {
            for(int j = 0; j < key_len; j++) {
                output[i + j] ^= key[j];
            }
        }
        char *str = output;
        printf("%s\n",str);
        
        while(*str)
        {
            printf("%d ",*str);
            printf("(%c)\t",*str);
            str++;
        }
        break;
    }
    free(output);
    return 0;
}

