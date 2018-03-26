#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

int main(int argc, char *argv[]){
	pid_t pid;

	// signal(SIGCHLD, SIG_IGN);
	pid = fork();
	
	// sleep(30);
	if (pid > 0) { // Parent
		//printf("pid: %d\n", pid);
		printf("Parent - pid: %d\n", pid);
		sleep(10);
		
	} else if (pid == 0) { // child
		//sleep(10);
		printf("child - pid %d\n", pid);
	} else {
		printf("Error\n");
	}

	return 0;
}

