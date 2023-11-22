#include <iostream>

using namespace std;

int possibleParenthesizations(int n) {
    if (n == 1) {
        return 1;
    }
    int sum = 0;
    for (int i = 1; i < n; i++) {
        sum += possibleParenthesizations(i) * possibleParenthesizations(n - i);
    }
    return sum;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Number of possible parenthesizations: " << possibleParenthesizations(n) << endl;
    return 0;
}