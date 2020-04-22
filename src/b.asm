section  .data
  	   a dd 10
   	   b dd 10
   	   z dw 10
   	   c db "monali" ,10,0
section .bss
       f resw 2
       d resb 2
       g resd 2
       h resb 2
section .text

global main
    extern printf,abc,pqr
   
main:      
       call d   
       add eax,10
mk:    mov eax,10
       jmp cal
cal:   call printf
       push d
cal:   jmp mk
