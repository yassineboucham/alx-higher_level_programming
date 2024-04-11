#!/usr/bin/node
// Specifies that this script should be executed with the Node.js interpreter

// Exporting a class named Square
module.exports = class Square extends require('./5-square.js') {
    // Method to print a square made of a specific character
    charPrint(c) {
      // If no character is provided, call the print method of the parent class
      if (c === undefined) {
        this.print();
      } else {
        // Print the square using the provided character
        for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
      }
    }
  };
  