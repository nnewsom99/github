#include "stdio.h"

int main(void) {
  // local declarations
 
  int  dollars, Quarters, Dimes, Nickels, Pennies, centAmount;
  double initial_amount;
 
 //statements
  
  printf("How much do you need? Enter amount x.xx.\n");
  scanf("%lf", &initial_amount);
  printf("Your bank will dispense $%0.2lf.\n", initial_amount);
  
  //equations 
  
  centAmount = initial_amount * 100; //converts from dollars to cents
  dollars = centAmount / 100;
  Quarters = (centAmount % 100)/25; 
  Dimes = (centAmount % 25)/10;
  Nickels = (centAmount % 25%10)/5; /*two dividors used here because 5 is a multiple of 
  25; otherwise the screen would show inncorect numbers for the number of nickels*/
  Pennies = (centAmount % 5);
  
  //More statements
  printf("%d dollars\n", dollars);
  printf("%d quarters\n",  Quarters);
  printf("%d dimes\n",  Dimes);
  printf("%d nickels\n",  Nickels); 
  printf("%d pennies\n",  Pennies);
  printf("Please remove cash. Have a nice day.");
  
  return 0;
}
