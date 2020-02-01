grammar mvasm;


program : (instr NEWLINE)* instr NEWLINE*
        ;


instr   :   LD reg COMMA mem    #instrLD
        |   ST reg COMMA mem    #instrST
        |   MOV reg COMMA reg   #instrMOV
        |   PSH reg             #instrPSH
        |   POP reg             #instrPOP
        |   bug_instr           #instrBug_Instr
        ;

bug_instr   :   SRCF             #instrSRCF
            |   WLKT             #instrWLKT
            |   WLKW             #instrwlkW
            |   WLK reg          #instrWLK
            ;

mem     :   address                     #memRel
        |   OBRACE address CBRACE       #memAbs
        ;

address :   number
        |   gen_reg
        ;

gen_reg     : 'R' DIGIT+
        ;

reg     :   gen_reg
        |   'CS' | 'CH' | 'DS' | 'PC' | 'SP'
        ;


number  :   DIGIT+
        ;

LD  :   'LD';
ST  :   'ST';
MOV :   'MOV';
PSH :   'PSH';
POP :   'POP';
SRCF:   'SRCF';
WLKT:   'WLKT';
WLKW:   'WLKW';
WLK :   'WLK';


COMMA:  ',';
OPAR:   '(';
CPAR:   ')';
OBRACE:   '{';
CBRACE:   '}';
DIGIT   : [0-9];
NEWLINE   : '\r' '\n' | '\n' | '\r';

WS
   : [ \r\n] + -> skip
   ;
