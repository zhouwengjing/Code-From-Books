#include <stdio.h>


int BinSearch2(int r[], int low, int high, int x) {
    // 数组r[1]~r[n]存放查找集合
    if (low>high)
        return 0;
    else {
        int mid = (low+high) / 2;
        if (x<r[mid])
            return BinSearch2(r, low, mid-1, x);
        else if (x>r[mid])
            return BinSearch2(r, mid+1, high, x);
        else
            return mid;
    }
}

int main() {
    int arr[8] = {2, 4, 6, 8, 10, 12, 14, 16};
    int a = BinSearch2(arr, 0, 7, 14);
    printf("%d", a);
}