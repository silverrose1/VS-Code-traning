console.log(["Nebula","Thanos","Star","Groot","Rocket"].sort()) //string
console.log(["Nebula","Thanos","Star","Groot","Rocket"].sort().reverse()) //string

console.log([9, 3, 12, 11, 40, 28, 5].sort((a, b) => a - b)) //number
console.log([9, 3, 12, 11, 40, 28, 5].sort((a, b) => b - a))

books = [
  { title: "Book A", year: 2010 },
  { title: "Book B", year: 2005 },
  { title: "Book C", year: 2018 },
];
console.log(books.sort((a, b) => a.year - b.year)); //number
console.log(books.sort((a, b) => b.year - a.year)); //number
console.log(books.sort((a, b) => a.title.localeCompare(b.title))); //string
console.log(books.sort((a, b) => b.title.localeCompare(a.title))); //string

const names = ["Mike Smith", "Dr. Johnson", "John Doe", "Dr. Williams"];

names.sort((a, b) => {
  if (a.startsWith("Dr.") && !b.startsWith("Dr.")) {
    return -1;
  } else if (!a.startsWith("Dr.") && b.startsWith("Dr.")) {
    return 1;
  } else {
    return a.localeCompare(b); // sort alphabetically
  }
});

console.log(names);


const items = ["b", "3", "a", "2", "c", "1"];
items.sort((a, b) => {
  const aIsNumber = !isNaN(a); // isNaN = is Not a Number
  const bIsNumber = !isNaN(b);

  if (aIsNumber && !bIsNumber) {
    return -1; // numbers should be sorted before letters
  } else if (!aIsNumber && bIsNumber) {
    return 1; // letters should be sorted after numbers
  } else if (aIsNumber && bIsNumber) {
    return a - b; // sort numbers numerically
  } else {
    return a.localeCompare(b); // sort letters alphabetically
  }
});

console.log(items);
