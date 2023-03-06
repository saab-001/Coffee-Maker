# Coffee Maker 

This program will operate the coffee machine and perform the functions it is commanded to. It can perform the following functions:

**For customer:**

   - Take an order for a drink from the user
   - Take payment from the user for their order
   - Return all the extra money to the user
   - Cancel the order and refund the money to the user if the amount paid is less than the amount of their order
   - Confirms the payment and provide the user their selected drink
   - Deduct the resources from the coffee machine those are used to make the drink selected by the user and store the money in the machine
   - If there are not enough resources to create a drink. It tells user that there aren't enough resources to make the drink before going to payment section
   - If there are not enough resources to create any of the drinks. It turns off the machine automatically.

**For Owner/Worker:**

  - Shows the report of all the available resources and money stored in the machine `keyword: report`
  - Turns the machine off if commanded to do so. `keyword: off`
