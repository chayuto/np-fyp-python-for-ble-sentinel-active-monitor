// Code tested with BeagleBone Black
//   and  LinkSprite 16 X 2 LCD Keypad Shield for Arduino
//   Code inspired by library for Arduino
//     https://code.google.com/p/arduino/source/browse/trunk/libraries/LiquidCrystal/LiquidCrystal.cpp
//   and the book
//     Bad to the Bone

var b = require('bonescript');

// String to display
var my_string = "FALL DETECTED!!";

// Pins used 
var lcd_pin_D4 = "P8_11";
var lcd_pin_D5 = "P8_12";
var lcd_pin_D6 = "P8_13";
var lcd_pin_D7 = "P8_14";
var lcd_rs = "P8_15";
var lcd_e = "P8_16";

b.pinMode(lcd_pin_D4, b.OUTPUT);
b.pinMode(lcd_pin_D5, b.OUTPUT);
b.pinMode(lcd_pin_D6, b.OUTPUT);
b.pinMode(lcd_pin_D7, b.OUTPUT);
b.pinMode(lcd_rs, b.OUTPUT);
b.pinMode(lcd_e, b.OUTPUT);

b.digitalWrite(lcd_pin_D4, b.LOW);
b.digitalWrite(lcd_pin_D5, b.LOW);
b.digitalWrite(lcd_pin_D6, b.LOW);
b.digitalWrite(lcd_pin_D7, b.LOW);
b.digitalWrite(lcd_rs, b.LOW);
b.digitalWrite(lcd_e, b.LOW);

// ----- Main part -----
LCD_init( function () { write_string_to_lcd(my_string, function() {} ); } );

// ----- Initialization of LCD -----
function LCD_init(callback) {
    // LCD Enable (E) pin low
    b.digitalWrite(lcd_e, b.LOW);
    // Start at the beginning of the list of steps to perform
    var i = 0;
    // List of steps to perform
    var steps = [
        function(){ setTimeout(next, 50); }, // Wait 50 ms (time for the current to reach LCD)
        // We start in 8bit mode, try to set 4 bit mode
        function(){ write4bits(0x03, next); },
        function(){ setTimeout(next, 5); },
        // Second try
        function(){ write4bits(0x03, next); },
        function(){ setTimeout(next, 5); },
        // Third try
        function(){ write4bits(0x03, next); },
        function(){ setTimeout(next, 2); },
        function(){ write4bits(0x02, next); }, // Finally, set to 8-bit interface
        function(){ write_bits_to_lcd(0x28, true, next); }, // Finally, set # lines, font size, etc.
        function(){ write_bits_to_lcd(0x0C, true, next); }, // Turn the display on with no cursor or blinking default
        function(){ write_bits_to_lcd(0x06, true, next); }, // Setup Cursor/Display
        function(){ write_bits_to_lcd(0x01, true, callback); } // Clear the display
        // That's all
        ];
    next(); //Execute the first step
    //Function for executing the next step
    function next() {
        i++;
        steps[i-1]();
    }
}

// ----- Writing to the lcd -----
// Can write bits, a string, or 2 lines to lcd
function write_bits_to_lcd(value, command_or_character, callback) {
    // true = it is a command
    // false = it is a character to display
    var value_left = (value >> 4); // The left 4 bits
    if (command_or_character === true) b.digitalWrite(lcd_rs, b.LOW); //LCD Register Set (RS) to logic zero for command input
        else b.digitalWrite(lcd_rs, b.HIGH);  //LCD Register Set (RS) to logic one for character input
    write4bits(value_left, function() { write4bits(value, callback); } );
}

function write4bits(value, callback) {
    // Works for 4bits command
    //   Parse command variable into individual bits for output to LCD
    if((value >> 3) & 0x01) b.digitalWrite(lcd_pin_D7, b.HIGH);
        else b.digitalWrite(lcd_pin_D7, b.LOW);
    if((value >> 2) & 0x01) b.digitalWrite(lcd_pin_D6, b.HIGH);
        else b.digitalWrite(lcd_pin_D6, b.LOW);
    if((value >> 1) & 0x01) b.digitalWrite(lcd_pin_D5, b.HIGH);
        else b.digitalWrite(lcd_pin_D5, b.LOW);
    if(value & 0x01) b.digitalWrite(lcd_pin_D4, b.HIGH);
        else b.digitalWrite(lcd_pin_D4, b.LOW);
    //LCD Enable (E) pin high
    b.digitalWrite(lcd_e, b.HIGH);
    //LCD Enable (E) pin low
    b.digitalWrite(lcd_e, b.LOW);
    callback();
}

function write_string_to_lcd(s, callback) {
    var s_length = s.length;
    // Check the length of the string, split it if needed
    if (s_length > 32) {
        write_string_to_lcd_two_lines('ERROR:', 'String too long', callback);
        return;
    }
    if (s_length < 17) {
        write_bits_to_lcd(0x80, true, function () { helper_lcd_display_string(s, callback ); } );
    } else {
        write_string_to_lcd_two_lines(s.slice(0,16), s.slice(16, s_length), callback);
    }
}

function write_string_to_lcd_two_lines(line1, line2, callback) {
    // command 0x80 puts the cursor at the beginning of the first line
    write_bits_to_lcd(0x80, true, function () { helper_lcd_display_string(line1, function() {second_line();} ); } );
    function second_line() {
        // command 0xC0 puts the cursor at the beginning of the second line
        write_bits_to_lcd(0xC0, true, function () { helper_lcd_display_string(line2, callback ); } );
    }
}

function helper_lcd_display_string(s, callback) {
    if (s.length === 0) {
        callback();
    } else {
        write_bits_to_lcd(s.charCodeAt(0), false, function() {helper_lcd_display_string(s.slice(1), callback);} );
    }
}
