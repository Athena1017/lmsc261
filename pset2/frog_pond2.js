const activities = ["babysit tadpoles", 
    "flies for lunch", 
    "tongue stretch", 
    "swimming lesson"];

let index = prompt("What's the frog up to today? Enter any number:");
index = Number(index) % activities.length;

print(activities[index]);