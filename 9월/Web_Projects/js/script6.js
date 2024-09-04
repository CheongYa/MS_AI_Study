const pwd = '1234';
let userpwd;

do {
    userpwd = prompt('비밀번호 입력: ')
} while (pwd !== userpwd);

console.log('탈출')