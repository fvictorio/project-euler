#include <iostream>
#include <time.h>
using namespace std;

typedef unsigned long long ull;

const ull MAX = 10000000;
ull divisores[MAX];

ull gcd(ull a, ull b) {
    ull c;

    if (b > a) {c = a; a = b; b = c;} // intercambiar

    while (1) {
        c = a % b;
        if (c == 0) return b;
        a = b;
        b = c;
    }
}

ull calcular_divisores(ull n) {
    ull result = 2;
    ull i, j;


    for (i = 2; i*i < n; i++) {
        if (n % i == 0) {
            result += 2;
            j = n/i;
            if ( (j % i != 0) and (gcd(i, j) == 1) ) {
                return divisores[i]*divisores[j];
            }
        }
    }

    if (i*i == n) result += 1;
    
    return result;
}

int main () {
    ull i, cant;
    double start = clock();


    /*
    cout << calcular_divisores(36) << " " << calcular_divisores(4) << " " << calcular_divisores(9) << endl;
    return 0;
    */
    i = 3;
    cant = 0;
    divisores[1] = 1;
    divisores[2] = 2;

    while (i < MAX) {
        divisores[i] = calcular_divisores(i);
        if (divisores[i-1] == divisores[i]) {
            cant++;
        }
        i++;
    }

    /*
    for (i = 2; i < 100; i++) {
        cout << i << " tiene " << divisores[i] << " divisores." << endl;
    }
    */

    cout << cant << endl;
    cout << "tiempo: " << clock() - start << endl;

    return 0;
}

