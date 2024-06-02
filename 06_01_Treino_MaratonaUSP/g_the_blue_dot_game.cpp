#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>
#include <string>

using namespace std;

/*
0 1 1
int q, n;
    cin>>q>>n;
    vector<string> lucky(q);
    vector<int> used(n);
    vector<char> deck(n);
    map<int, vector<long long>> mp;
    for(int i=0; i<q; i++){
        cin>>lucky[i];
    }

    for(int i=0; i<n; i++){
        cin>>deck[i];
        used[i] = 0;
    }

    for(int i=0; i<q; i++){

    }

    1 1 1 1 0 0
*/

int main() {
    int n, q=0, z=0;
    cin >> n;


    for (int i=0; i<n;i++) {
        int dot;
        cin >> dot;
        if (dot == 1) {
            q++;
        }else{
            z++;
        }
    }

    if(n==1)
        cout << 1 << endl;
    else{
        if(q==n){
            cout<<n<<endl;
        }else{
            cout<<q+1<<endl;
        }
    }

    return 0;
}
