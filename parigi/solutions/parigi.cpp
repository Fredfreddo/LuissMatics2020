//Soluzione LuissMatics 2020
//Task n.1 "Parigi"
//Carlo Malagnino

#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, N;
    cin >> T;
    for(int t=1;t<=T;t++){
        int ris=0;
        cin >> N;
        getchar();
        set<string>l;
        for(int i=0;i<N;i++){
            string s;
            getline(cin, s);
            s=s.substr(12);
            if(l.count(s)==0){
                l.insert(s);
                ris++;
            }
        }
        l.clear();
        cout << "Case #" << t << ": " << ris << "\n";
    }
}
