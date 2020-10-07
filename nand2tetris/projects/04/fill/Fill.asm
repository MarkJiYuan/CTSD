// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Initialize keyboard address
(INIT)
    // length = 8192
    @8192
    D=A
    @length
    M=D

    // prev = 0
    @prev
    M=0

    // color = 0
    @color
    M=0

(CHECK)
    // i = 0
    @i
    M=0
    // addr = SCREEN
    @SCREEN
    D=A
    @addr
    M=D

    // if keycode == 0:
    //     if prev == 0: goto CHECK
    //     else: prev = 0; color = 0;
    // else:
    //     if prev != 0 goto CHECK
    //     else: prev = 1; color = -1;

    @24576
    D=M
    @KEY_NZ
    D;JNE

    (KEY_ZERO)
    @prev
    D=M
    @KEY_ZERO_PREV_NZ
    D;JNE
    (KEY_ZERO_PREV_ZERO)
    @CHECK
    0;JMP

    (KEY_ZERO_PREV_NZ)
    @prev
    M=0
    @color
    M=0
    @DRAW
    0;JMP

    (KEY_NZ)
    @prev
    D=M
    @KEY_NZ_PREV_ZERO
    D;JEQ
    (KEY_NZ_PREV_NZ)
    @CHECK
    0;JMP

    (KEY_NZ_PREV_ZERO)
    @prev
    M=1
    @color
    M=-1
    @DRAW
    0;JMP

(DRAW)
    @i
    D=M
    @length
    D=D-M
    @CHECK
    D;JEQ


    @color
    D=M
    @COLOR_NZ
    D;JNE
    (COLOR_ZERO)
    @addr
    A=M
    M=0
    @DRAW_INCREMENT
    0;JMP

    (COLOR_NZ)
    @addr
    A=M
    M=-1

    (DRAW_INCREMENT)
    @addr
    M=M+1
    @i
    M=M+1
    @DRAW
    0;JMP









