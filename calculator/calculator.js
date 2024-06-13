document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    let currentOperand = '';
    let previousOperand = '';
    let operation = null;

    const clear = () => {
        currentOperand = '';
        previousOperand = '';
        operation = null;
        updateDisplay();
    };

    const appendNumber = (number) => {
        if (number === '.' && currentOperand.includes('.')) return;
        currentOperand = currentOperand.toString() + number.toString();
        updateDisplay();
    };

    const chooseOperation = (op) => {
        if (currentOperand === '') return;
        if (previousOperand !== '') {
            compute();
        }
        operation = op;
        previousOperand = currentOperand;
        currentOperand = '';
    };

    const compute = () => {
        let result;
        const prev = parseFloat(previousOperand);
        const curr = parseFloat(currentOperand);
        if (isNaN(prev) || isNaN(curr)) return;
        switch (operation) {
            case '+':
                result = prev + curr;
                break;
            case '-':
                result = prev - curr;
                break;
            case '*':
                result = prev * curr;
                break;
            case '/':
                result = prev / curr;
                break;
            default:
                return;
        }
        currentOperand = result;
        operation = null;
        previousOperand = '';
        updateDisplay();
    };

    const updateDisplay = () => {
        display.innerText = currentOperand || '0';
    };

    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', () => {
            const value = button.value;
            if (button.classList.contains('operand')) {
                appendNumber(value);
            } else if (button.classList.contains('operator')) {
                chooseOperation(value);
            } else if (button.classList.contains('equal')) {
                compute();
            } else if (button.classList.contains('clear')) {
                clear();
            } else if (button.classList.contains('decimal')) {
                appendNumber(value);
            } else if (button.classList.contains('sign')) {
                if (currentOperand !== '') {
                    currentOperand = (parseFloat(currentOperand) * -1).toString();
                    updateDisplay();
                }
            } else if (button.classList.contains('percent')) {
                if (currentOperand !== '') {
                    currentOperand = (parseFloat(currentOperand) / 100).toString();
                    updateDisplay();
                }
            }
        });
    });
});
