#include "stdio.h"

int BinSearch2(int r[], int low, int high, int x) {
    // 数组 r[1]~r[n]存放查找集合
    if(low>high) return 0;
    while(low<=high) {
        if(r[low]==x)
            return low;
        if(r[high]==x)
            return high;
        int mid = low + (high - low) / 2;
        if(r[mid]==x)
            return mid;
        if(r[mid]<x)
            low = mid + 1;
        else
            high = mid - 1;
    }
    if(low>high)
        return 0;
}

int main() {
    int r[8] = {3, 6, 9, 12, 15, 18, 21, 24};
    printf("%d", BinSearch2(r, 0, 7, 21));
}