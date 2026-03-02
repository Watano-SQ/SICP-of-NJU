#include<stdio.h>
int main() {
    int n;
    scanf("%d",&n);
    char arr[n+2][n+2];
    //边界设置为o
    for(int i=0;i<n+2;i++) {
        arr[0][i]='o';
        arr[i][0]='o';
        arr[i][n+1]='o';
        arr[n+1][i]='o';
    }

    for (int i=1;i<n+1;i++) {
        for (int j=1;j<n+2;j++) {
            scanf("%c",&arr[i][j]);//%c
        }
    }    for (int i=1;i<n+1;i++) {
        for (int j=1;j<n+2;j++) {
            printf("%c\n",arr[i][j]);
        }
    }

    return 0;

}