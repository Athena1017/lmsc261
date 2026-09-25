const conesSoldPerHour = 14;
const inventory = 200;

for (let hour = 1; hour <= 12; hour++) {
    print(conesSoldPerHour * hour + " sold at hour " + hour);
    print(inventory - conesSoldPerHour * hour + " left");
}