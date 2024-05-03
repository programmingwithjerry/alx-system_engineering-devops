#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */

int main(void)	/* Main function */
{
	pid_t pid;	/* Process ID variable */
	int count;

	/* Use a for loop to create 5 child processes that become zombies */
	for (count = 0; count < 5; count++)	/* Loop 5 times */
	{
		pid = fork();	/* Create a new child process */
		if (pid > 0)	/* Parent process */
		{
			printf("Zombie process created, PID: %d\n", pid);/* Display child's PID */
			sleep(1);	/* Pause for 1 second */
		}
		else	/* Child process */
		{
			exit(0);/* Child exits immediately, creating a zombie */
		}
	}

	/* Enter an infinite loop to keep the parent process running */
	infinite_while();	/* Keep the parent process alive */

	return (EXIT_SUCCESS);	/* Return successful exit status */
}
