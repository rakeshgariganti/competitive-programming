#include <stdio.h>

int main()
{
	int t;
	scanf("%d",&t);
	while(t--){
		long long int n;
		scanf("%lld",&n);
		printf("%d",(n*(n+1))/2);
	}
    return 0;
}
