grammar mvasm;


program : (instr NEWLINE)* instr NEWLINE*
        ;


instr   :   LD wrt_reg COMMA val    #instrLD
        |   ST reg COMMA mem        #instrST
        |   MOV reg COMMA reg       #instrMOV
        |   PSH reg                 #instrPSH
        |   POP reg                 #instrPOP
        |   bug_instr               #instrBug_Instr
        ;

bug_instr   :   SRCF             #instrSRCF
            |   WLKT             #instrWLKT
            |   WLKW             #instrwlkW
            |   WLK reg          #instrWLK
            ;

val     :   mem                  #valmem
        |   OPAR number CPAR     #valnumber
        ;

mem     :   address                     #memRel
        |   OBRACE address CBRACE       #memAbs
        ;

address :   number
        |   reg
        ;

reg     :   wrt_reg | prt_reg ;

wrt_reg :   gen_reg
        |   SRF
        ;

gen_reg     : 'R' DIGIT+
        ;

prt_reg :   'CS' | 'CH' | 'DS' | 'PC' | 'SP' | 'SRR' | 'DRS'
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
SRF :   'SRF';


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
