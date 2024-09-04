const rawInput = Number(prompt("태어난 해를 입력해 주세요 : ", ''));
const year = rawInput % 12;

let result;

switch(year) {
    case 0: result = '원숭이';break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 1: result = '닭'; break;
    case 11: result = '양'; break;
}
console.log(`${rawInput}년에 태어났다면 ${result}띠 입니다`)