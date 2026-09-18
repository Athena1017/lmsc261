const maxFrogCapacity = 15;
let numFrogs = prompt("How many frogs are about to jump in?");
let isPondOverCapacity = numFrogs > maxFrogCapacity;
let messageToPrint = isPondOverCapacity ? "It's too crowded!" : "Come on in!";
print(messageToPrint);