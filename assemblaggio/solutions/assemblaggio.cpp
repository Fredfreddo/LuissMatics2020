//Soluzione LuissMatics 2020
//Task n.4 "Assemblaggio"
//Carlo Malagnino

#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, N;
    string ris;

    cin >> T;

    for(int t=1;t<=T;t++){

        cin >> N;
        cin >> ris;

        int pos=0, last=0, j;

        for(int i=1;i<N;i++){
            string s;
            cin >> s;

            bool st=false;
            for(j=last+1;j<ris.size() && !st;j++){
                st=true;
                for(pos=0;pos<s.size() && j+pos<ris.size() && st;pos++){
                    if(s[pos]!=ris[j+pos])
                        st=false;
                }
            }
            if(st && pos==s.size()){
                    last=j-1;
            }
            if(st && pos<s.size() && j-1+pos==ris.size()){
                ris=ris+s.substr(pos);
                last=j-1;
            }
            if(!st){
                last=ris.size();
                ris=ris+s;
            }
        }

        cout << "Case #" << t << ": " << ris.size() << "\n";
    }
}
