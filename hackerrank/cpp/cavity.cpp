#include<iostream>
#include<cstdio>

using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    long long int a[n+1],b[m+1],c[m+1];
    for(int k=1;k<=n;k++){
        cin>>a[k];
    }
    for(int j=1;j<=m;j++){
        cin>>b[j];
    }
    for(int l=1;l<=m;l++){
        cin>>c[l];
    }
    cout<<n<<endl;
    cout<<m<<endl;
    for(int z=1;z<=m;z++){
        int mnow=b[z];
        int cnow=c[z];
        int seed=b[z];
        while(seed<=n){
            a[seed]=(a[seed]*cnow)%1000000007;
            seed=seed+mnow;
        }
    }
    for(int k=1;k<=n;k++){
        cout<<a[k]%1000000007<<" ";
    }

}
