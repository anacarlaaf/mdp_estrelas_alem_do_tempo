#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>
#include <string>

using namespace std;

/*
int q, n;
    cin>>q>>n;
    vector<long long> lucky(q);
    vector<int> used(n);
    vector<long long> deck(n);
    map<int, vector<long long>> mp;
    for(int i=0; i<q; i++){
        cin>>lucky[i];
    }

    for(int i=0; i<n; i++){
        cin>>deck[i];
        used[i] = 0;
    }

*/

int main()
{
    int s;
    cin>>s;
    map<int, int> mp;
    vector<int> posicoes;
    mp[1] = 15;
    mp[2] = 12;
    mp[3] = 10;
    int j = 9;
    for(int i=4; i<=12; i++){
        mp[i] = j;
        j--;
    }

    int maior = 1;
    int soma = 0;
    while(s>0){
        if(s>=mp[maior]){
            soma++;
            s = s - mp[maior];
            posicoes.push_back(maior);
        }else{
            maior++;
        }
    }

    cout<<soma<<endl;
    for(int p : posicoes){
        cout<<p<< " ";
    }
    return 0;
}
