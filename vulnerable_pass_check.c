//A VULNERABLE PASSWORD CHECKING PROGRAM

#include<stdio.h>
#include<string.h>

int main(){
	
	int login_allow = 0;
	char password[12];
	char target_pass[12] = "Mypwd123";

	gets(password);
	if(strncmp(password, target_pass, 12)==0){
		login_allow=1;
		if(login_allow==0){
			printf("Login request rejected\n");
		}
		else {
			printf("Login request allowed\n");
		}
	}
}