const priceOfIceCream = 5;
let paymentRecieved = prompt("How many dollars do you have in your pocket?");
let isPaymentEnough = Number(paymentRecieved) >= priceOfIceCream;

if (isPaymentEnough) {
    print("Thanks! Enjoy the Ice Cream!");
} else {
    print("Not enough cash!");
}

const change = Number(paymentRecieved) - priceOfIceCream;

if(isPaymentEnough) {
    print("Your change is: $" + change.toFixed(2));
}