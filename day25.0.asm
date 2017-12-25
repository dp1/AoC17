bits 64

global main
extern printf

section .text

main:
	mov rcx, qword [n]
	mov rax, qword [state]
	mov rbx, qword [pos]
	xor rdx, rdx
	xor r12, r12
	
.loop:
	cmp rdx, rcx
	jge .end
	
	mov r8, qword [rbx * 8 + tape]
	mov r9, rax
	imul r9, 48
	add r9, qword states
	lea r9, [r9 + r8 * 8]
	lea r9, [r9 + r8 * 8]
	lea r9, [r9 + r8 * 8]
	
	mov r10, qword [r9]
	mov qword [rbx * 8 + tape], r10
	add rbx, qword [r9 + 8]
	mov rax, qword [r9 + 16]
	
	cmp r8, 0
	jnz .f1
	cmp qword [r9], 1
	jnz .f1
	add r12, 1
.f1:
	
	cmp r8, 1
	jnz .f2
	cmp qword [r9], 0
	jnz .f2
	sub r12, 1
.f2:
	
	inc rdx
	jmp .loop
	
.end:
	xor eax, eax
	mov rdi, qword format
	mov rsi, r12
	call printf
	ret

section .data
states:
	dq 1, 1, 1, 0, 1, 2   ;'A'
	dq 0, -1, 0, 0, 1, 3  ;'B'
	dq 1, 1, 3, 1, 1, 0   ;'C'
	dq 1, -1, 4, 0, -1, 3 ;'D'
	dq 1, 1, 5, 1, -1, 1  ;'E'
	dq 1, 1, 0, 1, 1, 4   ;'F'

state dq 0
pos dq 12368930 ; Start in the middle of the tape
n dq 12368930

format db "%d", 10, 0

section .bss
tape resq 12368930 * 2
