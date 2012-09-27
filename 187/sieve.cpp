#include <iostream>
#include <time.h>
using namespace std;
typedef unsigned long long ui;

const ui MAX=100000000;
bool sieve[MAX];

int main() {
    double time = clock();
    ui i, j;
    ui cant = 0;

    for (i = 2; i < MAX; i++) {
        sieve[i] = 1;
    }
    sieve[0] = 0;
    sieve[1] = 0;

    for (i = 2; i*i < MAX; i++) {
        if (sieve[i] == 0) continue;
        for (j = i*i; j < MAX; j += i) {
            sieve[j] = 0;
        }
    }

    /*
    for (i = 2; i < MAX; i++) {
        if (sieve[i] == 1) cout << i << endl;
    }

    i = MAX - 1;
    while (i >= 2) {
        j = 2;
        if (sieve[i] == 1) {
            while (j <= i) {
                if (i*j > MAX) break;

                if (sieve[j] == 1) {
                    cant++;
                }

                j++;
            }
        }
        i--;
    }

    cout << cant << endl;*/

    cout << (clock() - time) / 1000000. << endl;

    return 0;
}

