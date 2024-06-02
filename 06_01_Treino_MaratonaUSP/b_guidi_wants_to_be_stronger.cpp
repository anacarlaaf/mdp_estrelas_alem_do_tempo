#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int main()
{
    string cepe, guidi;
    cin>>guidi;
    cin>>cepe;
    int m = guidi.size();
    int n = cepe.size();
    int mt[m+1][n+1];

    for(int i=0; i<(m+1); i++){
        for(int j=0; j<n+1; j++){
            mt[i][j] = 0;
        }
    }

    for(int i=1; i<(m+1); i++){
        for(int j=1; j<n+1; j++){
            if(guidi[i-1]==cepe[j-1]){
                mt[i][j] = mt[i-1][j-1] + 1;
            }else{
                mt[i][j] = max(mt[i-1][j], mt[i][j-1]);
            }
        }
    }

    cout<<mt[m][n]<<endl;
    return 0;
}
