//Soluzione LuissMatics 2020
//Task n.3 "Fred"
//Carlo Malagnino

#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, M;

    cin >> T;

    for(int t=1;t<=T;t++){

        cin >> M;

        vector<string>U(M);
        vector<int>nP(M);
        vector<int>par(M, 0);
        vector<int>G(M, 0);
        vector<int>R(M, 0);

        for(int i=0;i<M;i++){
            cin >> U[i];
        }
        for(int i=0;i<M;i++){
            cin >> nP[i];
        }
        getchar();
        for(int i=0;i<M;i++){
            for(int j=0;j<nP[i];j++){
                string post;
                int parole=0;
                getline(cin, post);
                for(int c=0;c<post.size();c++){
                    if(post[c]==' '){
                        parole++;
                    }
                }
                if(post.size()>0){
                    parole++;
                }
                par[i]+=parole;

                string like;
                getline(cin, like);
                int last=0;
                vector<string>utL;
                for(int c=0;c<like.size();c++){
                    if(like[c]==' '){
                        utL.push_back(like.substr(last,c-last));
                        last=c+1;
                    }
                }
                if(like.size()>0){
                    utL.push_back(like.substr(last));
                }
                for(int l=0;l<utL.size();l++){
                    for(int u=0;u<M;u++){
                        if(U[u]==utL[l]){
                            G[u]++;
                            if(U[u]!= U[i]) R[i]++;
                        }
                    }
                }
            }
        }
        double masF=-1, fred;
        string masU;
        for(int i=0;i<M;i++){
            fred=double(double(par[i])/double(nP[i])*double(R[i])/double(G[i]+1));
            if(fred>masF || (fred==masF && masU>U[i])){
                masF=fred;
                masU=U[i];
            }
        }
        cout << "Case #" << t << ": " << masU << "\n";
    }
}
