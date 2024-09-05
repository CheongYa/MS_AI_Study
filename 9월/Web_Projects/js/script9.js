document.addEventListener('DOMContentLoaded', () => {
    // const h1 = document.querySelector('h1')
    // const textarea = document.querySelector('textarea')

    // textarea.addEventListener('keyup', (event) => {
    //     const length = textarea.value.length;
    //     h1.textContent = `글자 수: ${length}`;
    // })

    const input = document.querySelector('input');
    const p = document.querySelector('p');

    const isEmail = (value) => {
        return (value.indexof('@' > 1) && (value.split('@')[1].indexof('.') > 1))
    }

    input.addEventListener('keyup', (event) => {
        const value = event.currentTarget.value;
        if(isEmail(value)) {
            p.style.color = 'green'
            p.textContent = `이메일 형식: ${value}`
            
        } else {

        }
    })
})