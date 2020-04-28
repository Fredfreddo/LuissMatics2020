//Soluzione LuissMatics 2020
//Task n.2 "COVID-19"
//Carlo Malagnino

#include<bits/stdc++.h>

#define NMAX 110

using namespace std;

int T,N,Z,D;
int X[NMAX],Y[NMAX],Xz[NMAX],Yz[NMAX],Cz[NMAX],cont[NMAX];

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> T;
    for(int t=1;t<=T;t++){
        cin >> N;
        for(int i=0;i<N;i++){
            cin >> X[i] >> Y[i];
            cont[i]=0;
        }

        cin >> Z;
        for(int i=0;i<Z;i++){
            cin >> Xz[i] >> Yz[i] >> Cz[i];
        }
        cin >> D;

        int massi=0, massip=0;
        for(int i=0;i<N;i++){
            for(int j=0;j<Z;j++){
                double dist=sqrt(pow(X[i]-Xz[j], 2) + pow(Y[i]-Yz[j], 2));
                if(dist<=D){
                    cont[i]+=Cz[j];
                }
            }
            if(massi<cont[i]){
                massi=cont[i];
                massip=i;
            }
        }
        cout << "Case #" << t << ": " << massip+1 << "\n";
    }
}

