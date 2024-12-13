let contacts = [{
  name: "Maxwell Wright",
  phone: "(0191) 719 6495",
  email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
  name: "Raja Villarreal",
  phone: "0866 398 2895",
  email: "posuere.vulputate@sed.com"
}, {
  name: "Helen Richards",
  phone: "0800 1111",
  email: "libero@convallis.edu"
}];

// Array.isArray(contacts) //check if array
// contacts instanceof Array // Old way..check if array



let showContact = (n) =>
  Array.isArray(contacts) && typeof n === 'number' && n >= 0 && n < contacts.length // if condition
  ? contacts[n] // True return
  : undefined; // Or throw an error:  throw new Error("Invalid input");
  
let showAllContact = () =>
  Array.isArray(contacts) // if condition
  ? contacts // True return
  : undefined; // Or throw an error:  throw new Error("Invalid input");
  
  console.log(showAllContact()); // Logs the array of contact objects
    
let addContact = (name, phone, email) =>
  Array.isArray(contacts) && typeof name === 'string' && typeof phone === 'string' && typeof email === 'string' // if condition
  ? contacts.push({ name, phone, email }) // True return
  : NaN; // Or throw an error:  throw new Error("Invalid input");

isDone=false;
while (!isDone){
  let choice = prompt("choose: 1- add new contact 2- show all contacts 3- show contact by index 4- sort contacts 5- exit");
  
   
  switch (choice) {
    case null:
      isDone=true;
      break;
    case "5":
      isDone=true;
      break;
    case '1':
      let name = prompt("Enter name");
      let phone = prompt("Enter phone");
      let email = prompt("Enter email");

      addContact(name, phone, email)
      console.log(showAllContact());
      
      break;
    case '2':
      console.log(showAllContact());
      break;

    case '3':
      let index = prompt("Enter index");
      console.log(showContact(Number(index)));
      break;

    case '4':
      let sort = prompt('1-name 2-phone 3-email')
      switch (sort) {
        case '1':
          contacts.sort((a,b) => a.name.localeCompare(b.name))
          break;
        case '2':
          contacts.sort((a,b) => a.phone.localeCompare(b.phone))
          break;
        case '3':
          contacts.sort((a,b) => a.email.localeCompare(b.email))
          break;
        default:
          isDone=true;
          break;
      }
   
   
   }
   
} 


