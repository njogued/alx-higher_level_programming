#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    this.temp = this.width;
    this.width = this.height;
    this.height = this.temp;
  }
}
module.exports = Rectangle;
