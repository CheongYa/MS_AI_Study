// const number = Number(prompt("숫자를 입력하세요:"));

// if (number !== null) {
//     // 입력된 숫자가 3의 배수인지 확인합니다.
//     if (number % 3 === 0) {
//         // 3의 배수일 경우
//         console.log("3의 배수입니다.");
//     } else {
//         // 3의 배수가 아닐 경우
//         console.log("3의 배수가 아닙니다.");
//     }
// } else {
//     console.log("빈 값을 입력하였습니다. 값을 입력해주세요.")
// }

const mainID = "Admin";
const mainPwd = "pwd1234";

const userID = prompt("아이디를 입력해주세요: ");

if (userID === null) {
    console.log("취소되었습니다.");
} else if (mainID !== userID) {
    console.log("인증에 실패하였습니다.");
} else {
    const userPwd = prompt("비밀번호를 입력해주세요: ");
    if (userPwd === null) {
        console.log("취소되었습니다");
    } else if (mainPwd !== userPwd) {
        console.log("인증에 실패하였습니다.");
    } else {
        console.log("환영합니다!")
    }
}