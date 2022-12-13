/* Prints table of 
sine and cosines between 0 and 1 */

#include<stdio.h>
#include<math.h>
int main(void)
{ 
	
	float interval,x,y;
	int i;

	for(i = 0; i <10; i++)
	{
 		interval = i/10.0;
		x=(sin(interval));
		y=(cos(interval));
 		printf("sine(%f)=%f\t cosine(%f)=%f\n",interval,x,interval,y);
	}	

return 0;

}